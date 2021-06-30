import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
import logging
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = os.environ['azure_microservice_pj_db_connection']  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url, ssl_cert_reqs=ssl.CERT_NONE)
        database = client['azure_microservice_mongo_db']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

