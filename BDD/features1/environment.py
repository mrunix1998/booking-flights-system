import time
from threading import Thread
from werkzeug.serving import make_server
from app import create_app
import os


def before_all(context):
    print("[>] Run app api")
    app = create_app('development')
    server = make_server("0.0.0.0", 6000, app)
    server_thread = Thread(target=server.serve_forever)
    server_thread.start()
    context.server = server


def after_all(context):
    context.server.shutdown()
    print("[>] Done!")
