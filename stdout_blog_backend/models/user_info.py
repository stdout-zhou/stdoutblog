"""
Copyright @2021 stdout Inc. All rights reserved.
Authors: stdout.
"""

from sqlalchemy.sql.functions import now
from sqlalchemy.sql.schema import Column
from sqlalchemy.types import BOOLEAN, VARCHAR


class UserInfo(object):
    user_id = Column(VARCHAR(13), nullable=False, unique=True)
    password = Column(VARCHAR(13), nullable=False)
    nick_name = Column(VARCHAR(13), nullable=False)
    is_active = Column(BOOLEAN, nullable=False, default=True)

    @classmethod
    def create(cls, user_id, password, nick_name, is_active=True, commit=False):
        cls.user_id = user_id
        # todo by stdout: change the password store in the database.
        cls.password = password
        cls.nick_name = nick_name
        cls.is_active = is_active
        instance = cls


