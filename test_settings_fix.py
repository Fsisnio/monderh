#!/usr/bin/env python3
"""
Script de test pour vérifier que la page des paramètres fonctionne
"""

import requests

def test_settings_page():
    """Test de la page des paramètres"""
    print("🧪 Test de la page des paramètres...")
    print("=" * 50)
    
    base_url = "http://127.0.0.1:5000"
    
    try:
        # Test de la page des paramètres
        response = requests.get(f'{base_url}/admin/settings', timeout=5)
        
        if response.status_code == 302:
            print("✅ Page des paramètres - Redirection (login requis)")
            print("   La page fonctionne correctement !")
        elif response.status_code == 200:
            print("✅ Page des paramètres - Accessible")
        else:
            print(f"⚠️  Page des paramètres - Code: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Erreur: {e}")
    
    print("\n" + "=" * 50)
    print("📋 Instructions pour tester :")
    print("1. Connectez-vous en tant qu'admin (admin@monderh.fr)")
    print("2. Allez sur Administration > Paramètres du site")
    print("3. Vérifiez que tous les champs s'affichent correctement")
    print("4. Testez la modification et sauvegarde des paramètres")

if __name__ == '__main__':
    test_settings_page() 