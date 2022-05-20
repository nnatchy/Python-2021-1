import urllib
from bs4 import BeautifulSoup
from time import sleep
import copy

table2 = soup.find_all('span',string = 'ภาพยนตร์')[1].parent.find_next_sibling()