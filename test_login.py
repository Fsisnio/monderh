#!/usr/bin/env python3
"""
Script de test pour déboguer la connexion admin
"""

from app import app, db, User, LoginForm
from werkzeug.security import check_password_hash

def test_admin_login():
    with app.app_context():
        print("=== Test de connexion admin ===")
        
        # Données de test
        test_email = "admin@monderh.fr"
        test_password = "admin123"
        
        print(f"Email testé: '{test_email}'")
        print(f"Mot de passe testé: '{test_password}'")
        
        # Recherche de l'utilisateur
        user = User.query.filter_by(email=test_email).first()
        
        if user:
            print(f"✅ Utilisateur trouvé: {user.email}")
            print(f"Type d'utilisateur: {user.user_type}")
            print(f"Actif: {user.is_active}")
            
            # Test du mot de passe
            password_check = check_password_hash(user.password_hash, test_password)
            print(f"✅ Vérification mot de passe: {password_check}")
            
            if password_check:
                print("🎉 Connexion devrait fonctionner!")
            else:
                print("❌ Mot de passe incorrect")
                
        else:
            print("❌ Utilisateur non trouvé")
            
            # Lister tous les utilisateurs
            print("\nTous les utilisateurs:")
            for u in User.query.all():
                print(f"  - ID: {u.id}, Email: '{u.email}', Type: {u.user_type}")

if __name__ == '__main__':
    test_admin_login() 