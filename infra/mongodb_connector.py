from pymongo import MongoClient
import os

# Gets environment variables defined in compose.yaml
# Creates a connection and return database
def get_database():
    CONNECTION_STRING = os.environ.get("MONGO_URI")
    client = MongoClient(CONNECTION_STRING)
    return client["jobs_db"]