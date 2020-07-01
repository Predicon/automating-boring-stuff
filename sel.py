import shutil,os
# if filename.endswith('.zip')

#searching the file name with the extension.txt and sending them to another folder



    #walking through the path
for foldername,subname,filenames in os.walk('C:\\Users\\Nirav\\Desktop\\quiz-papers'):
        for filename in filenames:
            if filename.endswith('.txt'):

                print(filename)
                shutil.copy('C:\Users\Nirav\Desktop\quiz-papers\filename','C:\Users\Nirav\Desktop\quiz-answers')
print('successful')




