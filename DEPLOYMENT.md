# 🚀 Guide de Déploiement MonDRH sur Render

## 📋 Prérequis

- Compte Render.com
- Repository GitHub avec le code MonDRH
- Variables d'environnement configurées

## 🔧 Configuration Render

### **1. Créer un nouveau Web Service**

1. Connectez-vous à [Render.com](https://render.com)
2. Cliquez sur "New +" → "Web Service"
3. Connectez votre repository GitHub
4. Sélectionnez le repository `mondera`

### **2. Configuration du Service**

- **Name**: `monderh`
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120`
- **Plan**: `Free` (pour commencer)

### **3. Variables d'Environnement**

Ajoutez ces variables dans les paramètres du service :

#### **Variables Requises**
```
SECRET_KEY=your-secret-key-here
MAIL_USERNAME=contact@monderh.fr
MAIL_PASSWORD=your-email-password
```

#### **Variables Optionnelles (Google OAuth)**
```
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
```

#### **Base de Données (Automatique)**
```
DATABASE_URL=postgresql://... (fourni par Render)
```

## 🗄️ Base de Données PostgreSQL

1. Créez un nouveau service PostgreSQL sur Render
2. Connectez-le à votre service web
3. La variable `DATABASE_URL` sera automatiquement configurée

## 🔄 Déploiement Automatique

- Le déploiement se fait automatiquement à chaque push sur la branche `main`
- Render détecte les changements et redéploie automatiquement

## 📊 Monitoring

- **Health Check**: `/` (page d'accueil)
- **Logs**: Disponibles dans l'interface Render
- **Métriques**: Temps de réponse, utilisation des ressources

## 🛠️ Commandes Utiles

### **Redémarrage Manuel**
```bash
# Dans l'interface Render
Settings → Manual Deploy → Deploy Latest Commit
```

### **Vérification des Logs**
```bash
# Dans l'interface Render
Logs → View Logs
```

## 🔍 Dépannage

### **Erreur de Base de Données**
- Vérifiez que PostgreSQL est connecté
- Vérifiez la variable `DATABASE_URL`

### **Erreur de Build**
- Vérifiez `requirements.txt`
- Vérifiez la version Python (3.9+)

### **Erreur de Démarrage**
- Vérifiez les variables d'environnement
- Vérifiez les logs pour plus de détails

## 🌐 URL de Production

Une fois déployé, votre application sera accessible sur :
```
https://monderh.onrender.com
```

## 📧 Configuration Email

Pour que les emails fonctionnent en production :

1. Configurez un service SMTP (Gmail, SendGrid, etc.)
2. Ajoutez les variables `MAIL_USERNAME` et `MAIL_PASSWORD`
3. Testez l'envoi d'emails

## 🔐 Sécurité

- `SECRET_KEY` doit être unique et sécurisé
- Variables sensibles marquées comme "Secret" dans Render
- HTTPS automatiquement activé

## 📈 Scaling

Pour passer en production :
1. Changez le plan vers "Starter" ou supérieur
2. Configurez un domaine personnalisé
3. Activez le monitoring avancé

## 🔐 Identifiants Administrateur

Après le déploiement, les administrateurs sont créés automatiquement :

```
Email: admin@monderh.fr
Mot de passe: admin123

Email: faladespero1@gmail.com
Mot de passe: admin123
```

## 📁 Fichiers de Configuration

- `render.yaml` - Configuration Render
- `requirements.txt` - Dépendances Python
- `runtime.txt` - Version Python
- `build.sh` - Script de build
- `app.py` - Application avec support PostgreSQL 