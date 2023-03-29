from aiogram.utils import executor 
from database import db
from create_bot import dp





async def on_startup(_):
    db.sql_start()



from handlers import other, delete, add_file

other.regisret_handlers_other(dp)
add_file.regisret_handlers_add_file(dp)
delete.regisret_handlers_delete(dp)





executor.start_polling(dp, skip_updates=True, on_startup=on_startup) 

