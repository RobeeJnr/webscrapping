import requests
from bs4 import BeautifulSoup
import pandas as pd
 
page = requests.get('https://www.lightdl.xyz/2021/03/yqsadtgrre.html') # Getting page HTML through request
soup = BeautifulSoup(page.content, 'html.parser') # Parsing content using beautifulsoup



episode = []
link = []
links = soup.select("div a", attrs={'class':'post-body'}) # Selecting all of the anchors with titles
#first10 = links[:18] # Keep only the first 10 anchors
for anchor in links:
    episode_name = anchor.text 
    episode_link = anchor.get('href')

    episode.append(episode_name)
    link.append(episode_link)
    print(episode_link)

    df = pd.DataFrame({'episode':episode,'link':link}) 
    df.to_csv('all-american.csv', index=False, encoding='utf-8')
print("Done")

    
