#!/usr/bin/env python3
"""
Script de test pour la configuration OAuth Google
"""

from app import app, get_google_callback_url

def test_google_oauth_config():
    """Test de la configuration OAuth Google"""
    print("🧪 Test de la configuration OAuth Google...")
    print("=" * 50)
    
    with app.app_context():
        # Vérifier la configuration
        client_id = app.config.get('GOOGLE_CLIENT_ID')
        client_secret = app.config.get('GOOGLE_CLIENT_SECRET')
        
        print(f"🔑 Configuration :")
        print(f"   CLIENT_ID : {'✅ Configuré' if client_id else '❌ Manquant'}")
        print(f"   CLIENT_SECRET : {'✅ Configuré' if client_secret else '❌ Manquant'}")
        
        if client_id and client_secret:
            print(f"\n✅ Configuration complète !")
            print(f"📋 URLs à ajouter dans Google Cloud Console :")
            print(f"   http://localhost:5001/auth/google/callback")
            print(f"   http://127.0.0.1:5001/auth/google/callback")
            print(f"   http://localhost:5000/auth/google/callback")
            print(f"   http://127.0.0.1:5000/auth/google/callback")
        else:
            print(f"\n❌ Configuration incomplète !")
            print(f"Vérifiez votre fichier .env")

if __name__ == '__main__':
    test_google_oauth_config() 