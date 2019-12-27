import click
import os
import sqlite3
from flask.cli import with_appcontext
from backend.config import get_config_by_env


def read_sql_file():
    module_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(module_path, 'sql', 'definition.sql')
    query = ''
    with open(filepath) as f:
        query = f.read()
    return query


def build_database(query):
    if not query:
        raise ValueError()
    config = get_config_by_env()
    filepath = config.get_database_path()
    with sqlite3.connect(filepath, isolation_level='EXCLUSIVE') as tran:
        tran.executescript(query)


@click.command('create-db')
@with_appcontext
def command_create_db():
    query = read_sql_file()
    try:
        build_database(query)
        print('Create database successfully')
    except Exception as e:
        print('Failed create database')
        raise e
