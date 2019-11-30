import os
import click
from flask.cli import with_appcontext


def get_template_file_path(filename):
    module_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(module_path, 'templates', filename)


def get_api_file_path(filename):
    module_path = os.path.dirname(os.path.abspath(__file__))
    module_path = module_path.replace('commands', 'controller')
    return os.path.join(module_path, filename)


@click.command('create-api')
@click.argument('name')
@with_appcontext
def command_create_api(name):
    filepath = get_template_file_path('api.txt')
    with open(filepath, mode='r') as f:
        text = f.read()
    text = text.replace('{{name}}', name)

    write_filename = '{0}.py'.format(name)
    write_file_path = get_api_file_path(write_filename)
    with open(write_file_path, mode='w') as f:
        f.write(text)

    message = 'succeeded' if os.path.exists(write_file_path) else 'failed'
    print('{0} create {1}.'.format(write_filename, message))
