#!/usr/bin/env python3
"""
Script de test pour les fonctionnalités d'administration des utilisateurs
"""

import requests
import json

def test_admin_features():
    """Test des fonctionnalités d'administration"""
    print("🧪 Test des fonctionnalités d'administration...")
    print("=" * 50)
    
    base_url = "http://127.0.0.1:5000"
    
    # URLs à tester
    admin_urls = [
        ('Page Utilisateurs', '/admin/users'),
        ('Page Applications', '/admin/applications'),
        ('Page Rendez-vous', '/admin/appointments'),
        ('Page Paramètres', '/admin/settings'),
    ]
    
    print("\n📋 Test des pages d'administration :")
    for name, url in admin_urls:
        try:
            response = requests.get(f'{base_url}{url}', timeout=5)
            if response.status_code == 302:
                print(f"✅ {name} - Redirection (login requis)")
            elif response.status_code == 200:
                print(f"✅ {name} - Accessible")
            else:
                print(f"⚠️  {name} - Code: {response.status_code}")
        except Exception as e:
            print(f"❌ {name} - Erreur: {e}")
    
    print("\n" + "=" * 50)
    print("📋 Instructions pour tester :")
    print("1. Connectez-vous en tant qu'admin (admin@monderh.fr)")
    print("2. Allez sur Administration > Utilisateurs")
    print("3. Cliquez sur l'icône 'Modifier' (crayon) pour un utilisateur")
    print("4. Modifiez les informations et sauvegardez")
    print("5. Testez la suppression d'un utilisateur (icône poubelle)")
    print("6. Vérifiez que les modifications sont bien enregistrées")

if __name__ == '__main__':
    test_admin_features() 