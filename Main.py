import urllib.request
import urllib.error
import os
import time
import random
import datetime
from bs4 import BeautifulSoup

link = ""
folder_name = ""
default_dir = ""

counter = 0
start_time = datetime.datetime.now()

opener = urllib.request.build_opener()
urllib.request.install_opener(opener)


def save_image(filename, img_src):
    img_data = opener.open(img_src)
    file = open(filename, "wb")
    file.write(img_data.read())
    file.close()


def get_input():
    global link, folder_name
    link = input("Enter the link of the 4chan post:\n")
    folder_name = input("Enter name for the folder:\n")
    print()


def set_up_environment():
    global default_dir, folder_name
    default_dir = os.path.join(os.path.expanduser("~"), "Pictures")
    os.mkdir(os.path.join(default_dir, folder_name))
    default_dir = os.path.join(default_dir, folder_name)


def download_thread_images():
    global counter, link, default_dir
    run = True
    while run:
        print(datetime.datetime.now())
        try:
            page = BeautifulSoup(urllib.request.urlopen(link), "html.parser")
            images = page.findAll('a', {"class": "fileThumb"})

            i = 1
            for img in images:
                img_src = "http:" + img["href"]
                filename = os.path.join(default_dir, img_src.split("/")[-1])
                save_image(filename, img_src)
                print(i, "\tSaved: ", img_src, "\tin: ", default_dir)
                i += 1
            counter = i

            time_to_sleep = random.randrange(30, 60)
            print('Sleeping for ', time_to_sleep, ' seconds')
            time.sleep(time_to_sleep)
        except urllib.error.HTTPError as e:
            print("Total images downloaded", counter)
            print("The thread 404'd in", datetime.datetime.now() - start_time)
            run = False
        except urllib.error.URLError as e:
            print("Error while connecting to the server. Check the URL and/or your network connection.")
            run = False


def main():
    get_input()
    set_up_environment()
    download_thread_images()


if __name__ == "__main__":
    print("+-----------------------------------------------------+")
    print("|               Download Manager (4Chan)              |")
    print("|                   © Giani Noyez                     |")
    print("+-----------------------------------------------------+")
    main()
