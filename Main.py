# https://kickass.unblocked.la/usearch/aaa%20category:games/
import urllib.request
import os
from bs4 import BeautifulSoup


opener = urllib.request.build_opener()
urllib.request.install_opener(opener)


def saveImage(filename, img_src):
    img_data = opener.open(img_src)
    file = open(filename, "wb")
    file.write(img_data.read())
    file.close()


def main():
    link = input("Enter the link of the 4chan post:\n")
    foldername = input("Enter name for the folder:\n")
    print()

    default_dir = os.path.join(os.path.expanduser("~"), "Pictures")

    page = BeautifulSoup(urllib.request.urlopen(link), "html.parser")
    images = page.findAll('a', {"class": "fileThumb"})

    os.mkdir(os.path.join(default_dir, foldername))
    default_dir = os.path.join(default_dir, foldername)

    i = 1
    for img in images:
        img_src = "http:" + img["href"]
        filename = os.path.join(default_dir, img_src.split("/")[-1])
        saveImage(filename, img_src)
        print(i, "\tSaved: ", img_src, "\tin: ", default_dir)
        i += 1

    print("\nTotal images: ", i)


if __name__ == "__main__":
    print("+-----------------------------------------------------+")
    print("|               Download Manager (4Chan)              |")
    print("|                   © Giani Noyez                     |")
    print("+-----------------------------------------------------+")
    main()
