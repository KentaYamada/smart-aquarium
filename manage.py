from backend import app
from backend.commands.create_api import command_create_api


# Register commands
app.cli.add_command(command_create_api)
