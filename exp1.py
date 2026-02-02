from fastapi import FastAPI
from fastapi.responses import FileResponse

new_api = FastAPI()

@new_api.get("/")
async def root():
  return FileResponse("index.html")

@new_api.get("/file", response_class = FileResponse)
async def root_html():
  return "index.html"