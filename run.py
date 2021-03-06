#!/usr/bin/python

import sqlite3
import urllib2
import unicodedata
from BeautifulSoup import BeautifulSoup

source = 'https://www.heyjobs.de/en/jobs-in-berlin'
soup = BeautifulSoup(urllib2.urlopen(source).read())

links = soup.findAll('a') 
adds = [x for x in links if x.get('href') != None and '/en/jobs' in x.get('href')] # select just those links that are adds

title_and_uid_with_id = [(x, # Index
                         unicodedata.normalize('NFKD', adds[x].div.div.div.nextSibling.string).encode('ascii','ignore'), # Title
                         adds[x]['href'].split('/')[-1]) # UID
                         for x in range(len(adds))]

conn = sqlite3.connect('heyjobs.db')

cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS heyjobs (id INTEGER, uid STRING, title STRING);')

for item in title_and_uid_with_id:
    cur.execute('INSERT INTO heyjobs VALUES (?, ?, ?)', item)

# showing that the table heyjobs is now filled with the scraped information
cur.execute('SELECT * FROM heyjobs')
results = cur.fetchall()

print(results)
