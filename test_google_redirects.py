#!/usr/bin/env python3
"""
Script de test pour les redirections Google Workspace
"""

import requests

def test_google_redirects():
    """Test des redirections Google Workspace"""
    print("🧪 Test des redirections Google Workspace...")
    print("=" * 50)
    
    # URLs à tester
    redirects = [
        ('Google Drive', '/google/drive'),
        ('Google Calendar', '/google/calendar'),
        ('Google Forms', '/google/forms'),
        ('Google Sheets', '/google/sheets')
    ]
    
    for name, url in redirects:
        try:
            print(f"\n🔗 Test de {name}...")
            response = requests.get(f'http://127.0.0.1:5000{url}', allow_redirects=False, timeout=5)
            
            if response.status_code == 302:
                location = response.headers.get('Location', 'Non trouvée')
                print(f"✅ {name} - Redirection vers : {location}")
            else:
                print(f"⚠️  {name} - Code de réponse : {response.status_code}")
                
        except Exception as e:
            print(f"❌ {name} - Erreur : {e}")
    
    print("\n" + "=" * 50)
    print("📋 Instructions pour tester :")
    print("1. Allez sur http://127.0.0.1:5000")
    print("2. Connectez-vous à votre compte")
    print("3. Allez sur le dashboard")
    print("4. Vérifiez que les boutons Google Workspace apparaissent")
    print("5. Cliquez sur les boutons pour tester les redirections")

if __name__ == '__main__':
    test_google_redirects() 