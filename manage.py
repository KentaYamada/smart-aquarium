from backend import app
from backend.commands.create_api import command_create_api
from backend.commands.create_db import command_create_db


# Register commands
app.cli.add_command(command_create_api)
app.cli.add_command(command_create_db)
