# Inference API for Machine Learning Hub

## Running the App Locally
Please ensure you have `Python 3.11.4` or higher installed, as well as the latest version of `pip` and `pipenv` (if needed).
* Activate a virtual environment `pipenv shell`
* Install requirements `pipenv install -r requirements.txt` and `pipenv install -r ml_requirements.txt`
* Run `python3 ml.app` to download ml model
* Run `uvicorn main:app` to start server or `uvicorn main:app --reload` for hot-reloading
* Access local server's docs page to run inference at `http://127.0.0.1:8000/docs#/default/generate_answer_inference__prompt__get`

## Using pre-built docker image
* Pull image from docker hub: `docker pull dhannywi/inference-api`
* Running docker image with bind mount: `docker run --rm --mount type=bind,source=/tmp,target=/root/.cache -p 5000:5000 dhannywi/inference-api`
* Access inference server on: `http://0.0.0.0:5000/inference/{model_id}` and be sure to pass your prompt as a JSON object on your request body. Eg. `{"prompt": "What is the capital of France?"}`