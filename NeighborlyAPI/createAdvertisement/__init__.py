import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
import logging
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = os.environ['azure_microservice_pj_db_connection']  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['azure_microservice_mongo_db']
            collection = database['advertisements']
            rec_id1 = collection.insert_one(request)
            return func.HttpResponse(req.get_body())
        except:
            print("could not connect to mongodb")
            return func.HttpResponse(Exception(),'Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )