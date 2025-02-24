import pymongo
import pandas as pd
import json
from pymongo import MongoClient

from sensor.config import mongo_client
mongo_client = MongoClient("mongodb+srv://mdsameer:Mumbai123@cluster0.50hiier.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATA_FILE_PATH="aps-failure-trainingset.csv"
DATABASE_NAME="aps"
COLLECTION_NAME="sensor"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    #Convert dataframe to json so that we can dump these record in mongo db
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    #insert converted json record to mongo db
    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)