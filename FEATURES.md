# Fonctionnalités Avancées - MondeRH

## 📋 Table des matières

1. [Système d'authentification](#système-dauthentification)
2. [Formulaire de candidature en ligne](#formulaire-de-candidature-en-ligne)
3. [Module de prise de rendez-vous](#module-de-prise-de-rendez-vous)
4. [Espace client sécurisé](#espace-client-sécurisé)
5. [Intégration LinkedIn](#intégration-linkedin)
6. [Newsletter](#newsletter)
7. [Chat en ligne](#chat-en-ligne)
8. [Base de données](#base-de-données)
9. [Système d'emails](#système-demails)

---

## 🔐 Système d'authentification

### Fonctionnalités
- **Inscription** : Création de compte avec validation des données
- **Connexion** : Authentification sécurisée avec hachage des mots de passe
- **Types d'utilisateurs** : Candidats et clients avec permissions différentes
- **Sessions sécurisées** : Gestion des sessions avec Flask-Login
- **Déconnexion** : Fermeture sécurisée des sessions

### Utilisation
```python
# Routes disponibles
/login - Page de connexion
/register - Page d'inscription
/logout - Déconnexion
/dashboard - Tableau de bord (protégé)
```

---

## 📝 Formulaire de candidature en ligne

### Fonctionnalités
- **Formulaire complet** : Informations personnelles, expérience, disponibilité
- **Upload de fichiers** : CV en PDF, DOC, DOCX (max 16MB)
- **Lettre de motivation** : Zone de texte pour présentation
- **Validation** : Vérification des données côté client et serveur
- **Intégration LinkedIn** : Import automatique des profils
- **Notifications** : Email automatique de confirmation

### Champs du formulaire
- Poste recherché
- Type de service (Recrutement, Coaching, Formation, etc.)
- Années d'expérience
- Disponibilité
- Prétentions salariales
- URL LinkedIn
- CV (fichier)
- Lettre de motivation

### Utilisation
```python
# Route
/apply - Formulaire de candidature
```

---

## 📅 Module de prise de rendez-vous

### Fonctionnalités
- **Calendrier interactif** : Sélection de date et heure
- **Validation temporelle** : Empêche les RDV dans le passé
- **Durées flexibles** : 30min, 1h, 1h30, 2h
- **Services multiples** : Tous les services MondeRH
- **Confirmation automatique** : Email de confirmation
- **Gestion des RDV** : Vue d'ensemble et détails

### Utilisation
```python
# Routes
/appointments - Prise de RDV et liste
```

---

## 🏠 Espace client sécurisé

### Fonctionnalités
- **Tableau de bord** : Vue d'ensemble des activités
- **Statistiques** : Nombre de candidatures, RDV, etc.
- **Gestion des candidatures** : Suivi des statuts
- **Gestion des RDV** : Planning et détails
- **Actions rapides** : Liens directs vers les fonctionnalités
- **Interface responsive** : Adapté à tous les appareils

### Sections du dashboard
- **Statistiques** : Candidatures, RDV, statuts
- **Mes candidatures** : Tableau avec filtres
- **Actions rapides** : Nouvelle candidature, RDV, LinkedIn
- **Prochains RDV** : Planning des rendez-vous

---

## 🔗 Intégration LinkedIn

### Fonctionnalités
- **Import de profil** : Récupération automatique des données
- **Authentification OAuth** : Connexion sécurisée à LinkedIn
- **Synchronisation** : Mise à jour des informations
- **API LinkedIn** : Utilisation de l'API officielle

### Configuration
```python
# Variables d'environnement requises
LINKEDIN_CLIENT_ID=your-client-id
LINKEDIN_CLIENT_SECRET=your-client-secret
```

---

## 📧 Newsletter

### Fonctionnalités
- **Inscription** : Formulaire simple sur la page d'accueil
- **Gestion des préférences** : Choix des services d'intérêt
- **Base de données** : Stockage des abonnés
- **Validation** : Vérification des emails
- **Désabonnement** : Possibilité de se désinscrire

### Utilisation
```python
# Route
/newsletter - Inscription à la newsletter
```

---

## 💬 Chat en ligne

### Fonctionnalités
- **Widget flottant** : Bouton de chat en bas à droite
- **Interface moderne** : Design professionnel
- **Messages en temps réel** : Communication instantanée
- **Historique** : Conservation des conversations
- **Responsive** : Adapté mobile et desktop

### API Chat
```python
# Endpoint
POST /api/chat/message
{
    "message": "Votre message"
}
```

---

## 🗄️ Base de données

### Modèles

#### User
- Informations utilisateur (email, nom, type, etc.)
- Relations avec candidatures et RDV

#### Application
- Candidatures avec statuts
- Fichiers uploadés et métadonnées

#### Appointment
- Rendez-vous avec planning
- Statuts et descriptions

#### Newsletter
- Abonnés avec préférences
- Gestion des désabonnements

### Utilisation
```python
# Création des tables
with app.app_context():
    db.create_all()
```

---

## 📬 Système d'emails

### Fonctionnalités
- **Configuration SMTP** : Support Gmail et autres fournisseurs
- **Templates** : Emails personnalisés
- **Notifications automatiques** : Candidatures, RDV, contact
- **Gestion des erreurs** : Logs et retry automatique

### Types d'emails
- **Confirmation de candidature**
- **Confirmation de RDV**
- **Notifications de contact**
- **Newsletter** (préparé)

### Configuration
```python
# Variables d'environnement
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email
MAIL_PASSWORD=your-password
```

---

## 🔧 Configuration

### Variables d'environnement
Copiez le fichier `env.example` vers `.env` et configurez :

```bash
# Flask
SECRET_KEY=your-secret-key
FLASK_ENV=development

# Email
MAIL_USERNAME=contact@monderh.fr
MAIL_PASSWORD=your-password

# LinkedIn (optionnel)
LINKEDIN_CLIENT_ID=your-client-id
LINKEDIN_CLIENT_SECRET=your-client-secret

# Base de données
DATABASE_URL=sqlite:///monderh.db
```

### Démarrage
```bash
# Installation
pip install -r requirements.txt

# Base de données
python -c "from app import db; db.create_all()"

# Lancement
python app.py
```

---

## 🚀 Déploiement

### Production
1. **Variables d'environnement** : Configurez toutes les variables
2. **Base de données** : Utilisez PostgreSQL ou MySQL
3. **Serveur WSGI** : Gunicorn ou uWSGI
4. **Serveur web** : Nginx ou Apache
5. **SSL** : Certificat Let's Encrypt

### Sécurité
- **HTTPS obligatoire** en production
- **Clés secrètes** changées
- **Permissions** des fichiers uploadés
- **Validation** côté serveur
- **Logs** de sécurité

---

## 📞 Support

Pour toute question sur les fonctionnalités :
- **Email** : contact@monderh.fr
- **Documentation** : Ce fichier et le README.md
- **Code** : Commentaires dans le code source 