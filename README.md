# Inference Server for google/flan-t5-large

## Running the App
Please ensure you have `Python 3.11.4` or higher installed, as well as the latest version of `pip` and `pipenv` (if needed).
* Install requirements using `pipenv` or `pip install -r requirements.txt`
* Run `python3 ml.app` to download ml model
* Run `uvicorn main:app` to start server or `uvicorn main:app --reload` for hot-reloading
* Access local server's docs page to run inference at `http://127.0.0.1:8000/docs#/default/generate_answer_inference__prompt__get`

* Running docker image: `docker run -it --mount type=bind,source=/tmp,target=/root/.cache -p 8000:8000 dhannywi/google-flan-t5-large`