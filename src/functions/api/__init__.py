from flask import Flask, Request
from werkzeug.datastructures import MultiDict

class MutableRequest(Request):
    """Request subclass to override request parameter storage.

    What this allows us to do is add parameters to request.args, so that we can use 1
    wtforms to validate both query and path parameters.
    """
    parameter_storage_class = MultiDict

class MyFlask(Flask):
    """We use a Flask subclass to tell Flask to use our custom request class
    """
    request_class = MutableRequest

app = MyFlask(__name__)
app.config['WTF_CSRF_ENABLED'] = False

from api import routes
