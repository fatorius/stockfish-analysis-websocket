from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

app = FastAPI(default_response_class=ORJSONResponse)

# Adiciona o middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


from .controllers import analyzer_ws

app.include_router(analyzer_ws.router)