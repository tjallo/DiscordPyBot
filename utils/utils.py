import os, shutil
#Oldwindows remover
#def removeDownloads():
#    folder = 'Downloads/'
#    for filename in os.listdir(folder):
#        file_path = os.path.join(folder, filename)
#        try:
#            if os.path.isfile(file_path) or os.path.islink(file_path):
#                os.unlink(file_path)
#            elif os.path.isdir(file_path):
#                shutil.rmtree(file_path)
#        except Exception as e:
#            print('Failed to delete %s. Reason: %s' % (file_path, e))

def removeDownloads():
    os.system('/bin/bash -c "rm -r -f downloads"')
    os.system('/bin/bash -c "mkdir downloads"')

def removeFried():
    os.remove("downloads\\fried.jpeg")
def remove_at(i, s):
    return s[:i] + s[i+1:]

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def addLineToFile(line, fileName):
    with open(fileName, "a") as myfile:
        myfile.write(line)

def readFileToVariable(filepath):
    data = ""
    with open(filepath, "r") as textfile:
        return textfile.read()