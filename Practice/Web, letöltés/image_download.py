import random
import urllib.request

def download_image(url):
    name = random.randrange(1, 1000)
    fullname = str(name) + ".jpg"
    urllib.request.urlretrieve(url, fullname, )