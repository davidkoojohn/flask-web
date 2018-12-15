
from flask.ext.script import Manager, Server

from app import create_app as app


manage = Manager(app)


@manage.shell
def make_shell_content():
    return dict(app=app)


if __name__ == '__main__':
    manage.add_command('server', Server())

    manage.run()

