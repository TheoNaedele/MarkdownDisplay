import os
import uvicorn
from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse, Response
from fastapi.staticfiles import StaticFiles

runningDir = os.path.dirname(os.path.abspath(__file__))
staticDir = os.path.join(runningDir, "static")

test_steps = [
    {"step": "Perform test step 1", "image": None},
    {"step": "Perform test step 2", "image": "C:/Users/TheoN/Desktop/Work/TestChatGPT/MarkdownDisplay/LibManualTestUpdate/static/8166acd8-5f9c-44eb-8126-ff9dac111289.jpg"},
    # Add more test steps as needed
]

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

# Store connected WebSocket clients
connected_clients = set()

@app.websocket("/ws/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    try:
        for step in test_steps:
            await websocket.send_json(step)
            response = await websocket.receive_text()
            print(response)
    except:
        connected_clients.remove(websocket)

@api.get("/getImageByPath")
def getImageByPath(path: str):
    print(path)
    fileObj = open(path,"rb")
    fileContentBlob = fileObj.read()
    fileObj.close()
    return Response(fileContentBlob,media_type="application/octet_stream")

if __name__ == "__main__":
    Main()



