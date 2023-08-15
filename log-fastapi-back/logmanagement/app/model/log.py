from pydantic import BaseModel
from datetime import datetime
class Log(BaseModel):
    system_subscribe:	str
    department_name	:	str
    personal_name	:	str
    name			:	str
    open_date		:	datetime
    respond_time	:	float
    remote_addr		:	str
    return_date		:	datetime
    remote_port		:	int
    path_info		:	str
    content_length	:	int
    server_port		:	int
    p_request_method:	str
    content_type	:	str 
    server_name		:	str
    server_protocol	:	str
    access_token	:	str
    function_name	:	str
    http_user_agent	:	str
    query_string 	:	str
    msg 	        :   str
