from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

global b2, b3

b1 = KeyboardButton('/delete') 
b2 = KeyboardButton('/cancel') 
b3 = KeyboardButton('/help') 

kb_message = ReplyKeyboardMarkup(resize_keyboard=True) 
kb_message.row(b3, b2)


def get_kb_list_folders(tpl: tuple, text: str):
    '''Возвращает клавиатуру из списка названий папок'''

    kb_message_4 = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder=text)
    kb_message_4.row(b3, b2)
    for i, n in enumerate(tpl):
        if i == 0:
            kb_message_4.add(KeyboardButton(n[1]))
        else:
            kb_message_4.insert(KeyboardButton(n[1]))

    return kb_message_4

