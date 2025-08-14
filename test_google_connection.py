#!/usr/bin/env python3
"""
Script de test pour la connexion Google Workspace
"""

import requests
import json
from app import app, db, GoogleToken, User

def test_google_connection():
    """Test de la connexion Google Workspace"""
    print("🧪 Test de la connexion Google Workspace...")
    print("=" * 50)
    
    # Test de l'API de statut Google
    try:
        print("\n1. Test de l'API de statut Google...")
        response = requests.get('http://127.0.0.1:5001/api/google/status', timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API accessible - Statut: {data.get('connected', 'N/A')}")
            print(f"   Message: {data.get('message', 'N/A')}")
        else:
            print(f"⚠️  API répond avec le code {response.status_code}")
    except Exception as e:
        print(f"❌ Erreur API: {e}")
    
    # Test de la base de données
    try:
        print("\n2. Test de la base de données...")
        with app.app_context():
            tokens = GoogleToken.query.all()
            users = User.query.all()
            print(f"✅ Base accessible - Tokens: {len(tokens)}, Users: {len(users)}")
            
            if tokens:
                for token in tokens:
                    print(f"   Token pour user {token.user_id}, expiré: {token.expiry}")
    except Exception as e:
        print(f"❌ Erreur base de données: {e}")
    
    # Test de la route Google OAuth
    try:
        print("\n3. Test de la route Google OAuth...")
        response = requests.get('http://127.0.0.1:5001/auth/google', timeout=5)
        if response.status_code == 302:
            print("✅ Route Google OAuth fonctionne (redirection attendue)")
            print(f"   URL de redirection: {response.headers.get('Location', 'Non trouvée')}")
        else:
            print(f"⚠️  Route Google OAuth répond avec le code {response.status_code}")
    except Exception as e:
        print(f"❌ Erreur route Google: {e}")
    
    print("\n" + "=" * 50)
    print("📋 Instructions pour tester :")
    print("1. Connectez-vous à votre compte")
    print("2. Allez sur le dashboard")
    print("3. Cliquez sur 'Connecter Google'")
    print("4. Autorisez l'application dans Google")
    print("5. Vérifiez que le statut change à 'Connecté'")

if __name__ == '__main__':
    test_google_connection() 