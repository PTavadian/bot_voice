import os

def deleting_file(path=None):

    if path:
        try:
            os.remove(path)

        except:
            pass

