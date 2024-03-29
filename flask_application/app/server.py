import logging
import time
import uuid
import os

from flask import Flask, jsonify, make_response, render_template
from flask import json
from flask_application.app.forms import CustomRequestForm, DefaultRequestForm
from werkzeug.utils import secure_filename

from renessandro.openai_api import MJConnection
from renessandro.openai_api import ChatGPTHandler
from werkzeug.exceptions import HTTPException
from renessandro.config import FLASK_SECRET_KEY


app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates'
            )

logger = logging.getLogger('server')

mj_runner = MJConnection()
chat_gpt = ChatGPTHandler()
app.config["SECRET_KEY"] = FLASK_SECRET_KEY


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/api/hello', methods=['GET'])
def hello():
    response_body = {'message': 'Hello, world!'}
    status_code = 200
    response_headers = {'Content-Type': 'application/json'}
    response = make_response(jsonify(response_body), status_code)
    response.headers = response_headers
    return response


@app.route('/creative/default', methods=["GET", "POST"])
def mj_request_default():
    form = DefaultRequestForm()
    if form.validate_on_submit():
        file = form.picture_data_file.data
        filename = secure_filename('data.json')
        picture_data_path = "../../image_data/"

        if not os.path.exists(picture_data_path):
            # Create a new directory because it does not exist
            os.makedirs(picture_data_path)
            print("The new directory is created!")
        file.save(os.path.join(picture_data_path, filename))

        for _ in range(100):
            time.sleep(5)
            gpt_mj_prompt = chat_gpt.create_mj_prompt_default()
            mj_runner.mj_request(gpt_mj_prompt)

        response_body = {'message': 'Request to MJ sent!',
                         'Prompt': 100}
        status_code = 200
        response_headers = {'Content-Type': 'application/json'}
        response = make_response(jsonify(response_body), status_code)
        response.headers = response_headers
        return render_template('success_page.html')
    return render_template("default_creative.html", form=form)

@app.route("/creative/custom", methods=["GET", "POST"])
def custom_creative():
    form = CustomRequestForm()
    subject_1 = form.subject_1.data
    subject_1_description = form.subject_1_description.data
    subject_2 = form.subject_2.data
    subject_2_description = form.subject_2_description.data
    place = form.place.data
    action = form.action.data
    quantity = form.quantity.data
    if form.validate_on_submit():
        random_id = uuid.uuid4()
        gpt_result = chat_gpt.create_mj_prompt_custom(subject_1=subject_1,
                                                      subject_1_description=subject_1_description,
                                                      subject_2=subject_2,
                                                      subject_2_description=subject_2_description,
                                                      place=place,
                                                      action=action, )
        logger.info(f"Request prompt: {gpt_result}")
        mj_runner.mj_request(gpt_result)
        return render_template('success_page.html')

    return render_template("custom_creative.html", form=form)


@app.route('/creative', methods=['GET'])
def creative_demo():
    return render_template("demo_page.html")


@app.route("/success")
def success():
    return "Form submitted successfully!"


@app.errorhandler(500)
def pageNotFound(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    logging.error(response.data)
    return render_template("500_error.html"), 500


app.register_error_handler(500, pageNotFound)


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    logging.error(response.data)
    return render_template("error.html")


def main():
    try:
        app.run(host='0.0.0.0', port=8080)
    except KeyboardInterrupt:
        print('Interrupted')
        mj_runner.close_selenium_driver()

    finally:
        logger.debug("Exit program")
        mj_runner.close_selenium_driver()


if __name__ == '__main__':
    main()
