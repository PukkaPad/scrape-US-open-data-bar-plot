#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import the classes that are needed
import urllib2
from bs4 import BeautifulSoup
import sqlite3
import itertools

td_listDemo = []
td_listRisk = []
td_listIncid = []
td_listPrev = []
td_listMort = []

# URL to scrape and open it with the urllib2
page = urllib2.urlopen("https://statecancerprofiles.cancer.gov/quick-profiles/index.php?statename=florida#t=0")

# Turn source into a BeautifulSoup object
soup = BeautifulSoup(page, "html.parser")

# From the source HTML page, search and store all <div id="demo">...</div> and it's content
demoDiv = soup.findAll('div', { "id" : "demo" })
#print demoDiv

for table in demoDiv:
    
    tableTags = table.find_all("td")
    
    for td in tableTags:

        td_text = td.get_text()

        td_listDemo.append(td_text)


# From the source HTML page, search and store all <div id="risk">...</div> and it's content
riskDiv = soup.findAll('div', { "id" : "incd" })
#print demoDiv

for table in riskDiv:
    
    tableTags = table.find_all("td")
    
    for td in tableTags:

        td_text = td.get_text()

        td_listRisk.append(td_text)



# From the source HTML page, search and store all <div id="incd">...</div> and it's content
incidDiv = soup.findAll('div', { "id" : "incd" })
#print demoDiv

for table in incidDiv:
    
    tableTags = table.find_all("td")
    
    for td in tableTags:

        td_text = td.get_text()

        td_listIncid.append(td_text)


# From the source HTML page, search and store all <div id="prev">...</div> and it's content
prevDiv = soup.findAll('div', { "id" : "prev" })
#print demoDiv

for table in prevDiv:
    
    tableTags = table.find_all("td")
    
    for td in tableTags:

        td_text = td.get_text()

        td_listPrev.append(td_text)

# From the source HTML page, search and store all <div id="mort">...</div> and it's content
mortDiv = soup.findAll('div', { "id" : "mort" })
#print demoDiv

for table in mortDiv:
    
    tableTags = table.find_all("td")
    
    for td in tableTags:

        td_text = td.get_text()

        td_listMort.append(td_text)


# doing this I get all the lables - Demographycs Columns
array1D = [td_listDemo[i] for i in xrange(0, len(td_listDemo), 5)]
array1R = [td_listRisk[i] for i in xrange(0, len(td_listRisk), 5)]
array1I = [td_listIncid[i] for i in xrange(0, len(td_listIncid), 7)]
array1P = [td_listPrev[i] for i in xrange(0, len(td_listPrev), 4)]
array1M = [td_listMort[i] for i in xrange(0, len(td_listMort), 9)]


# get Florida info column
array2D = [td_listDemo[i] for i in xrange(1, len(td_listDemo), 5)]
array2R = [td_listRisk[i] for i in xrange(1, len(td_listRisk), 5)]
array2I = [td_listIncid[i] for i in xrange(1, len(td_listIncid), 7)]
array2P = [td_listPrev[i] for i in xrange(1, len(td_listPrev), 4)]
array2M = [td_listMort[i] for i in xrange(1, len(td_listMort), 9)]


# get USA info column
array3D = [td_listDemo[i] for i in xrange(2, len(td_listDemo), 5)]
array3R = [td_listRisk[i] for i in xrange(2, len(td_listRisk), 5)]
array3I = [td_listIncid[i] for i in xrange(2, len(td_listIncid), 7)]
array3P = [td_listPrev[i] for i in xrange(2, len(td_listPrev), 4)]
array3M = [td_listMort[i] for i in xrange(2, len(td_listMort), 9)]



# add arrays to database

conn = sqlite3.connect('Florida.db')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS Demographics;
DROP TABLE IF EXISTS Screening_RiskFactors;
DROP TABLE IF EXISTS Incidence;
DROP TABLE IF EXISTS Prevalence;
DROP TABLE IF EXISTS Mortality;


CREATE TABLE Demographics (
    Label TEXT, Florida_Percent INTEGER, USA_Percent INTEGER
    );

CREATE TABLE Screening_RiskFactors (
    Label TEXT, Florida INTEGER, USA INTEGER
    );

CREATE TABLE Incidence (
    Label TEXT, Florida_Rate INTEGER, USA_Rate INTEGER
    );

CREATE TABLE Prevalence (
    Label TEXT, Florida INTEGER, USA INTEGER
    );

CREATE TABLE Mortality (
    Label TEXT, Florida_Rate INTEGER, USA_Rate INTEGER
    )

''')



for item1D, item2D, item3D in zip(array1D, array2D, array3D):
    conn.execute('''INSERT OR IGNORE INTO Demographics (Label, Florida_Percent, USA_Percent) VALUES (?,?, ?)''', (item1D,item2D,item3D,)) 

for item1R, item2R, item3R in zip(array1R, array2R, array3R):
    conn.execute('''INSERT OR IGNORE INTO Screening_RiskFactors (Label, Florida, USA) VALUES (?,?, ?)''', (item1R,item2R,item3R,)) 

for item1I, item2I, item3I in zip(array1I, array2I, array3I):
    conn.execute('''INSERT OR IGNORE INTO Incidence (Label, Florida_Rate, USA_Rate) VALUES (?,?, ?)''', (item1I,item2I,item3I,)) 

for item1P, item2P, item3P in zip(array1P, array2P, array3P):
    conn.execute('''INSERT OR IGNORE INTO Prevalence (Label, Florida, USA) VALUES (?,?, ?)''', (item1P,item2P,item3P,)) 

for item1M, item2M, item3M in zip(array1M, array2M, array3M):
    conn.execute('''INSERT OR IGNORE INTO Mortality (Label, Florida_Rate, USA_Rate) VALUES (?,?, ?)''', (item1M,item2M,item3M,)) 

conn.commit()
print("Records Created Successfully")

conn.close()
