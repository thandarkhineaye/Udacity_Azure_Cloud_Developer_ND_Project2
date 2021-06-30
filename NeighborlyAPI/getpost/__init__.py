import azure.functions as func
import logging
import json
import os
import pymongo
from bson.json_util import dumps
from bson.objectid import ObjectId

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = os.environ['azure_microservice_pj_db_connection']  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['azure_microservice_mongo_db']
            collection = database['posts']
            query = {"_id": ObjectId(id)}
            result_query = collection.find_one(query)
            result = dumps(result_query)
            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except Exception as e:
            logging.error(e)   
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)