import json

from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/echo")
async def echo(request: Request):
    body = await request.json()
    print(json.dumps(body, indent=4))
    return body
