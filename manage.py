#!/usr/bin/env python
import os
from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand

from app import create_app, db


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


@manager.shell
def make_shell_content():
    return dict(app=app, db=db)


manager.add_command('server', Server())
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':

    manager.run()

