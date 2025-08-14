from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session, abort, Response, make_response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, FileField, DateField, TimeField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
from datetime import datetime, timedelta, timezone
import json
from functools import wraps
from io import StringIO
import csv
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Configuration de la base de données
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL and DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL or 'sqlite:///monderh.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', 'contact@monderh.fr')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', '')

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
mail = Mail(app)

# Create upload folder
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    user_type = db.Column(db.String(20), default='candidate')  # candidate, client, admin
    company = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    is_active = db.Column(db.Boolean, default=True)
    
    # Relationships
    applications = db.relationship('Application', backref='applicant', lazy=True)
    appointments = db.relationship('Appointment', backref='user', lazy=True)
    
    def is_admin(self):
        return self.user_type == 'admin'

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)  # recrutement, coaching, formation, etc.
    cv_filename = db.Column(db.String(200))
    google_drive_link = db.Column(db.String(500))
    cover_letter = db.Column(db.Text)
    linkedin_url = db.Column(db.String(200))
    experience_years = db.Column(db.Integer)
    salary_expectation = db.Column(db.String(50))
    availability = db.Column(db.String(50))
    status = db.Column(db.String(20), default='pending')  # pending, reviewed, accepted, rejected
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    notes = db.Column(db.Text)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    duration = db.Column(db.Integer, default=60)  # minutes
    subject = db.Column(db.String(200))
    description = db.Column(db.Text)
    google_calendar_link = db.Column(db.String(500))
    status = db.Column(db.String(20), default='pending')  # pending, confirmed, cancelled, completed
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

class JobOffer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    contract_type = db.Column(db.String(50), nullable=False)  # CDI, CDD, Stage, Alternance
    experience_level = db.Column(db.String(50), nullable=False)  # Junior, Confirmé, Senior, Expert
    salary_range = db.Column(db.String(100))
    description = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text, nullable=False)
    benefits = db.Column(db.Text)
    department = db.Column(db.String(100))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

# Forms
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    remember_me = BooleanField('Se souvenir de moi')
    submit = SubmitField('Se connecter')

class RegistrationForm(FlaskForm):
    first_name = StringField('Prénom', validators=[DataRequired()])
    last_name = StringField('Nom', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    account_type = SelectField('Type de compte', choices=[
        ('candidate', 'Candidat'),
        ('client', 'Client')
    ])
    password = PasswordField('Mot de passe', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirmer le mot de passe', validators=[
        DataRequired(), 
        EqualTo('password', message='Les mots de passe doivent correspondre')
    ])
    accept_terms = BooleanField('J\'accepte les conditions d\'utilisation', validators=[DataRequired()])
    company = StringField('Entreprise')
    phone = StringField('Téléphone')
    submit = SubmitField('S\'inscrire')

class ApplicationForm(FlaskForm):
    position = StringField('Poste recherché', validators=[DataRequired()])
    service_type = SelectField('Type de service', choices=[
        ('recrutement', 'Recrutement'),
        ('coaching', 'Coaching'),
        ('formation', 'Formation'),
        ('interim', 'Intérim'),
        ('conseil', 'Conseil en Organisation')
    ])
    experience_years = SelectField('Années d\'expérience', choices=[
        ('0-1', '0-1 an'),
        ('1-3', '1-3 ans'),
        ('3-5', '3-5 ans'),
        ('5-10', '5-10 ans'),
        ('10+', '10+ ans')
    ])
    salary_expectation = StringField('Prétentions salariales')
    availability = SelectField('Disponibilité', choices=[
        ('immediate', 'Immédiate'),
        ('1-2-weeks', '1-2 semaines'),
        ('1-month', '1 mois'),
        ('3-months', '3 mois'),
        ('flexible', 'Flexible')
    ])
    cover_letter = TextAreaField('Lettre de motivation')
    cv_file = FileField('CV (PDF)')
    submit = SubmitField('Soumettre ma candidature')

