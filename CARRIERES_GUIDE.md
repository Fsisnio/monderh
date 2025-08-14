# 🚀 Guide d'Utilisation - Système de Gestion des Offres d'Emploi

## 📋 Vue d'ensemble

Le système de gestion des offres d'emploi de MonDRH permet aux administrateurs de créer, modifier et gérer les offres d'emploi, et aux visiteurs de consulter et postuler aux offres disponibles.

## 🏗️ Architecture

### Modèles de données

#### JobOffer (Offre d'emploi)
- **id** : Identifiant unique
- **title** : Titre du poste
- **company** : Nom de l'entreprise
- **location** : Localisation
- **contract_type** : Type de contrat (CDI, CDD, Stage, etc.)
- **experience_level** : Niveau d'expérience (Junior, Confirmé, Senior, Expert)
- **salary_range** : Fourchette salariale
- **description** : Description du poste
- **requirements** : Profil recherché
- **benefits** : Avantages et bénéfices
- **department** : Département
- **is_active** : Statut actif/inactif
- **created_at** : Date de création
- **updated_at** : Date de modification

#### JobApplication (Candidature)
- **id** : Identifiant unique
- **job_offer_id** : Référence vers l'offre
- **user_id** : Référence vers l'utilisateur
- **cv_filename** : Nom du fichier CV
- **cover_letter** : Lettre de motivation
- **status** : Statut (pending, reviewed, accepted, rejected)
- **created_at** : Date de candidature
- **notes** : Notes internes

## 🔧 Installation et Configuration

### 1. Migration de la base de données

```bash
python migrate_jobs.py
```

Ce script :
- Crée les tables `job_offer` et `job_application`
- Ajoute des offres d'exemple
- Vérifie le bon fonctionnement

### 2. Vérification

Après la migration, vous devriez avoir :
- 3 offres d'emploi d'exemple dans la base
- Accès à `/admin/jobs` pour la gestion
- Accès à `/careers` pour la consultation publique

## 👨‍💼 Interface d'Administration

### Accès
- URL : `/admin/jobs`
- Authentification admin requise
- Accessible via la sidebar admin

### Fonctionnalités

#### 📊 Tableau de bord
- **Statistiques** : Total offres, offres actives/inactives, candidatures
- **Vue d'ensemble** : Liste paginée des offres
- **Actions rapides** : Voir, modifier, activer/désactiver, supprimer

#### ➕ Créer une nouvelle offre
1. Cliquer sur "Nouvelle Offre"
2. Remplir le formulaire :
   - **Informations générales** : Titre, entreprise, localisation, département
   - **Détails du contrat** : Type, niveau d'expérience, salaire
   - **Description du poste** : Missions et responsabilités
   - **Profil recherché** : Compétences et qualités requises
   - **Avantages** : Bénéfices de l'entreprise (optionnel)
3. Activer/désactiver l'offre
4. Publier

#### ✏️ Modifier une offre
1. Cliquer sur l'icône "Modifier" (crayon)
2. Modifier les champs souhaités
3. Sauvegarder les modifications
4. L'aperçu se met à jour automatiquement

#### 🎛️ Gérer le statut
- **Activer** : Rendre l'offre visible publiquement
- **Désactiver** : Masquer l'offre (non supprimée)
- **Supprimer** : Suppression définitive

### Validation des données

Le formulaire inclut des validations :
- **Titre** : 5-200 caractères
- **Description** : Minimum 50 caractères
- **Profil recherché** : Minimum 30 caractères
- **Champs obligatoires** : Titre, entreprise, localisation, type de contrat, niveau d'expérience

## 🌐 Interface Publique

### Page Carrières (`/careers`)

#### Fonctionnalités
- **Hero section** : Présentation avec statistiques
- **Filtres de recherche** :
  - Recherche textuelle (titre, entreprise, localisation)
  - Type de contrat
  - Niveau d'expérience
- **Liste des offres** : Cartes avec informations clés
- **Pagination** : Navigation entre les pages
- **CTA** : Candidature spontanée et prise de rendez-vous

#### Design
- **Responsive** : Adaptation mobile/tablet/desktop
- **Animations** : Effets visuels au scroll
- **Cartes interactives** : Hover effects et transitions

### Détail d'une offre (`/careers/<id>`)

