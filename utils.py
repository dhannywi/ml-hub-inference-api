from fastapi.responses import JSONResponse
from transformers import pipeline

def load_model(model_id):
    return pipeline(model=model_id)

def response(status=200, message=None, result=None, version="v1", metadata={}):
    if message==None:
        message = 'Success' if status in range(200, 299) else 'Error'

    return JSONResponse(content={
            "status": status,
            "message": message,
            "result": result,
            "version": version,
            "metadata": metadata
        })