#!/usr/bin/python

import sqlite3
import urllib2
import unicodedata
from BeautifulSoup import BeautifulSoup

source = 'https://www.heyjobs.de/en/jobs-in-berlin'
soup = BeautifulSoup(urllib2.urlopen(source).read())

links = soup.findAll('a')
adds = [x for x in links if x.get('href') != None and '/en/jobs' in x.get('href')]

title_and_uid_with_id = [(x,
                         unicodedata.normalize('NFKD', adds[x].div.div.div.nextSibling.string).encode('ascii','ignore'),
                         adds[x]['href'].split('/')[-1]) 
                         for x in range(len(adds))]

conn = sqlite3.connect('/Users/elise/Desktop/database.db')
cur = conn.cursor()
cur.execute('CREATE TABLE heyjobs (id INTEGER, uid STRING, title STRING);')

for item in title_and_uid_with_id:
    cur.execute('INSERT INTO heyjobs VALUES (?, ?, ?)', item)

cur.execute('SELECT * FROM heyjobs')
results = cur.fetchall()
print results