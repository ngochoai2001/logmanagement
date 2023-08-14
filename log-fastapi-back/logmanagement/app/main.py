from fastapi import FastAPI
from routers import auth, log
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
app = FastAPI()
# 
# NEW
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080","http://192.168.2.17:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# 
app.include_router(auth.authRouter)
app.include_router(log.logRouter)
@app.get("/")
def index():
    return {"Hello":"World"}
if __name__ == "__main__":
    uvicorn.run('main:app', reload=True, port=5000)