#### Sections
1. **Hero** : Titre, entreprise, informations clés
2. **Description** : Missions et responsabilités
3. **Profil recherché** : Compétences requises
4. **Avantages** : Bénéfices de l'entreprise
5. **Sidebar** : Informations clés, offres similaires
6. **Formulaire de candidature** : Postulation directe

#### Fonctionnalités
- **Navigation fluide** : Liens vers les sections
- **Offres similaires** : Suggestions automatiques
- **Formulaire intégré** : Candidature directe
- **Design moderne** : Animations et interactions

## 📝 Gestion des Candidatures

### Processus de candidature
1. **Visiteur** : Consulte l'offre sur `/careers/<id>`
2. **Formulaire** : Remplit les informations et upload le CV
3. **Soumission** : Envoi vers le système de candidatures existant
4. **Notification** : Email automatique à l'administrateur
5. **Suivi** : Gestion via `/admin/applications`

### Intégration
- Utilise le système de candidatures existant
- Lien automatique avec l'offre d'emploi
- Statuts et notes personnalisables

## 🔍 Fonctionnalités Avancées

### Recherche et Filtrage
- **Recherche textuelle** : Titre, entreprise, localisation, description
- **Filtres** : Type de contrat, niveau d'expérience
- **Pagination** : 12 offres par page
- **URLs propres** : Paramètres dans l'URL

### SEO et Performance
- **URLs optimisées** : `/careers/<id>` pour chaque offre
- **Meta tags** : Titre et description dynamiques
- **Performance** : Requêtes optimisées avec filtres
- **Responsive** : Design adaptatif

### Sécurité
- **Authentification** : Accès admin requis
- **Validation** : Données validées côté serveur
- **CSRF protection** : Protection contre les attaques
- **Upload sécurisé** : Validation des fichiers CV

## 📊 Statistiques et Analytics

### Métriques disponibles
- **Total offres** : Nombre total d'offres créées
- **Offres actives** : Offres visibles publiquement
- **Offres inactives** : Offres masquées
- **Candidatures** : Nombre total de candidatures
- **Candidatures par offre** : Statistiques détaillées

### Tableau de bord admin
- **Vue d'ensemble** : Statistiques en temps réel
- **Graphiques** : Évolution des candidatures
- **Filtres** : Par période, type de contrat, etc.

## 🛠️ Maintenance

### Sauvegarde
- **Base de données** : Sauvegarde régulière des tables
- **Fichiers** : Sauvegarde des CV uploadés
- **Configuration** : Sauvegarde des paramètres

### Monitoring
- **Logs** : Suivi des actions admin
- **Erreurs** : Gestion des exceptions
- **Performance** : Monitoring des requêtes

### Mises à jour
- **Sécurité** : Mises à jour régulières
- **Fonctionnalités** : Ajout de nouvelles options
- **Compatibilité** : Tests sur différents navigateurs

## 🎯 Bonnes Pratiques

### Création d'offres
1. **Titre clair** : Description précise du poste
2. **Description détaillée** : Missions et responsabilités
3. **Profil précis** : Compétences et expérience requises
4. **Avantages attractifs** : Mise en avant des bénéfices
5. **Informations complètes** : Salaire, localisation, type de contrat

### Gestion des candidatures
1. **Réponse rapide** : Traitement sous 24-48h
2. **Communication claire** : Statuts et feedback
3. **Confidentialité** : Protection des données
4. **Suivi** : Notes et commentaires internes

### Maintenance
1. **Nettoyage régulier** : Suppression des offres obsolètes
2. **Mise à jour** : Actualisation des informations
3. **Monitoring** : Surveillance des performances
4. **Sauvegarde** : Protection des données

## 🚀 Évolutions Futures

### Fonctionnalités prévues
- **Notifications push** : Alertes nouvelles offres
- **Candidature en ligne** : Formulaire intégré
- **Matching automatique** : Suggestions de candidats
- **Analytics avancés** : Statistiques détaillées
- **API REST** : Intégration externe
- **Multi-langues** : Support international

### Améliorations techniques
- **Cache** : Optimisation des performances
- **CDN** : Distribution de contenu
- **Mobile app** : Application native
- **IA** : Matching intelligent
- **Blockchain** : Certifications vérifiées

---

## 📞 Support

Pour toute question ou problème :
- **Email** : admin@mondrh.com
- **Documentation** : Ce guide
- **Code source** : Repository GitHub
- **Issues** : Système de tickets

---

*Dernière mise à jour : Août 2025*
*Version : 1.0* 