from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import List
import os

app = FastAPI()

class DataStorage:
    testcase = ""
    def setTestcase(this, testcase):
        this.testcase = testcase
    def getTestcase(this):
        return this.testcase


class TestStep(BaseModel):
    step: str = Field(..., description="Current step")
    action: str = Field(..., description="Action to perform by the user")
    result: str = Field(..., description="Expected result")

class WorkItemRequest(BaseModel):
    id: str = Field(..., description="ID of the work item to create")
    description: str = Field(..., description="Description of the work item to create")
    maintainer: str = Field(..., description="Author of the work item to create")
    teststeps: List[TestStep] = Field(..., description="List of test steps")
    tags: List[str] = Field(..., description="List of tags for the work item to create")

dataStorage = DataStorage()

@app.post("/postData")
async def postData(data: WorkItemRequest):
    try:
        validated_data = WorkItemRequest(**data.dict())
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid data format: {str(e)}")

    dataStorage.setTestcase(formatWorkitem(data.dict()))
    print(dataStorage.getTestcase())
    
    return {"message": "Data received successfully", "data": data.dict()}

@app.post("/postFile", summary="Upload a .txt file", description="This endpoint accepts a .txt file.")
async def postFile(file: bytes = File(..., media_type="text/plain")):
    # Check if the file is a .txt file
    print(file)
    return {"message": "File received successfully", "file_size": len(file), "file content":file}

@app.get("/getPostedTestcase")
def getPostedTestcase():
    print(dataStorage.getTestcase())
    return dataStorage.getTestcase()

def formatWorkitem(data: dict) -> str:
    testcase_str = f"Testcase {data['id']}\n"
    testcase_str += f"Maintainer: \n {data['maintainer']}\n\n"
    testcase_str += f"Description: \n {data['description']}\n\n"
    testcase_str += "Teststeps\n"
    testcase_str += "| Step | Action | Result |\n"
    for step in data['teststeps']:
        testcase_str += f"| {step['step']} | {step['action']} | {step['result']} |\n"
    testcase_str += f"\nTags: \n"
    for tag in data['tags']:
        testcase_str += f"- {tag}\n"
    return testcase_str

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
