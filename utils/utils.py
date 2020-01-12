import os, shutil

def removeDownloads():
    folder = 'Downloads/'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def removeFried():
    os.remove("downloads\\fried.jpeg")            

def remove_at(i, s):
    return s[:i] + s[i+1:]