import os
import random

import vk_api

from dotenv import load_dotenv

from vk_api.longpoll import VkLongPoll
from vk_api.longpoll import VkEventType

from ui.keyboards import main_keyboard

from storage.db import init_db

from handler.message_handler import handle_message

load_dotenv()

init_db()

VK_TOKEN = os.getenv("VK_TOKEN")

vk_session = vk_api.VkApi(
    token=VK_TOKEN
)

vk = vk_session.get_api()

longpoll = VkLongPoll(
    vk_session
)


def send_message(
    user_id: int,
    text: str
):

    vk.messages.send(
        user_id=user_id,

        message=text,

        keyboard=main_keyboard(),

        random_id=random.randint(
            1,
            1_000_000
        )
    )


print("Бот запущен...")


for event in longpoll.listen():

    if (
        event.type == VkEventType.MESSAGE_NEW
        and event.to_me
    ):

        try:

            handle_message(
                event,
                send_message,
                vk
            )

        except Exception as e:

            send_message(
                event.user_id,
                f"Ошибка: {e}"
            )
            break