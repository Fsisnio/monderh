#!/usr/bin/env python3
"""
Script de test pour l'intégration Google OAuth
"""

import os
import requests
from dotenv import load_dotenv

def test_google_integration():
    """Test de l'intégration Google OAuth"""
    print("🧪 Test de l'intégration Google OAuth...")
    print("=" * 50)
    
    # Charger les variables d'environnement
    load_dotenv()
    
    # Vérifier la configuration
    client_id = os.getenv('GOOGLE_CLIENT_ID')
    client_secret = os.getenv('GOOGLE_CLIENT_SECRET')
    
    if not client_id or not client_secret:
        print("❌ Configuration Google OAuth manquante")
        return False
    
    print(f"✅ Configuration trouvée")
    print(f"   CLIENT_ID: {client_id[:20]}...")
    print(f"   CLIENT_SECRET: {client_secret[:10]}...")
    
    # Test de l'application Flask
    try:
        print("\n🌐 Test de l'application Flask...")
        response = requests.get('http://127.0.0.1:5001/', timeout=5)
        if response.status_code == 200:
            print("✅ Application Flask accessible")
        else:
            print(f"⚠️  Application Flask répond avec le code {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("❌ Application Flask non accessible (démarrez l'application)")
        return False
    except Exception as e:
        print(f"❌ Erreur lors du test : {e}")
        return False
    
    # Test de la route Google OAuth
    try:
        print("\n🔗 Test de la route Google OAuth...")
        response = requests.get('http://127.0.0.1:5001/auth/google', timeout=5)
        if response.status_code == 302:
            print("✅ Route Google OAuth fonctionne (redirection attendue)")
            print(f"   URL de redirection : {response.headers.get('Location', 'Non trouvée')}")
        else:
            print(f"⚠️  Route Google OAuth répond avec le code {response.status_code}")
    except Exception as e:
        print(f"❌ Erreur lors du test de la route Google : {e}")
    
    print("\n" + "=" * 50)
    print("🎉 Configuration Google OAuth prête !")
    print("\n📋 Prochaines étapes :")
    print("1. Connectez-vous à votre compte")
    print("2. Allez sur le dashboard")
    print("3. Cliquez sur 'Connecter Google'")
    print("4. Autorisez l'application dans Google")
    print("5. Testez les fonctionnalités Google Drive et Calendar")
    
    return True

if __name__ == '__main__':
    test_google_integration() 