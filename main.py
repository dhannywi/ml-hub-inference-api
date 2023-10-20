from fastapi import FastAPI, Request
from pipelines import get_answer
from utils import load_model, response
from const import PRELOADED_MODELS
from schema import ReqPostText2TextGeneration
import uvicorn
from pydantic import ValidationError


for model_id in PRELOADED_MODELS:
    load_model(model_id)

app = FastAPI()

@app.get('/')
def title():
    return 'Machine Learning Hub Inference API!'

@app.get('/inference')
def available_models():
    try:
        if len(PRELOADED_MODELS) != 0:
            models = {"pipeline_tag": "text2text-generation", "available_models": PRELOADED_MODELS}
            return response(result=models)
    except Exception as e:
        return response(
            status= 500,
            message= str(e)
        )

@app.post('/inference/{model_id:path}')
async def generate_answer(model_id:str, request: Request) -> str:
    body = await request.json()
    try:
        ReqPostText2TextGeneration(**body)
    except ValidationError as e:
        return response(
            status= 400,
            message= 'Bad Request: ' + str(e)
        )
    except Exception as e:
        return response(
            status= 500,
            message= str(e)
        )
    answer = get_answer(model_id, body['prompt'])
    return response(result=answer)

if __name__ == "__main__":
    # change port number back to 5000 if not running two APIs locally
    uvicorn.run("main:app", host='0.0.0.0', port=8080, log_level="info")