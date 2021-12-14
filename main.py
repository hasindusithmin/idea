import uvicorn

from fastapi import BackgroundTasks, FastAPI
from backgroundtask.scrap import (isUpdate,download)
from pydantic import BaseModel
app = FastAPI()


@app.get("/isupdate")
async def check(background_tasks: BackgroundTasks):
    background_tasks.add_task(isUpdate)
    return {"message": "check if website is update"}

@app.get('/send')
async def sendNotification(background_tasks: BackgroundTasks):
    background_tasks.add_task(download)
    return {"message": "Notification sent in the background"}


class Condition(BaseModel):
    currency:str
    timeframe:str
    signal:str

@app.post('/condition')
async def getCondition(condition:Condition):
    conditionDict = condition.dict()
    
    return {"message": "Notification sent in the background"} 

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
