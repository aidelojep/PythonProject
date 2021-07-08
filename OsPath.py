import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    print(os.name)

print("Item exist :" + str(path.exists("textfile.txt")))
print("Item is a file: " + str(path.isfile("textfile.txt")))
print("Item is a directory: " + str(path.isdir("textfile.txt")))

print("Item path is real: " + str(path.realpath("textfile.txt")))
print("Item path splitted: " + str(path.split(path.realpath("textfile.txt"))))

if __name__ == "__main__":
    main()
