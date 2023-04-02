from flask import Flask, jsonify, make_response, render_template, redirect, url_for
from mj_request import MJRequest
from forms import MyForm

from openai_request import create_mj_prompt

app = Flask(__name__)

mj_runner = MJRequest()
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
        count = form.name.data
        gpt_result = create_mj_prompt()
        print(gpt_result)

        mj_runner.mj_request(gpt_result)

        # Handle the form data, e.g., save to database, send an email, etc.
        print(f"Name: {count}")
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

        # Handle the form data, e.g., save to database, send an email, etc.
        print(f"Name: {gpt_result}")
    return render_template("mj_home.html", form=form)



def main():
    try:
        app.run(host='0.0.0.0', port=8080)
    except KeyboardInterrupt:
        print('Interrupted')
        # mj_runner.close_selenium_driver()

    finally:
        print("EXIT")
        mj_runner.close_selenium_driver()


if __name__ == '__main__':
    main()


