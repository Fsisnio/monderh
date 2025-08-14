#!/usr/bin/env python3
"""
Script pour tester la connexion à la base de données PostgreSQL
"""

import os
from app import app, db

def test_database_connection():
    with app.app_context():
        print("🔍 Test de connexion à la base de données...")
        
        # Afficher la configuration
        print(f"📋 Configuration de la base de données:")
        print(f"   URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
        
        # Tester la connexion
        try:
            # Essayer de se connecter
            db.engine.connect()
            print("✅ Connexion à la base de données réussie!")
            
            # Tester une requête simple
            result = db.engine.execute("SELECT version();")
            version = result.fetchone()[0]
            print(f"✅ Version PostgreSQL: {version}")
            
            # Vérifier les tables
            result = db.engine.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                ORDER BY table_name;
            """)
            tables = [row[0] for row in result.fetchall()]
            
            if tables:
                print(f"✅ Tables trouvées: {', '.join(tables)}")
            else:
                print("ℹ️  Aucune table trouvée (normal si c'est une nouvelle base)")
                
        except Exception as e:
            print(f"❌ Erreur de connexion: {e}")
            return False
        
        return True

if __name__ == '__main__':
    test_database_connection() 