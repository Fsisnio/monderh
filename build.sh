#!/usr/bin/env bash
# exit on error
set -o errexit

echo "🚀 Début du build MonDRH..."

# Installer les dépendances
echo "📦 Installation des dépendances..."
pip install -r requirements.txt

# Créer le dossier uploads s'il n'existe pas
echo "📁 Création du dossier uploads..."
mkdir -p static/uploads

# Initialiser la base de données et créer les administrateurs
echo "🗄️ Configuration de la base de données PostgreSQL..."
python -c "
from app import app, db, User
from werkzeug.security import generate_password_hash

with app.app_context():
    # Créer les tables
    db.create_all()
    print('✅ Base de données initialisée!')
    
    # Créer ou vérifier l'administrateur principal
    admin1 = User.query.filter_by(email='admin@monderh.fr').first()
    if not admin1:
        admin1 = User(
            email='admin@monderh.fr',
            password_hash=generate_password_hash('admin123'),
            first_name='Admin',
            last_name='MondeRH',
            user_type='admin',
            is_active=True
        )
        db.session.add(admin1)
        print('✅ Administrateur principal créé: admin@monderh.fr')
    else:
        admin1.password_hash = generate_password_hash('admin123')
        admin1.user_type = 'admin'
        admin1.is_active = True
        print('✅ Administrateur principal mis à jour: admin@monderh.fr')
    
    # Créer ou vérifier le deuxième administrateur
    admin2 = User.query.filter_by(email='faladespero1@gmail.com').first()
    if not admin2:
        admin2 = User(
            email='faladespero1@gmail.com',
            password_hash=generate_password_hash('admin123'),
            first_name='Spero',
            last_name='Falade',
            user_type='admin',
            is_active=True
        )
        db.session.add(admin2)
        print('✅ Deuxième administrateur créé: faladespero1@gmail.com')
    else:
        admin2.password_hash = generate_password_hash('admin123')
        admin2.user_type = 'admin'
        admin2.is_active = True
        print('✅ Deuxième administrateur mis à jour: faladespero1@gmail.com')
    
    # Sauvegarder les changements
    db.session.commit()
    print('✅ Tous les administrateurs sont prêts!')
    print('')
    print('🔐 Identifiants administrateur:')
    print('   Email: admin@monderh.fr')
    print('   Mot de passe: admin123')
    print('   ---')
    print('   Email: faladespero1@gmail.com')
    print('   Mot de passe: admin123')
"

echo "✅ Build terminé avec succès!" 