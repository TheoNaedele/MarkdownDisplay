import os
import uvicorn
from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse, Response
from fastapi.staticfiles import StaticFiles
from typing import List

runningDir = os.path.dirname(os.path.abspath(__file__))
staticDir = os.path.join(runningDir, "static")

#maybe append test steps here?
test_steps = [
    {"step": "Perform test step 1 \n This is a new line", "image": None},
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
#connected_clients = set()
connected_clients: List[WebSocket] = []
myWebsocket: WebSocket = None

@app.websocket("/ws/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)
    #connected_clients.add(websocket)
    try:
        for step in test_steps:
            await websocket.send_json(step)
            response = await websocket.receive_json()
            print(response)
            #await sendTeststepToFrontend(step)
    except:
        connected_clients.remove(websocket)

async def sendTeststepToFrontend(teststep: dict):
    await connected_clients[0].send_json(test_steps[0])
    return


@api.get("/getImageByPath")
def getImageByPath(path: str):
    print(path)
    fileObj = open(path,"rb")
    fileContentBlob = fileObj.read()
    fileObj.close()
    return Response(fileContentBlob,media_type="application/octet_stream")

if __name__ == "__main__":
    Main()



