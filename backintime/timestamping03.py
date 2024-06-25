#!/usr/bin/python3
import time
import datetime as dt

def main():
    rightmeow = time.strftime("%Y-%m-%d")
    with open(rightmeow + '-example.txt', 'w') as f:
        f.write('File with current date created!\n')

    hourtime = time.strftime("%H")
    with open(hourtime + '-example.txt', 'w') as f:
        f.write('File with hour timestamp created!\n')

    yearmonth = time.strftime("%Y-%B")
    with open(yearmonth + '-reporting.txt', 'w') as f:
        f.write('File with monthly timestamp created!\n')
    jasons = dt.datetime(1979, 3, 13, 23, 40, 13)
    nowtimeobject = dt.datetime.now()
    print("I've been alive ",(nowtimeobject-jasons).days, " days")

if __name__ == '__main__':
    main()

