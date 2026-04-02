import webbrowser
import time

link = input("Enter TikTok video link: ")
views = int(input("Enter number of views: "))

count = 0

print("Starting viewer...")

while count < views:
    webbrowser.open(link)
    count += 1
    print("View", count, "sent")
    time.sleep(3)

print("Done!")
