#!/usr/bin/env python3
# HELLO WORLD SERVICE

import logging

from flask import Flask
from flask_api import status
from healthcheck import HealthCheck


health = HealthCheck()
app = Flask("Hello World Service")
app.logger.setLevel(logging.DEBUG)
app.add_url_rule("/health", "health", view_func=lambda: health.run())


@app.route("/", methods=["GET","POST"])
def emailrequests_get():
    return ("Hello World!", status.HTTP_200_OK)


if __name__ == "__main__":
    # Set debug mode to False so that Visual Studio's debugger can hit
    # breakpoints
    # https://flask.palletsprojects.com/en/2.2.x/quickstart/#debug-mode
    app.run(debug=False)
