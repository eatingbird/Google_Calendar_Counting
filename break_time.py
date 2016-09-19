import time
import webbrowser

total_breaks = 3
break_count = 0

print ("This program started on "+time.ctime())
while (break_count < total_breaks):
    time.sleep (10)
    webbrowser.open("http://www.seahusa.com")
    break_count +=1
print ("Program ended on "+time.ctime())

