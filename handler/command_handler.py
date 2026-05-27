from .commands import (
    style_command,
    effort_command,
    help_command,
    preferences_command,
    reset_command
)

def handle_command(
    user_id,
    text,
    send_message
):

    parts = text.split()

    command = parts[0]

    args = parts[1:]

    COMMANDS = {
        "/style": style_command,
        "/help": help_command,
        "/reset": reset_command,
        "/effort": effort_command,
        "/preferences": preferences_command,
    }

    handler = COMMANDS.get(command)

    if handler:
        handler(
            user_id,
            args,
            send_message
        )

    else:
        send_message(
            user_id,
            "Неизвестная команда."
        )