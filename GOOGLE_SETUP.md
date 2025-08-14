# Configuration Google Workspace - MondeRH

Ce guide vous explique comment configurer l'intégration Google Workspace pour activer Google Drive et Google Calendar.

## 🚀 Fonctionnalités activées

- **Google Drive** : Sauvegarde automatique des CV candidats
- **Google Calendar** : Synchronisation des rendez-vous

## 📋 Prérequis

1. Un compte Google (Gmail ou Google Workspace)
2. Accès à la Google Cloud Console

## ⚙️ Configuration étape par étape

### 1. Créer un projet Google Cloud

1. Allez sur [Google Cloud Console](https://console.cloud.google.com)
2. Cliquez sur **"Créer un projet"**
3. Nommez votre projet (ex: "MondeRH-Integration")
4. Cliquez sur **"Créer"**

### 2. Activer les APIs nécessaires

1. Dans le menu, allez à **"APIs et services" > "Bibliothèque"**
2. Recherchez et activez ces APIs :
   - **Google Drive API**
   - **Google Calendar API**

### 3. Configurer l'écran de consentement OAuth

1. Allez à **"APIs et services" > "Écran de consentement OAuth"**
2. Choisissez **"Externe"** si vous n'avez pas Google Workspace
3. Remplissez les informations requises :
   - **Nom de l'application** : MondeRH
   - **Email d'assistance utilisateur** : votre email
   - **Domaines autorisés** : votre domaine (ex: monderh.fr)
4. Ajoutez les scopes :
   - `https://www.googleapis.com/auth/drive.file`
   - `https://www.googleapis.com/auth/calendar`

### 4. Créer les identifiants OAuth

1. Allez à **"APIs et services" > "Identifiants"**
2. Cliquez sur **"+ CRÉER DES IDENTIFIANTS" > "ID client OAuth 2.0"**
3. Type d'application : **"Application Web"**
4. Nom : **"MondeRH Web Client"**
5. **URIs de redirection autorisés** :
   - `http://localhost:5001/auth/google/callback` (développement)
   - `https://votre-domaine.com/auth/google/callback` (production)
6. Cliquez sur **"Créer"**

### 5. Récupérer les clés

Après création, vous obtenez :
- **ID client** : `xxxxxx.apps.googleusercontent.com`
- **Secret client** : `xxxxxx`

## 🔧 Configuration de l'application

### 1. Variables d'environnement

Ajoutez ces variables à votre fichier `.env` :

```bash
# Configuration Google OAuth
GOOGLE_CLIENT_ID=votre-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=votre-client-secret
```

### 2. Redémarrer l'application

```bash
python app.py
```

### 3. Tester l'intégration

1. Connectez-vous à votre compte MondeRH
2. Allez sur le **Tableau de bord**
3. Cliquez sur **"Connecter Google"** dans la section Google Workspace
4. Autorisez l'accès à Google Drive et Calendar
5. Testez en :
   - Déposant une candidature avec un CV (→ sauvegarde sur Drive)
   - Prenant un rendez-vous (→ ajout au Calendar)

## 🔒 Sécurité

- Les tokens Google sont stockés de manière sécurisée en base de données
- Les tokens sont automatiquement rafraîchis si nécessaire
- Les utilisateurs peuvent déconnecter leur compte Google à tout moment

## 📁 Structure des fichiers Google Drive

Les CV sont automatiquement organisés dans :
```
Google Drive/
└── MondeRH_CV/
    ├── 20250101_120000_cv_candidat1.pdf
    ├── 20250101_130000_cv_candidat2.docx
    └── ...
```

## 📅 Événements Google Calendar

Les rendez-vous créent automatiquement :
- **Titre** : "RDV [Type de service] - MondeRH"
- **Description** : Détails du client et du rendez-vous
- **Participants** : Email du client
- **Rappels** : 24h par email, 30min par popup

## 🔧 Dépannage

### Erreur "Configuration Google OAuth manquante"
- Vérifiez que `GOOGLE_CLIENT_ID` et `GOOGLE_CLIENT_SECRET` sont définis
- Redémarrez l'application après modification du `.env`

### Erreur "redirect_uri_mismatch"
- Vérifiez que l'URI de redirection est correctement configurée dans Google Cloud Console
- Format exact : `http://localhost:5001/auth/google/callback`

### Erreur "access_denied"
- L'utilisateur a refusé l'autorisation
- Demandez à l'utilisateur de réessayer la connexion

## 📞 Support

Pour toute question sur la configuration Google, contactez l'équipe technique. 