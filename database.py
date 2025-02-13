from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017/")

try:
    client.admin.command('ping')
    print("✅ Connected to MongoDB successfully!")
except Exception as e:
    print(f"❌ MongoDB connection failed: {e}")
