#!/usr/bin/env python3
"""
Script pour configurer la base de données PostgreSQL en production
"""

import os
from app import app, db, User
from werkzeug.security import generate_password_hash

def setup_production_database():
    with app.app_context():
        print("🚀 Configuration de la base de données PostgreSQL...")
        
        # Vérifier la connexion à la base de données
        try:
            # Créer les tables
            db.create_all()
            print("✅ Tables créées avec succès!")
        except Exception as e:
            print(f"❌ Erreur lors de la création des tables: {e}")
            return
        
        # Créer l'administrateur principal
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
            print("✅ Administrateur principal créé: admin@monderh.fr")
        else:
            admin1.password_hash = generate_password_hash('admin123')
            admin1.user_type = 'admin'
            admin1.is_active = True
            print("✅ Administrateur principal mis à jour: admin@monderh.fr")
        
        # Créer le deuxième administrateur
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
            print("✅ Deuxième administrateur créé: faladespero1@gmail.com")
        else:
            admin2.password_hash = generate_password_hash('admin123')
            admin2.user_type = 'admin'
            admin2.is_active = True
            print("✅ Deuxième administrateur mis à jour: faladespero1@gmail.com")
        
        # Sauvegarder les changements
        try:
            db.session.commit()
            print("\n✅ Base de données configurée avec succès!")
        except Exception as e:
            print(f"\n❌ Erreur lors de la sauvegarde: {e}")
            db.session.rollback()
            return
        
        # Afficher les informations de connexion
        print("\n🔐 Identifiants administrateur:")
        print("   Email: admin@monderh.fr")
        print("   Mot de passe: admin123")
        print("   ---")
        print("   Email: faladespero1@gmail.com")
        print("   Mot de passe: admin123")
        
        # Vérifier la configuration de la base de données
        print(f"\n🗄️ Configuration de la base de données:")
        print(f"   URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
        
        # Compter les utilisateurs
        total_users = User.query.count()
        admin_users = User.query.filter_by(user_type='admin').count()
        print(f"\n📊 Statistiques:")
        print(f"   Total utilisateurs: {total_users}")
        print(f"   Administrateurs: {admin_users}")

if __name__ == '__main__':
    setup_production_database() 