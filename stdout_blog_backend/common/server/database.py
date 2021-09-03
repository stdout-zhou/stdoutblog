"""
Copyright @2021 stdout Inc. All rights reserved.
Authors: stdout.
"""


class Database:
    instance = None
    initialized = None

    @classmethod
    def get_instance(cls) -> 'Database':
        """
        return the globally unique instance of Database
        """
        if not cls.initialized or not cls.initialized:
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

