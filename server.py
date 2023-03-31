from flask import Flask, jsonify, make_response, render_template, redirect, url_for
from mj_request import MJRequest
from forms import MyForm


app = Flask(__name__)

text = 'The majestic mountains rise high into the sky, their rugged peaks piercing through the clouds. The sun casts a warm golden glow over their rocky slopes, highlighting the vibrant greens of the trees and the deep blues of the rivers and lakes that wind through the valleys below. As you gaze at the breathtaking panorama, you are struck by the sheer grandeur and immensity of these natural wonders. The air is crisp and invigorating, and the silence is punctuated only by the gentle rustling of leaves and the distant calls of birds. It is a scene of unparalleled beauty and awe-inspiring power, and one that leaves an indelible impression on all who behold it.'

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
    mj_runner.mj_request(text)
    response_body = {'message': 'Request to MJ sent!'}
    status_code = 200
    response_headers = {'Content-Type': 'application/json'}
    response = make_response(jsonify(response_body), status_code)
    response.headers = response_headers
    return response


@app.route("/mj/request", methods=["GET", "POST"])
def index():
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        mj_runner.mj_request(name)

        # Handle the form data, e.g., save to database, send an email, etc.
        print(f"Name: {name}")
        return redirect(url_for("success"))

    return render_template("index.html", form=form)

@app.route("/success")
def success():
    return "Form submitted successfully!"

if __name__ == '__main__':
    mj_runner = MJRequest()
    try:
        app.run()

    except KeyboardInterrupt:
        print('Interrupted')
        mj_runner.close_selenium_driver()
        try:
            import sys

            sys.exit(130)
        except SystemExit:
            import os

            os._exit(130)
