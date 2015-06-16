# coding: utf-8
import os

from flask.ext.script import Manager
from app import create_app

app = create_app()
manager = Manager(app)

@manager.command
def run():
    """启动app"""
    app.run(debug=True,host='0.0.0.0')

if __name__ == "__main__":
    manager.run()
