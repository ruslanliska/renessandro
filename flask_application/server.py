import logging

from flask import Flask, jsonify, make_response, render_template
from forms import MyForm

from renessandro.openai_api.openai_request import create_mj_prompt
from renessandro.openai_api.mj_request import MJConnection
app = Flask(__name__)

logger = logging.getLogger('server')

mj_runner = MJConnection()
app.config["SECRET_KEY"] = "your-secret-key-ruslan" # Replace "your-secret-key" with a secure secret key


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


@app.route('/api/mj/default', methods=['GET'])
def mj_request_default():
    gpt_mj_prompt = create_mj_prompt()
    mj_runner.mj_request(gpt_mj_prompt)
    response_body = {'message': 'Request to MJ sent!',
                     'Prompt': gpt_mj_prompt}
    status_code = 200
    response_headers = {'Content-Type': 'application/json'}
    response = make_response(jsonify(response_body), status_code)
    response.headers = response_headers
    return response


@app.route("/mj/request", methods=["GET", "POST"])
def index():
    form = MyForm()
    if form.validate_on_submit():
        gpt_result = create_mj_prompt()
        logger.info(f"Request prompt: {gpt_result}")
        mj_runner.mj_request(gpt_result)

    return render_template("index.html", form=form)

@app.route("/success")
def success():
    return "Form submitted successfully!"

@app.route("/mj", methods=["GET", "POST"])
def mj_home():
    form = MyForm()
    if form.validate_on_submit():
        gpt_result = create_mj_prompt()

        mj_runner.mj_request(gpt_result)
    return render_template("mj_home.html", form=form)


@app.errorhandler(500)
def pageNotFound(error):
    return render_template("error.html"), 500

app.register_error_handler(500, pageNotFound)


def main():
    try:
        app.run(host='0.0.0.0', port=8080)
    except KeyboardInterrupt:
        print('Interrupted')
        # mj_runner.close_selenium_driver()

    finally:
        logger.debug("Exit program")
        # mj_runner.close_selenium_driver()


if __name__ == '__main__':
    main()


