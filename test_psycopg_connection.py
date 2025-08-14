#!/usr/bin/env python3
"""
Test script to verify psycopg connection works with the updated requirements.
"""

import os
from dotenv import load_dotenv
import psycopg

# Load environment variables
load_dotenv()

def test_psycopg_connection():
    """Test psycopg connection to PostgreSQL database."""
    try:
        # Get database URL from environment
        database_url = os.environ.get('DATABASE_URL')
        
        if not database_url:
            print("❌ DATABASE_URL environment variable not found")
            return False
            
        # Fix postgres:// to postgresql:// for newer versions
        if database_url.startswith('postgres://'):
            database_url = database_url.replace('postgres://', 'postgresql://', 1)
            
        print(f"🔗 Testing connection to: {database_url.split('@')[1] if '@' in database_url else 'local database'}")
        
        # Test connection
        with psycopg.connect(database_url) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT version();")
                version = cur.fetchone()
                print(f"✅ Successfully connected to PostgreSQL: {version[0]}")
                return True
                
    except Exception as e:
        print(f"❌ Connection failed: {str(e)}")
        return False

if __name__ == "__main__":
    print("🧪 Testing psycopg connection...")
    success = test_psycopg_connection()
    
    if success:
        print("🎉 psycopg connection test passed!")
    else:
        print("💥 psycopg connection test failed!")
        exit(1) 