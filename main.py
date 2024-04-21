from typing import Union
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi import FastAPI

app = FastAPI()

# grab from build and set as static bundle
app.mount("/", StaticFiles(directory="gt-fe-core/dist", html=True), name="static")
@app.get("/{full_path:path}")
async def index(full_path: str):
    return FileResponse("gt-fe-core/dist/index.html")


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}