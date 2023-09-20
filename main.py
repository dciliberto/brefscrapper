#TO DO:
#change getHitter to a return rather than a print
#make a function to get the WAR of a list of players
#figure out pitcher WAR
#figure out timeout/fangraphs data limiting
#export and combine into existing .csv

from bs4 import BeautifulSoup
from selenium import webdriver

#pitchers untested
def getHitterWAR(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    browser = webdriver.Chrome(options=options)
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html,'lxml')
    print(soup.find('tr', {"class" : "row-career row-mlb-season"}).find('td',{"data-col-id" : "WAR"}).text.strip())
    browser.close()
    
getHitterWAR('https://www.fangraphs.com/players/joc-pederson/11899/stats?position=OF')