import snscrape.modules.twitter as sntwitter
import pandas as pd
import csv
import random
import os
import time

# Set maximum tweets to pull
maxTweets = 10
maxTweets2 = 1
# Set what keywords you want your twitter scraper to pull
# to-do immigration, border, illegals, undocumented, foreigner, refugee, deport, wall, detention centers, Mexicans, DACA
keyword = "education"
#Open/create a file to append data to
csvFile = open('scraped1.csv', 'a', newline='', encoding='utf8')
#Use csv writer
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['url','date', 'like count','replys','retweets','tweet','metaphorFamily'])

# Write tweets into the csv filter
for i in range(maxTweets2):

    randomEndYear = random.randint(2012, 2020)
    randomEndMonth = random.randint(1, 12)
    randomEndDay = random.randint(1, 30)
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(keyword + ' lang:en since:2011-01-01 until:{}-{}-{} -filter:links -filter:replies'.format(randomEndYear, randomEndMonth, randomEndDay)).get_items()):

            if i > maxTweets :
                break
            csvWriter.writerow([tweet.url, tweet.date, tweet.likeCount, tweet.replyCount, tweet.retweetCount, tweet.content])



csvFile.close()



# alert
i = 0

while i < 1:
    os.system('say "Scraping tweets is done."')
    time.sleep(3)
    i = i + 1
