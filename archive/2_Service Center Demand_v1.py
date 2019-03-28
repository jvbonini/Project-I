  'II.  Service Center Demand
'-----------------------------------
 'Dependencies and Setup
 
  # Importing library
%matplotlib inline

  # Importing external packages
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

  # File to Load 
ticket_data = "Resources//ticket_data.csv"

  # Read the Ticket file and store Pandas data frame
df_ticket_cl = pd.read_csv(ticket_data)
#ticket_data_df = ticket_data_df.drop_duplicates('city')
   # Print out in the window
df_ticket_cl.head()

'-----------------------------------
  'Service Center Demand (by location)
 
# The focus of this analysis, is ticket usage by service location
# Again, value_counts() is leveraged to find unique row count by service location
popular_Service_location = df_ticket_cl['Service location'].value_counts()
popular_Service_location.sort_values(ascending = False).head(6)

# Plot covers the top 6 service locations that potray more usage than other locations
pop_location_chart = popular_Service_location[0:6].plot(kind = "barh",width = 0.75,figsize = (13,5),alpha = 0.75)
plt.title("Top 6 Service locations")
plt.text(300,6.5,"The locations below receive the most tickets",bbox=dict(facecolor='Lightblue',alpha =0.5) )
plt.savefig("Images/5_pop_location.png",bbox_inches = "tight")
plt.show()

'-----------------------------------
  'Service Center Demand (by category)

  # Analysis by Tickets Types helps determine which programs are popular. 
popular_category_type = df_ticket_cl['Ticket Category Type'].value_counts() 
print(popular_category_type.head(10))

# plot the graph for the popular mebership types 
explode = (0.1,0,0,0,0,0)
colors = ["gold", "lightskyblue", "lightcoral","lightgreen","orange","plum"]
popular_category_type[0:6].plot.pie(colors = colors , explode = explode, shadow=True )
plt.title("Top 5 Ticket Category Types")
plt.savefig("Images/6_ticket_type.png",bbox_inches = "tight")
plt.show()


'-----------------------------------
  'Average Ticket Duration (by Service Center Category)

  # For each category type in the Top 5, prepare a data series with ticket durations
# Find the average for each category type
subscriber_type = df_ticket_cl['Ticket Category Type'].value_counts().index
top_subscriber_type = subscriber_type[0:6]

ticket_minutes = []
for element in top_subscriber_type:
  time_min = df_ticket_cl[df_ticket_cl['Ticket Category Type'] == element]['Ticket Duration Minutes'].values
  ticket_minutes.append(np.mean(time_min))

x_axis  =  np.arange(0, len(top_subscriber_type))
tick_locations = []
for x in x_axis:
  tick_locations.append(x)

ticket_minutes.sort(reverse=True)
plt.xticks(tick_locations, ["month","year"..], rotation=90)
colors = ["gold", "lightgreen","plum","lightcoral","orange","lightskyblue"]
plt.bar(height= ticket_minutes, x= tick_locations, color=colors,alpha = 0.75)
plt.title('Average Ticket Duration by Top Ticket Category Type')
plt.savefig("Images/7_avg_duration_mem_type.png",bbox_inches = "tight")
plt.show()

'-----------------------------------
  'Average Ticket Duration Over the Years (by Service Center Category)

# For each year, filter the data into a data frame.
# For that data frame, for the above selected top 5 category types 
# Calculate the average duration of tickets
fig, ax = plt.subplots(figsize=(20, 10))
title_font = {'fontname':'Arial', 'size':'20', 'color':'black', 'weight':'normal',
              'verticalalignment':'bottom'} # Bottom vertical alignment for more space
axis_font = {'fontname':'Arial', 'size':'20'}
w = 0.2
subscriber_type = df_ticket_cl['Ticket Category Type'].value_counts().index
top_subscriber_type = subscriber_type[0:6]

## For 2018
df_ticket_2018 = df_ticket_cl.loc[(df_ticket_cl["Ticket Year"] ==2018)]

ticket_minutes_2018 = []
for element in top_subscriber_type:
   time_min = df_ticket_2018[df_ticket_2018['Ticket Category Type'] == element]['Ticket Duration Minutes'].values
   ticket_minutes_2018.append(np.mean(time_min))

## For 2017

df_ticket_2017 = df_ticket_cl.loc[(df_ticket_cl["Ticket Year"] ==2017)]

ticket_minutes_2017 = []
for element in top_subscriber_type:
   time_min = df_ticket_2017[df_ticket_2017['Ticket Category Type'] == element]['Ticket Duration Minutes'].values
   ticket_minutes_2017.append(np.mean(time_min))

## For 2016

df_ticket_2016 = df_ticket_cl.loc[(df_ticket_cl["Ticket Year"] ==2016)]

ticket_minutes_2016 = []
for element in top_subscriber_type:
   time_min = df_ticket_2016[df_ticket_2016['Ticket Category Type'] == element]['Ticket Duration Minutes'].values
   ticket_minutes_2016.append(np.mean(time_min))

## For 2015

df_ticket_2015 = df_ticket_cl.loc[(df_ticket_cl["Ticket Year"] ==2015)]

ticket_minutes_2015 = []
for element in top_subscriber_type:
   time_min = df_ticket_2015[df_ticket_2015['Ticket Category Type'] == element]['Ticket Duration Minutes'].values
   ticket_minutes_2015.append(np.mean(time_min))

## For 2014

df_ticket_2014 = df_ticket_cl.loc[(df_ticket_cl["Ticket Year"] ==2014)]

ticket_minutes_2014 = []
for element in top_subscriber_type:
   time_min = df_ticket_2014[df_ticket_2014['Ticket Category Type'] == element]['Ticket Duration Minutes'].values
   ticket_minutes_2014.append(np.mean(time_min))


x_axis  =  np.arange(0, len(top_subscriber_type))
tick_locations = []
for x in x_axis:
   tick_locations.append(x)

# Plot with category types on X-axis and Minutes on Y-axis and stacked by year.
plt.setp(ax, xticks= tick_locations, xticklabels= top_subscriber_type)
plt.setp(ax.get_xticklabels(), rotation=70, fontsize= 20)
ax.bar(x_axis-0.5*w, ticket_minutes_2018,w,color='r',label='2018',alpha = 0.75)
ax.bar(x_axis, ticket_minutes_2017,w,color='g',label='2017',alpha = 0.75)
ax.bar(x_axis+0.5*w, ticket_minutes_2016,w,color='b',label='2016',alpha = 0.75)
ax.bar(x_axis+1*w, ticket_minutes_2015,w,color='y',label='2015',alpha = 0.75)
ax.bar(x_axis+1.5*w, ticket_minutes_2014,w,color='c',label='2014',alpha = 0.75)
ax.bar(x_axis+2*w, ticket_minutes_2013,w,color='m',label='2013',alpha = 0.75)

ax.set_title('Average Ticket Duration by Top Ticket Category Type (over the years)', **title_font)
ax.set_ylabel('Minutes', **axis_font)
ax.legend(loc=1, prop={'size': 16})
plt.savefig("Images/8_avg_duration_mem_type_year.png",bbox_inches = "tight")
plt.show()



