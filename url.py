import requests 
from bs4 import BeautifulSoup
import os
import re


url = input("Please enter your url: ")

def url_check(url: str):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False
    
if not url_check(url):
    print("Error, URL is invalid or unreachable")
    exit()

path = input("Please enter your directory path name to dowload png files: ")


def website_png(url: str,path: str):
    
    req = requests.get(url)

    soup = BeautifulSoup(req.text, 'html.parser')
# 
    images = soup.find_all('img', src=re.compile(".png", re.IGNORECASE))
     
    if images:
        try:
            os.makedirs(os.path.join(os.getcwd(),path))
        except:
            pass
        os.chdir(os.path.join(os.getcwd(),path))
    else:
        print("There is no .png extension image in this website")
        return

    i = 0
    for image in images:
        i = i + 1
        links = image['src']
        if not links.startswith('http') or not links.startswith('https'):
            #print('Skipping: ', links)
            continue
        with open("{}.png".format(i), 'wb') as f:
            saveimage = requests.get(links)
            f.write(saveimage.content)
            print('Writing: ',links)

if __name__ == "__main__":

    website_png(url=url, path=path)








