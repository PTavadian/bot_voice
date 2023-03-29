from database.folder import Folders
from database.create_db import DATABASE_NAME, Session, create_db
import os



def sql_start() -> None:
    '''Создает таблицы в БД'''
    db_is_created = os.path.exists(DATABASE_NAME) #проверка, существует БД или нет
    if not db_is_created:
        create_db()
    print('Data base connect OK!')







def append_folder(folder_id: str, title: str, user_id: str, user_date: dict=None) -> str:
    '''Записывает в БД id и название папки и данные пользователя'''
    session = Session()
    try:
        result = session.query(Folders.title).filter(Folders.folder_id == folder_id).one()
    except:
        result = None

    if not result:
        folder = Folders(folder_id, title, user_id, user_date)
        session.add(folder)
        session.commit()
        session.close()
        return 'reply_9_added'
    
    elif result[0] != title:
        session.query(Folders).filter(Folders.folder_id == folder_id).update({Folders.title: title})
        session.commit()
        session.close()
        return 'reply_10_updated'

    else:
        return ''







def get_folder(user_id: str) -> list:
    '''Возвращает название и id папки'''
    session = Session()
    result = session.query(Folders.folder_id, Folders.title).filter(Folders.user_id == user_id).all()
    return result







def del_folder(user_id: str, title: str) -> None:
    '''Удаляет название и id папки'''
    session = Session()
    folder = session.query(Folders).filter((Folders.user_id == user_id) & (Folders.title == title)).one()
    session.delete(folder)
    session.commit()
    session.close()


















