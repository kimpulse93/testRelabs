from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

file_name = "index.html"
html_file = open(file_name, 'r', encoding='utf-8')
html = html_file.read()

app = FastAPI()


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_json(f"{data}")
