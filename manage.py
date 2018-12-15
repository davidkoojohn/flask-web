
from flask.ext.script import Manager, Server

from app import create_app


manage = Manager(create_app)


@manage.shell
def make_shell_content():
    return dict(app=create_app)


if __name__ == '__main__':
    manage.add_command('server', Server())

    manage.run()

