import threading
import time
from threading import Timer

titles = ["Harry Potter","Pride and Prejudice"]
pages = [250, 430]
first_name = ["J.K", "Jane"]
last_name = ["Rowling", "Austen"]
locations = ["UK", "UK"]

def build_book_dict(titles, pages, first_name, last_name, locations):
    #define inputs
    inputs = zip(titles, pages, first_name, last_name, locations)
    #define empty dictionary below
    d = {}
    #for loop
    for titles, pages, first_name, last_name, locations in inputs:
        d.update({
            titles : {'Pages': pages, 'Author': {'First': first_name, "Last": last_name}, 'Publisher': {"Location": locations}}
                        },)
    
    time.sleep(3)
    return d

print(build_book_dict(titles, pages, first_name, last_name, locations))

timer = threading.Timer(5, build_book_dict(titles, pages, first_name, last_name, locations))
timer.start()
timer.cancel()
print("Timer Cancelled")

