"""
Copyright @2021 stdout Inc. All rights reserved.
Authors: stdout.
"""

from werkzeug.debug import DebuggedApplication

from stdout_blog_backend.common.server.launchers.gunicorn_launcher import GunicornApp

if __name__ == '__main__':
    options = {

    }
    GunicornApp(DebuggedApplication())
