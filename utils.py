from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from fastapi.responses import JSONResponse


def load_model(model_id):
    return AutoModelForSeq2SeqLM.from_pretrained(model_id)

def load_tokenizer(model_id):
    return AutoTokenizer.from_pretrained(model_id)

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