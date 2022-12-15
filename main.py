import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
from fastapi import FastAPI
import uvicorn
from core.router import set_routers
from core.router import set_routersgroupe
from core import settings

app = FastAPI(title="Python-FastApi")

@app.on_event("startup")
async def startup():
    set_routers(app)
    set_routersgroupe(app)


@app.on_event("shutdown")
async def shutdown():
    pass

if __name__ == "__main__":
    uvicorn.run("main:app",  host = settings.HOST, port = settings.PORT, reload=True)