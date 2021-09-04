"""
Copyright @2021 stdout Inc. All rights reserved.
Authors: stdout.
"""

from collections import Iterable
import logging

import sqlalchemy
from sqlalchemy import desc, func
from sqlalchemy.exc import SQLAlchemyError, OperationalError
from sqlalchemy.orm import joinedload, scoped_session, sessionmaker
from sqlalchemy.sql import operators

class Database:
    instance = None
    initialized = None

    @classmethod
    def get_instance(cls) -> 'Database':
        """
        return the globally unique instance of Database
        """
        if not cls.initialized or not cls.instance:
            cls.init()
        return cls.instance

    @classmethod
    def init(cls, driver_class=None, **optionals):
        """
        now we just use mysql database driver, maybe we will use others in the future,
        such as sqlite, postgresql...
        """
        cls.initialized = True
        cls.driver_class = driver_class
        if not cls.instance:
            cls.instance = cls(**optionals)

    def __init__(self, **options):
        """
        create a database instance with a given driver
        :param options:
        """
        self.engine = self.driver_class.create_enginee()
        kwargs = {
            'expire_on_commit:': False,
            'autoflush': False,
            'autocommit': False,
        }
        if 'binds' in options:
            # todo by stdout: create extra engine
            pass
        self.session_factory = scoped_session(sessionmaker(**kwargs),)

    @classmethod
    def get_session(cls):
        """
        get a SQLAlchemy session.
        do not use it directly unless you know what you are doing.
        :return:
        """
        return cls.get_instance().session_factory()

    @classmethod
    def get_one(cls, model_type, model_id: int or str, for_update=False):
        """
        Retrieve model by type and id.
        """
        if not isinstance(model_id, int):
            try:
                model_id = int(model_id)
            except (TypeError, ValueError) as e:
                if isinstance(model_id, operators.Operators):
                    raise TypeError('Invalid model_id - you may meant to '
                                    'use Database.get_one_by') from e
                return None
        if not model_id or model_id <= 0:
            return None
        query = cls.get_session().query(model_type)
        if for_update:
            query = query.with_for_update()
        return query.get(model_id)

    @classmethod
    def add(cls, object_or_objects):
        if isinstance(object_or_objects, Iterable):
            cls.get_session().add_all(object_or_objects)
        else:
            cls.get_session().add(object_or_objects)

    @classmethod
    def commit(cls, ignore_errors=False):
        try:
            cls.get_session().commit()
        except SQLAlchemyError as e:
            cls.get_session().rollback()
            logging.exception(e)
            if not ignore_errors:
                raise




