from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
async def main():
    return FileResponse(f"static/html/index.html")
