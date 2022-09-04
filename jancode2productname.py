import requests
from bs4 import BeautifulSoup

def postprocessing(name):
    left = name.find("[")
    right = name.find("]")
    name = name[left+1:right]
    sp = name.split("/")
    maker = sp[0]
    name = sp[1]
    return name
    

def jan2name(url, jancode):
    html_text = requests.get(url+jancode).text
    soup = BeautifulSoup(html_text, 'html.parser')
    hoge =  soup.find('title')
    hoge = hoge.text
    name = postprocessing(hoge)
    return name

