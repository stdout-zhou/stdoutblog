"""
Copyright @2021 stdout Inc. All rights reserved.
Authors: stdout.
"""

from werkzeug.debug import DebuggedApplication

from stdout_blog_backend.app import app

if __name__ == '__main__':
    options = {
    }
    app.run(debug=True)
