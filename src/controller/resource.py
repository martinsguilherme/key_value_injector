from fastapi import FastAPI, Response
import model.request as request
import model.injector as injector

app = FastAPI()
header_injector = injector.Injector()


#GET request to return random key:value
@app.get("/key_value")
async def get_request(response: Response):
    response.headers["Key-Value"] = header_injector.get_key_value()
    return {"Success. Check the response headers"}

#POST request that accepts key:value as JSON input
@app.post("/key_value")
async def post_request(payload: request.Request, response: Response):
    response.headers["Key-Value"] = payload.get_key_value()
    return payload
