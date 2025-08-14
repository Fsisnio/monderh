#!/usr/bin/env python3
"""
Script de migration pour ajouter les tables JobOffer et JobApplication
"""

import os
import sys
from datetime import datetime

# Ajouter le répertoire parent au path pour importer app
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, JobOffer, JobApplication

def create_jobs_tables():
    """Crée les tables pour les offres d'emploi"""
    with app.app_context():
        print("🔧 Création des tables pour les offres d'emploi...")
        
        # Créer les tables
        db.create_all()
        
        print("✅ Tables créées avec succès !")
        
        # Vérifier si les tables existent
        try:
            # Test d'insertion d'une offre d'exemple
            test_job = JobOffer(
                title="Développeur Full Stack",
                company="MonDRH",
                location="Dakar, Sénégal",
                contract_type="CDI",
                experience_level="Confirmé",
                salary_range="40000-60000€",
                description="Nous recherchons un développeur Full Stack passionné pour rejoindre notre équipe et participer au développement de nos solutions RH innovantes.",
                requirements="• 3-5 ans d'expérience en développement web\n• Maîtrise de Python, JavaScript, React\n• Connaissance de Flask/Django\n• Expérience avec les bases de données SQL\n• Capacité à travailler en équipe",
                benefits="• Environnement de travail moderne\n• Formation continue\n• Évolution de carrière\n• Avantages sociaux complets",
                department="Développement",
                is_active=True
            )
            
            db.session.add(test_job)
            db.session.commit()
            
            print("✅ Offre d'exemple créée avec succès !")
            print(f"   - ID: {test_job.id}")
            print(f"   - Titre: {test_job.title}")
            print(f"   - Entreprise: {test_job.company}")
            
            # Supprimer l'offre de test
            db.session.delete(test_job)
            db.session.commit()
            print("✅ Offre de test supprimée")
            
        except Exception as e:
            print(f"❌ Erreur lors du test: {e}")
            db.session.rollback()
            return False
        
        print("\n🎉 Migration terminée avec succès !")
        print("📋 Tables disponibles:")
        print("   - job_offer (offres d'emploi)")
        print("   - job_application (candidatures aux offres)")
        
        return True

def add_sample_jobs():
    """Ajoute quelques offres d'emploi d'exemple"""
    with app.app_context():
        print("\n📝 Ajout d'offres d'emploi d'exemple...")
        
        sample_jobs = [
            {
                "title": "Responsable RH",
                "company": "MonDRH",
                "location": "Dakar, Sénégal",
                "contract_type": "CDI",
                "experience_level": "Senior",
                "salary_range": "50000-70000€",
                "description": "Nous recherchons un Responsable RH expérimenté pour piloter notre département Ressources Humaines et contribuer à la croissance de notre entreprise.",
                "requirements": "• 5+ ans d'expérience en RH\n• Formation en Gestion des RH\n• Connaissance du droit social\n• Capacités managériales\n• Maîtrise des outils RH",
                "benefits": "• Poste à responsabilités\n• Équipe dynamique\n• Formation continue\n• Avantages sociaux",
                "department": "Ressources Humaines",
                "is_active": True
            },
            {
                "title": "Consultant en Formation",
                "company": "MonDRH",
                "location": "Dakar, Sénégal",
                "contract_type": "CDD",
                "experience_level": "Confirmé",
                "salary_range": "35000-50000€",
                "description": "Rejoignez notre équipe de consultants en formation pour accompagner nos clients dans le développement des compétences de leurs équipes.",
                "requirements": "• 3+ ans d'expérience en formation\n• Certifications en formation\n• Capacités pédagogiques\n• Mobilité géographique",
                "benefits": "• Missions variées\n• Développement professionnel\n• Travail en équipe\n• Horaires flexibles",
                "department": "Formation",
                "is_active": True
            },
            {
                "title": "Stagiaire Marketing Digital",
                "company": "MonDRH",
                "location": "Dakar, Sénégal",
                "contract_type": "Stage",
                "experience_level": "Junior",
                "salary_range": "Indemnités de stage",
                "description": "Stage de 6 mois en marketing digital pour soutenir nos activités de communication et de promotion de nos services RH.",
                "requirements": "• Formation en Marketing/Communication\n• Connaissance des réseaux sociaux\n• Créativité et autonomie\n• Maîtrise des outils digitaux",
                "benefits": "• Stage rémunéré\n• Encadrement personnalisé\n• Possibilité d'embauche\n• Expérience professionnelle",
                "department": "Marketing",
                "is_active": True
            }
        ]
        
        for job_data in sample_jobs:
            job = JobOffer(**job_data)
            db.session.add(job)
        
        try:
            db.session.commit()
            print(f"✅ {len(sample_jobs)} offres d'emploi d'exemple ajoutées !")
        except Exception as e:
            print(f"❌ Erreur lors de l'ajout des offres: {e}")
            db.session.rollback()
            return False
        
        return True

if __name__ == "__main__":
    print("🚀 Migration des offres d'emploi - MonDRH")
    print("=" * 50)
    
    # Créer les tables
    if create_jobs_tables():
        # Ajouter des offres d'exemple
        add_sample_jobs()
        
        print("\n🎯 Migration terminée !")
        print("📱 Vous pouvez maintenant :")
        print("   1. Accéder à l'admin pour gérer les offres")
        print("   2. Visiter /careers pour voir les offres publiques")
        print("   3. Créer de nouvelles offres via l'interface admin")
    else:
        print("\n❌ Migration échouée !")
        sys.exit(1) 