import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

page = requests.get('https://www.baseball-reference.com/')

print(page.text)