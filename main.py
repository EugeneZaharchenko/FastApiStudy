from typing import Optional

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, Response, JSONResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/calc")
async def calculate(x: int, y: int, z: Optional[int] = None):
    '''http://localhost:8000/calc?x=1&y=3&z=0'''
    if z == 0:
        return JSONResponse(content={"ERROR": "Z cannot be zero"},
                            status_code=400)
        # return Response(content='{"ERROR": "Z cannot be zero"}',
        #                 media_type='application/json', status_code=400)
    if z is None:
        z = 1
    result = (x + y) / z
    return HTMLResponse(f"<h1>{result}</h1>")


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
