from aiogram import types, Dispatcher 
from create_bot import dp, bot
from database import db
from handlers import message_answer as msg_answ
from keyboards import message_kb 

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup 



class FSMMess(StatesGroup):    
    order = State()





async def delete(message: types.Message, state: FSMContext):
    if message.chat.type == 'private':

        folders = db.get_folder(message.from_user.id)

        msg_answer = msg_answ.Text()
        language = message.__dict__['_values']['from']['language_code']

        if folders:
            msg = msg_answer.get_msg('reply_4_select', language)
            hid_msg = msg_answer.get_msg('reply_7_choose', language)
            kb = message_kb.get_kb_list_folders(folders, hid_msg) 
            await message.reply(msg, reply_markup=kb)

        else:
            msg = msg_answer.get_msg('reply_5_no_folder', language)
            await message.reply(msg)
            await state.finish() 
    
        await FSMMess.next()





async def order(message: types.Message, state: FSMContext):

    db.del_folder(message.from_user.id, message.text)
    msg_answer = msg_answ.Text()
    language = message.__dict__['_values']['from']['language_code']
    msg = msg_answer.get_msg('reply_6_deleted', language)
    await message.reply(msg, reply_markup=types.ReplyKeyboardRemove())
    await state.finish()





def regisret_handlers_delete(dp : Dispatcher):

    dp.register_message_handler(delete,  commands='delete')
    dp.register_message_handler(order, state=FSMMess.order)



