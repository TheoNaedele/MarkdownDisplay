import os
import uvicorn
from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

runningDir = os.path.dirname(os.path.abspath(__file__))
staticDir = os.path.join(runningDir, "static")


app = FastAPI(title = "DatabaseUIWebservice")
api = FastAPI(title="DatabaseUIApi")

app.connection = {
    "IpAdress": "192.168.178.54",
    "Port" : 11000,
    "BufferSize" : 1024,
    "Timeout": 5.0
}

def Main():
    app.mount("/api", api)
    app.mount("/", StaticFiles(directory=staticDir, html=True), name = "static")
    uvicorn.run(app,port=8000)

@api.get("/getNewMarkdownContent")
def getNewMarkdownContent():
    file = open(staticDir+"/testMarkdown.md","rt")
    fileText = file.read()
    fileText.replace("\"","'")
    print(fileText)
    file.close()
    return fileText

if __name__ == "__main__":
    Main()

