import shutil,os
# if filename.endswith('.zip')

#searching the file name with the extension.txt and sending them to another folder

folder_name=input(str('enter the source folder'))
def selcopy(folder):#folder is string of location

    destination=input('Enter the path where you want to copy the file')
    #walking through the path
    for foldername,subname,filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith('.txt'):

                shutil.copy(folder/filename,destination)

    print('successful')

selcopy(folder_name)


