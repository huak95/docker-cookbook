from typing import Union
from fastapi import FastAPI
import requests
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


class Message(BaseModel):
    fullname: str
    nickname: str
    bu: str
    heading: str

@app.post("/send_message")
def send_message(message:Message):
    # send http request to the server
    # server_url = "https://line_test.hubhoo.com"
    server_url = "http://localhost:3210"
    endpoint = "/v2/bot/message/push"    
    url = server_url + endpoint
    body = {
        "messages": [
            {
                "type": "flex",
                "altText": "เปิดการใช้งานเชคบัญชีกับไชโย",
                "contents":
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "md",
                        "contents": [
                            {
                                "type": "text",
                                "text": message.heading,
                                "wrap": True,
                                "weight": "bold",
                                "gravity": "center",
                                "size": "xl",
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "margin": "lg",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Name",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "flex": 1,
                                            },
                                            {
                                                "type": "text",
                                                "text": message.fullname,
                                                "wrap": True,
                                                "size": "sm",
                                                "color": "#666666",
                                                "flex": 4,
                                            },
                                        ],
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BU",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "flex": 1,
                                            },
                                            {
                                                "type": "text",
                                                "text": message.bu,
                                                "wrap": True,
                                                "color": "#666666",
                                                "size": "sm",
                                                "flex": 4,
                                            },
                                        ],
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Nickname",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "flex": 1,
                                            },
                                            {
                                                "type": "text",
                                                "text": message.nickname,
                                                "wrap": True,
                                                "color": "#666666",
                                                "size": "sm",
                                                "flex": 4,
                                            },
                                        ],
                                    },
                                ],
                            },
                        ],
                    },
                }
            }
        ]
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, json=body)
    return {
        "status_code": response.status_code,
    }
