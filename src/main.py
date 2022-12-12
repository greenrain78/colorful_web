from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def main():
    return FileResponse(f"static/html/index.html")

@app.get("/table")
async def main():
    return FileResponse(f"static/html/table/index.html")
