import webbrowser
import threading
import time

link = input("Enter TikTok link: ")
views = int(input("Enter number of views: "))
tabs = int(input("How many tabs at once: "))

def open_video():
    webbrowser.open(link)

count = 0

while count < views:
    threads = []
    
    for i in range(tabs):
        t = threading.Thread(target=open_video)
        t.start()
        threads.append(t)
        count += 1
        
        if count >= views:
            break

    for t in threads:
        t.join()

    print("Views opened:", count)
    time.sleep(5)

print("Done")
