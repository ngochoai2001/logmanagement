from pydantic import BaseModel, Field
from datetime import datetime
from model.log import Log

def log_serializer(log: Log) -> dict:
    return{
        "_id": str(log["_id"]),
        "system_subscribe":	log["system_subscribe"],
        "department_name":	log["department_name"],
        "personal_name":	log["personal_name"],
        "name":	log["name"],
        "open_date":	log["open_date"],
        "respond_time":	log["respond_time"],
        "remote_addr":	log["remote_addr"],
        "return_date":	log["return_date"],
        "remote_port":	log["remote_port"],
        "path_info":	log["path_info"],        
        "remote_port":	log["remote_port"],        
        "p_request_method":	log["p_request_method"],        
        "content_type":	log["content_type"],        
        "server_name":	log["server_name"],        
        "server_protocol":	log["server_protocol"],        
        "access_token":	log["access_token"],        
        "http_user_agent":	log["http_user_agent"],        
        "query_string":	log["query_string"],        
        "msg":	log["msg"]                   
    }
def logs_serializer(logs) -> list:
    return [log_serializer(log) for log in logs]
    