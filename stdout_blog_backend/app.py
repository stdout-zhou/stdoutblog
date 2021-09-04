"""
Copyright @2021 stdout Inc. All rights reserved.
Authors: stdout.
"""

from flask import Blueprint
from flask import jsonify
from flask import request
from flask_restplus import Api
from flask import Flask

from stdout_blog_backend.endpoints.user_info import user_info_namespace

blueprint = Blueprint('api', __name__, url_prefix='/stdout_blog')

api = Api(
    blueprint,
    title='stdout blog api',
    version='1.0',
    description='stdout blog api',
)

api.add_namespace(user_info_namespace, '/v1')

app = Flask(__name__)
app.register_blueprint(blueprint)
