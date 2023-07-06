from typing import Union
from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/send_message")
def send_message(message: str):
    #send http request to the server
    # server_url = "https://line_test.hubhoo.com"
    server_url = "http://localhost:3210"
    endpoint = "/v2/bot/message/push"
    your_name = "Warach D"
    url = server_url + endpoint
    body = {
        "messages":
        [
            {
                "type": "text",
                "text": your_name + ": " + message,
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=body)
    return {
        "status_code": response.status_code,
    }

