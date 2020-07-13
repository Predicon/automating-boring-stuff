import time , subprocess, webbrowser
def timer():
    time_for_timer=int(input(('enter the number of seconds')))
    while time_for_timer>1:
        print(time_for_timer)
        time.sleep(1)
        time_for_timer=time_for_timer-1
print(timer())
subprocess.Popen(webbrowser.open('https://www.google.com/'))