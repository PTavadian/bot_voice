from aiogram import types, Dispatcher 
from create_bot import dp, bot
from data_base import db
from keyboards import message_kb, kb_message
import deleting
from handlers import message_answer as msg_answ

import datetime
import google_drive

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup 


class FSMMess(StatesGroup):    
    link_folder = State()





async def get_voice(message: types.Message, state: FSMContext):

    if message.chat.type == 'private':    
        time = datetime.datetime.now()
        time = time.strftime("%d_%m_%Y__%H_%M_%S")

        file_id = message.voice.file_id
        file = await bot.get_file(file_id)
        file_path = file.file_path
        path_to_file = f"voice/{message.chat.username}/voice_{time}.mp3"  
        await bot.download_file(file_path, path_to_file)
        name = f"voice_{message.chat.username}_{time}.mp3"

        async with state.proxy() as dict_state:
            dict_state['name_file'] = name
            dict_state['path_to_file'] = path_to_file

            try:
                folders = db.get_folder(message.from_user.id)
                dict_state['id_and_name'] = folders          
            except:
                pass

        msg_answer = msg_answ.Text()
        language = message.__dict__['_values']['from']['language_code']
        msg = msg_answer.get_msg('reply_1_enter_link', language)

        if folders: 
            hid_msg = msg_answer.get_msg('reply_7_choose', language)
            kb = message_kb.get_kb_list_folders(folders, hid_msg) 
            await message.reply(msg, reply_markup=kb)

        else:
            await message.reply(msg, reply_markup=kb_message)

        await FSMMess.next()





async def cancel_handler(message: types.Message, state: FSMContext):
    '''Выход из состояний'''
    if message.chat.type == 'private':
        current_state = await state.get_state()
        if current_state is None:
            return
        
        async with state.proxy() as dict_state:
            if dict_state.get('path_to_file'):
                deleting.deleting_file(dict_state['path_to_file'])

        await state.finish() 
        await message.reply('ok', reply_markup=types.ReplyKeyboardRemove()) 





async def get_link(message: types.Message, state: FSMContext):

    async with state.proxy() as dict_state:
        name = dict_state['name_file']
        path_to_file = dict_state['path_to_file']

    msg_answer = msg_answ.Text()
    language = message.__dict__['_values']['from']['language_code']

    try:
        id_and_name = dict_state['id_and_name']
        folder_id = None
        if id_and_name:
            folder_id: str
            for tple in id_and_name:
                if tple[1] == message.text:
                    folder_id = tple[0]
                    break

        if not folder_id:
            link: str = message.text

            if link.rfind('?') != -1:
                folder_id: str = link[link.rfind('/')+1:link.rfind('?')] 
            else:
                folder_id: str = link[link.rfind('/')+1:]

        m = google_drive.upload_file(folder_id, name, path_to_file)        
        reply = db.append_folder(folder_id, m[0], message.from_user.id, m[2])   

        hid_msg = ''
        if reply:
            hid_msg = msg_answer.get_msg(reply, language)

        msg = msg_answer.get_msg('reply_2_file_uploaded', language)
        await message.reply(msg + f' {m[0]}\n' + f'{hid_msg}' + m[1], reply_markup=types.ReplyKeyboardRemove())
        deleting.deleting_file(dict_state['path_to_file'])

    except:
        msg = msg_answer.get_msg('reply_3_error', language)
        await message.reply(msg)

    await state.finish()





def regisret_handlers_add_file(dp : Dispatcher):

    dp.register_message_handler(get_voice,  content_types=['voice'], state=None)
    dp.register_message_handler(cancel_handler, state='*', commands='cancel')
    dp.register_message_handler(get_link, state=FSMMess.link_folder)








