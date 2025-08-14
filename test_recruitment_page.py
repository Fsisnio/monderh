#!/usr/bin/env python3
"""
Script de test pour la page de recrutement améliorée
"""

import requests
from bs4 import BeautifulSoup

def test_recruitment_page():
    """Test de la page de recrutement améliorée"""
    print("🧪 Test de la page de recrutement améliorée...")
    print("=" * 60)
    
    base_url = "http://127.0.0.1:5000"
    
    try:
        # Test de la page de recrutement
        response = requests.get(f'{base_url}/service/recrutement', timeout=10)
        
        if response.status_code == 200:
            print("✅ Page de recrutement - Accessible")
            
            # Analyser le contenu
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Vérifier les éléments clés
            elements_to_check = [
                ('Titre principal', 'h1', 'Recrutement de Talents'),
                ('Section avantages', 'h2', 'Pourquoi Choisir MonDRH'),
                ('Section services', 'h2', 'Nos Services de Recrutement'),
                ('Section processus', 'h2', 'Notre Processus de Recrutement'),
                ('Section témoignages', 'h2', 'Ce que disent nos clients'),
                ('Formulaire de contact', 'form', None),
                ('Bouton démarrer', 'a', 'Démarrer un recrutement'),
            ]
            
            print("\n📋 Vérification du contenu :")
            for name, tag, expected_text in elements_to_check:
                if expected_text:
                    element = soup.find(tag, string=lambda text: text and expected_text in text)
                    if element:
                        print(f"✅ {name} - Trouvé")
                    else:
                        print(f"⚠️  {name} - Non trouvé")
                else:
                    element = soup.find(tag)
                    if element:
                        print(f"✅ {name} - Trouvé")
                    else:
                        print(f"⚠️  {name} - Non trouvé")
            
            # Vérifier les animations CSS
            css_content = soup.find_all('style')
            if css_content:
                print("✅ Animations CSS - Présentes")
            else:
                print("⚠️  Animations CSS - Non trouvées")
            
            # Vérifier le JavaScript
            js_content = soup.find_all('script')
            if js_content:
                print("✅ JavaScript - Présent")
            else:
                print("⚠️  JavaScript - Non trouvé")
                
        else:
            print(f"❌ Page de recrutement - Erreur {response.status_code}")
            
    except Exception as e:
        print(f"❌ Erreur: {e}")
    
    print("\n" + "=" * 60)
    print("📋 Instructions pour tester :")
    print("1. Allez sur http://127.0.0.1:5000/service/recrutement")
    print("2. Vérifiez les animations au scroll")
    print("3. Testez le formulaire de contact")
    print("4. Vérifiez la responsivité sur mobile")
    print("5. Testez les liens et boutons")

if __name__ == '__main__':
    test_recruitment_page() 