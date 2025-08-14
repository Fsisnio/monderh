# 🔧 Guide de Configuration Google OAuth - MonDRH

## 📋 Prérequis

Pour utiliser l'intégration Google Workspace (Drive et Calendar), vous devez configurer un projet Google Cloud et obtenir les clés OAuth.

## 🚀 Étapes de configuration

### 1. Créer un projet Google Cloud

1. Allez sur [Google Cloud Console](https://console.cloud.google.com/)
2. Cliquez sur "Sélectionner un projet" → "Nouveau projet"
3. Nommez votre projet (ex: "MonDRH-Integration")
4. Cliquez sur "Créer"

### 2. Activer les APIs nécessaires

1. Dans le menu, allez à "APIs et services" → "Bibliothèque"
2. Recherchez et activez :
   - **Google Drive API**
   - **Google Calendar API**

### 3. Configurer l'écran de consentement OAuth

1. Allez à "APIs et services" → "Écran de consentement OAuth"
2. Sélectionnez "Externe" et cliquez sur "Créer"
3. Remplissez les informations :
   - **Nom de l'application** : MonDRH
   - **Email de support** : votre email
   - **Logo** : (optionnel)
   - **Domaine de l'application** : localhost (pour le développement)
4. Cliquez sur "Enregistrer et continuer"
5. Dans "Scopes", ajoutez :
   - `https://www.googleapis.com/auth/drive.file`
   - `https://www.googleapis.com/auth/calendar`
6. Cliquez sur "Enregistrer et continuer"
7. Ajoutez votre email comme utilisateur de test
8. Cliquez sur "Enregistrer et continuer"

### 4. Créer les identifiants OAuth

1. Allez à "APIs et services" → "Identifiants"
2. Cliquez sur "Créer des identifiants" → "ID client OAuth 2.0"
3. Sélectionnez "Application Web"
4. Nommez-la (ex: "MonDRH Web Client")
5. Dans "URIs de redirection autorisés", ajoutez :
   - `http://localhost:5001/auth/google/callback`
   - `http://127.0.0.1:5001/auth/google/callback`
6. Cliquez sur "Créer"
7. **Notez le CLIENT_ID et CLIENT_SECRET**

### 5. Configurer les variables d'environnement

Créez un fichier `.env` à la racine du projet :

```env
# Configuration Google OAuth
GOOGLE_CLIENT_ID=votre-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=votre-client-secret

# Configuration Email (optionnel)
MAIL_USERNAME=contact@monderh.fr
MAIL_PASSWORD=votre-mot-de-passe-email

# Clé secrète Flask
SECRET_KEY=votre-cle-secrete-change-en-production
```

### 6. Installer les dépendances

```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib google-auth
```

## 🔍 Test de l'intégration

1. Redémarrez l'application Flask
2. Connectez-vous à votre compte
3. Allez sur le dashboard
4. Cliquez sur "Connecter Google" dans la section Google Workspace
5. Autorisez l'application dans Google
6. Vérifiez que la connexion est établie

## 🛠️ Dépannage

### Erreur "Configuration Google OAuth manquante"
- Vérifiez que le fichier `.env` existe
- Vérifiez que `GOOGLE_CLIENT_ID` et `GOOGLE_CLIENT_SECRET` sont définis
- Redémarrez l'application

### Erreur "redirect_uri_mismatch"
- Vérifiez que les URIs de redirection dans Google Cloud Console correspondent exactement
- Incluez `http://localhost:5001/auth/google/callback` et `http://127.0.0.1:5001/auth/google/callback`

### Erreur "access_denied"
- Vérifiez que votre email est ajouté comme utilisateur de test
- Vérifiez que les scopes sont correctement configurés

### Erreur "invalid_client"
- Vérifiez que le CLIENT_ID et CLIENT_SECRET sont corrects
- Vérifiez que l'application OAuth est configurée pour "Application Web"

## 📱 Configuration pour la production

Pour la production, vous devrez :

1. **Changer les URIs de redirection** dans Google Cloud Console :
   - `https://votre-domaine.com/auth/google/callback`

2. **Publier l'application** dans l'écran de consentement OAuth

3. **Configurer les variables d'environnement** sur votre serveur

4. **Utiliser HTTPS** (obligatoire pour la production)

## 🔒 Sécurité

- **Ne jamais commiter** le fichier `.env` dans Git
- **Utiliser des clés secrètes fortes** en production
- **Limiter les scopes** aux minimums nécessaires
- **Surveiller les logs** d'utilisation

## 📞 Support

Si vous rencontrez des problèmes :

1. Vérifiez les logs de l'application Flask
2. Vérifiez les logs dans Google Cloud Console
3. Consultez la [documentation Google OAuth](https://developers.google.com/identity/protocols/oauth2)

---

*Dernière mise à jour : Août 2025* 