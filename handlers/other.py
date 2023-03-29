from aiogram import types, Dispatcher 
from create_bot import dp, bot
from handlers import message_answer as msg_answ
from aiogram.dispatcher import FSMContext
import deleting





async def start(message: types.Message, state: FSMContext):
    if message.chat.type == 'private':

        async with state.proxy() as dict_state:
            if dict_state.get('path_to_file'):
                deleting.deleting_file(dict_state['path_to_file'])

        await state.finish() 

        msg_answer = msg_answ.Text()
        language = message.__dict__['_values']['from']['language_code']
        msg = msg_answer.get_msg('reply_8_help', language)
        await message.reply(msg, reply_markup=types.ReplyKeyboardRemove())



        





def regisret_handlers_other(dp : Dispatcher):

    dp.register_message_handler(start,  commands=['start', 'help'], state='*')





