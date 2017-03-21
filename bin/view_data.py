import pandas as pd
from IPython.display import display
import sqlite3
import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap


#plt.rcdefaults()

import plotly.plotly as py # interactive graphing
from plotly.graph_objs import Bar, Scatter, Marker, Layout

# This makes the figure's width 20 inches, and its height 10 inches
from pylab import rcParams
rcParams['figure.figsize'] = 15, 10

# Create your connection.
cnx = sqlite3.connect('Florida.db')

#df = pd.read_sql_query("SELECT * FROM Mortality", cnx)

fig = plt.figure()
ax = fig.add_subplot(111)
width=0.35

df = pd.read_sql_query("SELECT Label, Florida_Rate FROM Mortality", cnx)[1:22]
dg = pd.read_sql_query("SELECT Label, USA_Rate FROM Mortality", cnx)[1:22]

y_pos = np.arange(len(df.Label))
#print df.Florida_Rate

plt.bar(y_pos,df.Florida_Rate, width,color='g', label="Florida")

plt.bar(y_pos+width,dg.USA_Rate, width,color='r')

plt.title('Age-Adjusted Mortality Rates by Cancer Site (2009-2013)')

df.Label = [ '\n'.join(wrap(l, 10)) for l in df.Label ]

plt.xticks(y_pos + width, df.Label, rotation=45, fontsize=10, ha='center')

plt.legend(  ('Florida', 'USA'))
plt.tight_layout(1)

fig.savefig('MortalityRate.pdf', orientation = 'portrait', bbox_inches='tight')

plt.show()

#new plot: Race
fig = plt.figure()
ax = fig.add_subplot(111)
width=0.35

df = pd.read_sql_query("SELECT Label, Florida_Rate FROM Mortality", cnx)[23:30]
dg = pd.read_sql_query("SELECT Label, USA_Rate FROM Mortality", cnx)[23:30]

y_pos = np.arange(len(df.Label))
#print df.Florida_Rate

plt.bar(y_pos,df.Florida_Rate, width,color='g', label="Florida")

plt.bar(y_pos+width,dg.USA_Rate, width,color='r')

plt.title('Age-Adjusted Mortality Rates by Race/Ethnicity (2009-2013)')

df.Label = [ '\n'.join(wrap(l, 10)) for l in df.Label ]

plt.xticks(y_pos + width, df.Label, rotation=45, fontsize=10, ha='center')

plt.legend(  ('Florida', 'USA'))
plt.tight_layout(1)

fig.savefig('MortalityRate_race.pdf', orientation = 'portrait', bbox_inches='tight')

plt.show()

#new plot: Gender
fig = plt.figure()
ax = fig.add_subplot(111)
width=0.35

df = pd.read_sql_query("SELECT Label, Florida_Rate FROM Mortality", cnx)[31:33]
dg = pd.read_sql_query("SELECT Label, USA_Rate FROM Mortality", cnx)[31:33]

y_pos = np.arange(len(df.Label))
#print df.Florida_Rate

plt.bar(y_pos,df.Florida_Rate, width,color='g', label="Florida")

plt.bar(y_pos+width,dg.USA_Rate, width,color='r')

plt.title('Age-Adjusted Mortality Rates by Sex (2009-2013)')

df.Label = [ '\n'.join(wrap(l, 10)) for l in df.Label ]

plt.xticks(y_pos + width, df.Label, rotation=45, fontsize=10, ha='center')

plt.legend(  ('Florida', 'USA'))
plt.tight_layout(1)

fig.savefig('MortalityRate_sex.pdf', orientation = 'portrait', bbox_inches='tight')

plt.show()

#new plot: Age
fig = plt.figure()
ax = fig.add_subplot(111)
width=0.35

df = pd.read_sql_query("SELECT Label, Florida_Rate FROM Mortality", cnx)[34:38]
dg = pd.read_sql_query("SELECT Label, USA_Rate FROM Mortality", cnx)[34:38]

y_pos = np.arange(len(df.Label))
#print df.Florida_Rate

plt.bar(y_pos,df.Florida_Rate, width,color='g', label="Florida")

plt.bar(y_pos+width,dg.USA_Rate, width,color='r')

plt.title('Age-Adjusted Mortality Rates by Age (2009-2013)')

df.Label = [ '\n'.join(wrap(l, 10)) for l in df.Label ]

plt.xticks(y_pos + width, df.Label, rotation=45, fontsize=10, ha='center')

plt.legend(  ('Florida', 'USA'))
plt.tight_layout(1)

fig.savefig('MortalityRate_age.pdf', orientation = 'portrait', bbox_inches='tight')

plt.show()

#new plot: Year
fig = plt.figure()
ax = fig.add_subplot(111)
width=0.35

df = pd.read_sql_query("SELECT Label, Florida_Rate FROM Mortality", cnx)[38:40]
dg = pd.read_sql_query("SELECT Label, USA_Rate FROM Mortality", cnx)[38:40]

y_pos = np.arange(len(df.Label))
#print df.Florida_Rate

plt.bar(y_pos,df.Florida_Rate, width,color='g', label="Florida")

plt.bar(y_pos+width,dg.USA_Rate, width,color='r')

plt.title('Age-Adjusted Mortality Rates by Year')

df.Label = [ '\n'.join(wrap(l, 10)) for l in df.Label ]

plt.xticks(y_pos + width, df.Label, rotation=45, fontsize=10, ha='center')

plt.legend(  ('Florida', 'USA'))
plt.tight_layout(1)

fig.savefig('MortalityRate_year.pdf', orientation = 'portrait', bbox_inches='tight')

plt.show()