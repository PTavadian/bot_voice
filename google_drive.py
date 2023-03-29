from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


gauth = GoogleAuth()
gauth.LocalWebserverAuth()





def upload_file(folder_id: str ='1nTr7dMufQ3r6DXCJyzws6ZOQFeNDC4PF', name: str ='some_file', path_to_file: str ='file_33.jpg') -> tuple:
    '''Загружает файл в папку диска с открытым доступом и возвращает: название папки и ссылку на загруженный файл'''
    
    drive = GoogleDrive(gauth)

    file_data = drive.CreateFile({'id': folder_id})
    file_data.FetchMetadata()
    title = file_data['title']
    user_date = file_data['lastModifyingUser']

    my_file = drive.CreateFile({'title': name,'parents': [{'id': folder_id}]})
    my_file.SetContentFile(path_to_file) 
    my_file.Upload()

    my_file.InsertPermission({
        'type': 'anyone',
        'value': 'anyone',
        'role': 'reader'})

    link = my_file['alternateLink']

    return title, link, user_date



































