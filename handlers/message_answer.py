
class Text:

    reply = {'reply_1_enter_link': {'en': 'Enter the link where you want to send the file', 'ru': 'Введи ссылку, куда нужно отправить файл'},
             
            'reply_2_file_uploaded': {'en': 'The file is uploaded to google drive in a folder:', 'ru': 'Файл загружен на гугл диск в папку:'},

            'reply_3_error': {'en': 'File upload error, please check the link and open write to your folder', 'ru': 'Ошибка загрузки файла, проверьте ссылку и откройте возможность записи в вашу папку'},

            'reply_4_select': {'en': 'Select the folder you want to delete', 'ru': 'Выберите папку, которую хотите удалить'},

            'reply_5_no_folder': {'en': 'You don\'t have any folder yet', 'ru': 'У вас еще нет ни одной папки'},

            'reply_6_deleted': {'en': 'Folder deleted', 'ru': 'Папка удалена'},

            'reply_7_choose': {'en': 'choose folder name', 'ru': 'выбери название папки'},

            'reply_8_help': {'en': 'The bot can upload voice messages to google drive in a folder with public write access', 'ru': 'Бот может загружать голосовые сообщение на гугл диск в папку с открытым доступом для записи'},
            
            'reply_9_added': {'en': '(The folder has been added)\n', 'ru': '(папка добавлена)\n'},
            
            'reply_10_updated': {'en': '(Updated folder name)\n', 'ru': '(обновлено название папки)\n'},}








    def get_msg(self, msg=None, language=None):

        if language == 'ru':
            self.msg = self.reply[msg]['ru']
        else:
            self.msg = self.reply[msg]['en']

        return self.msg
            

