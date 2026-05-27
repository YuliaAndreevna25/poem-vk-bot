from vk_api.keyboard import VkKeyboard
from vk_api.keyboard import VkKeyboardColor


def main_keyboard():

    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button(
        "❤️ Романтичный",
        color=VkKeyboardColor.POSITIVE
    )

    keyboard.add_button(
        "☀️ Жизнерадостный",
        color=VkKeyboardColor.SECONDARY
    )
    
    keyboard.add_button(
        "🌧️ Меланхоличный",
        color=VkKeyboardColor.SECONDARY
    )

    keyboard.add_line()

    keyboard.add_button(
        "⚡ + Усилия",
        color=VkKeyboardColor.POSITIVE
    )

    keyboard.add_button(
        "💤 - Усилия",
        color=VkKeyboardColor.NEGATIVE
    )
    
    keyboard.add_line()
    
    keyboard.add_button(
        "🔄 Сброс",
        color=VkKeyboardColor.NEGATIVE
    )
    
    keyboard.add_button(
        "⚙️ Мои настройки",
        color=VkKeyboardColor.NEGATIVE
    )
    

    keyboard.add_line()

    keyboard.add_button(
        "❓ Помощь",
        color=VkKeyboardColor.SECONDARY
    )

    

    return keyboard.get_keyboard()