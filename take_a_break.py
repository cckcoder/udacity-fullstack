import time
import webbrowser

total_breaks = 3
break_count = 0

print('This program started on ', time.ctime())
while break_count < total_breaks:
    time.sleep(10)
    print('Break Time count: ', break_count)
    webbrowser.open('https://www.youtube.com/watch?v=RgKAFK5djSk&list=RDRgKAFK5djSk&start_radio=1')
    time_break += 1
