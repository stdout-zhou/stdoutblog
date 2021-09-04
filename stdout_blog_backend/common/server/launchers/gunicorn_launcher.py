"""
Copyright @2021 stdout Inc. All rights reserved.
Authors: stdout.
"""

import gunicorn.app.base


class GunicornApp(gunicorn.app.base):
    """
    server launcher using the Gunicorn server.
    """

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(GunicornApp, self).__init__()