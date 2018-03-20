import bs4 as bs
import urllib3.request
saurce = urllib3.request.urlopen("https://www.matthewwoodward.co.uk/start-a-blog/").read()
soup = bs.BeautifulSoup(saurce,'lxml')

print(soup)