class AppointmentForm(FlaskForm):
    service_type = SelectField('Service', choices=[
        ('recrutement', 'Recrutement'),
        ('coaching', 'Coaching'),
        ('formation', 'Formation'),
        ('interim', 'Intérim'),
        ('conseil', 'Conseil en Organisation')
    ], validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    time = TimeField('Heure', validators=[DataRequired()])
    duration = SelectField('Durée', choices=[
        (30, '30 minutes'),
        (60, '1 heure'),
        (90, '1h30'),
        (120, '2 heures')
    ], default=60)
    subject = StringField('Sujet', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Prendre rendez-vous')

# User loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Admin decorator
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin():
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page:
                next_page = url_for('dashboard')
            return redirect(next_page)
        else:
            flash('Email ou mot de passe incorrect', 'error')
    
    return render_template('auth/login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            flash('Cet email est déjà utilisé', 'error')
        else:
            user = User(
                email=form.email.data,
                password_hash=generate_password_hash(form.password.data),
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                user_type=form.account_type.data,
                company=form.company.data,
                phone=form.phone.data
            )
            db.session.add(user)
            db.session.commit()
            flash('Compte créé avec succès! Vous pouvez maintenant vous connecter.', 'success')
            return redirect(url_for('login'))
    
    return render_template('auth/register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.is_admin():
        return redirect(url_for('admin_dashboard'))
    return render_template('dashboard/dashboard.html')

@app.route('/admin')
@login_required
@admin_required
def admin_dashboard():
    total_users = User.query.count()
    total_applications = Application.query.count()
    total_appointments = Appointment.query.count()
    pending_applications = Application.query.filter_by(status='pending').count()
    
    return render_template('admin/dashboard.html',
                         total_users=total_users,
                         total_applications=total_applications,
                         total_appointments=total_appointments,
                         pending_applications=pending_applications)

@app.route('/admin/applications')
@login_required
@admin_required
def admin_applications():
    page = request.args.get('page', 1, type=int)
    applications = Application.query.order_by(Application.created_at.desc()).paginate(page=page, per_page=20, error_out=False)
    return render_template('admin/applications.html', applications=applications)

@app.route('/admin/users')
@login_required
@admin_required
def admin_users():
    users = User.query.all()
    return render_template('admin/users.html', users=users)

@app.route('/careers')
def careers():
    return render_template('careers.html')

@app.route('/apply', methods=['GET', 'POST'])
@login_required
def apply():
    form = ApplicationForm()
    if form.validate_on_submit():
        application = Application(
            user_id=current_user.id,
            position=form.position.data,
            service_type=form.service_type.data,
            experience_years=form.experience_years.data,
            salary_expectation=form.salary_expectation.data,
            availability=form.availability.data,
            cover_letter=form.cover_letter.data
        )
        
        if form.cv_file.data:
            filename = secure_filename(form.cv_file.data.filename)
            form.cv_file.data.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            application.cv_filename = filename
        
        db.session.add(application)
        db.session.commit()
        flash('Candidature soumise avec succès!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('apply.html', form=form)

@app.route('/appointments', methods=['GET', 'POST'])
@login_required
def appointments():
    form = AppointmentForm()
    if form.validate_on_submit():
        appointment = Appointment(
            user_id=current_user.id,
            service_type=form.service_type.data,
            date=form.date.data,
            time=form.time.data,
            duration=form.duration.data,
            subject=form.subject.data,
            description=form.description.data
        )
        db.session.add(appointment)
        db.session.commit()
        flash('Rendez-vous pris avec succès!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('appointments.html', form=form)

# Export CSV function (simplified)
@app.route('/admin/applications/export')
@login_required
@admin_required
def admin_export_applications():
    applications = Application.query.all()
    
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(['ID', 'Candidat', 'Poste', 'Service', 'Statut', 'Date'])
    
    for app in applications:
        writer.writerow([
            app.id,
            f"{app.applicant.first_name} {app.applicant.last_name}",
            app.position,
            app.service_type,
            app.status,
            app.created_at.strftime('%Y-%m-%d')
        ])
    
    output.seek(0)
    return Response(
        output.getvalue(),
        mimetype='text/csv',
        headers={'Content-Disposition': 'attachment; filename=applications.csv'}
    )

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000) 