import schedule,time
import requests , os , bs4 ,io
link=input(str('enter the link'))

if not os.path.exists(os.getcwd() + '/html_txt_files'):
    os.mkdir('html_txt_files')
def job():
    number=1
    link=input(str('enter the link'))
    res=requests.get(link)
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    select_tag=soup.select('p')
    simple_string=''
    for i in range(len(select_tag)):

        simple_string+=select_tag[i].getText()
        simple_string+='/n'
    FilesPath = os.getcwd() + '/html_txt_files'
    File = io.open(FilesPath + '/updated' + str(number) + '.txt', 'w',encoding='utf-8')
    File.write(simple_string)
    print('file updated successfully') 
    print(type(simple_string))
    File.close()   

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


