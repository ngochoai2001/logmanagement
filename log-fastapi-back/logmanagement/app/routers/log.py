from fastapi import APIRouter, HTTPException, Depends
from core.config import logs_db
from schema.log import log_serializer, logs_serializer
from model.log import Log
from .jwt_bear import JWTBearer
from bson.objectid import ObjectId

logRouter = APIRouter()

@logRouter.get("/logs/", tags=["logs"],dependencies=[Depends(JWTBearer())])
async def retrieve_all_logs():
    return{
        "status": "Get all successfully",
        "data": logs_serializer(
        logs_db.find()
        )
    }

@logRouter.get("/logs/{logId}", tags=["logs"],dependencies=[Depends(JWTBearer())])
async def retrieve_a_log(logId):
    print(logs_db.find_one({"_id":ObjectId(logId)}))
    return{
        "status": "Get log successfully",
        "data": log_serializer(
        logs_db.find_one({"_id":ObjectId(logId)})
        )
    }

@logRouter.post("/logs/", tags=["logs"], status_code=201,dependencies=[Depends(JWTBearer())])
async def insert_new_log(log: Log):
    new_log = logs_db.insert_one(dict(log))
    return {
        "status": "Add successfully",
        "data": log_serializer(
            logs_db.find_one({"_id": new_log.inserted_id})
        )
    }

@logRouter.put("/logs/{logId}/", tags = ["logs"],dependencies=[Depends(JWTBearer())])
async def update_a_log(logID, log:Log):
    log = logs_db.find_one({"_id": ObjectId(logID)})
    if(log):
        logs_db.update_one({"_id": logID},{'$set': log_serializer(log)})
    else:
        raise HTTPException(status_code=404, detail="Log not found")

@logRouter.delete("/logs/{logId}/", tags = ["logs"],dependencies=[Depends(JWTBearer())])
async def delete_log(logId):
    log = logs_db.find_one({"_id": ObjectId(logId)})
    if(log):
        logs_db.delete_one({"_id": ObjectId(logId)})
    else:
        raise HTTPException(status_code=404, detail="Log not found")