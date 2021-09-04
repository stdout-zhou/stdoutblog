"""
Copyright @2021 stdout Inc. All rights reserved.
Authors: stdout.
"""

from http import HTTPStatus

from flask import g
from flask_restplus import Namespace
from flask_restplus import Resource

from stdout_blog_backend.models.user_info import UserInfo as UserInfoModel

user_info_namespace = Namespace(__name__, 'user info operations')


@user_info_namespace.route('/user_info/<int:user_id>')
class UserInfo(Resource):

    @user_info_namespace.doc(params={'user_id': 'User id'})
    @user_info_namespace.response(
        HTTPStatus.OK, 'Success', user_info_namespace.schema_model(
            'UserInfo', UserInfoModel
        )
    )
    def get(self, user_id: int):
        user_info = UserInfoModel.get_one_by_id(user_id)
        if user_info is None:
            # todo by stdout: define error type
            raise
        return user_info
