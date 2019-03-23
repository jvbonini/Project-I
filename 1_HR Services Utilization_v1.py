  'I. HR Services Utilization
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
  'Yearly Count 
  # Get the total number of tickets by Year 
df_ticket_cl = df_ticket_cl.groupby('Creation Year')
number_of_tickets_per_year = df_ticket_cl['Company'].count()
tickets_per_year_df = pd.DataFrame(data = number_of_tickets_per_year,index = None).reset_index()
tickets_per_year_df = tickets_per_year_df.rename(columns = {"Creation Year":"Year","Company":"Total Number of Tickets"})
  # Print out in the window
print(tickets_per_year_df)
  # Tells matplotlib that we want to make a line graph
total_tickets_per_year_chart = number_of_tickets_per_year.plot(kind = "line",grid=True,marker='^',title = "Tickets per Year",figsize = (10.5))                                                                                                             
total_tickets_per_year_chart.set_xlabel("Year")
total_tickets_per_year_chart.set_ylabel("Total Ticket per Year")
plt.text(2018.5,250000,"There is an increase in the usage of HRServices. ",bbox=dict(facecolor='green',alpha =0.75))
  # Save Figure
plt.savefig("Images/1_Tickets_per_Year.png",bbox_inches = "tight")
  # Print out in the window
plt.show()

'-----------------------------------
  'Monthly count

    #  Month by month breakdown declare DataFrame
df_month = df_ticket_cl.loc[(df_ticket_cl["Ticket Year"] >= 2014) & (df_ticket_cl["Ticket Year"] <= 2018),:]
df_ticket_month = df_month['Ticket Month'].value_counts()
   # Print out in the window
print(df_ticket_month)8
  # Tells matplotlib that we want to make graph with months on X-axis and total number of tickets on Y-axis
  # Formatting  importing python library Calendar to convert from month index to a month name
import calendar
mn=[calendar.month_name[int(x)] for x in df_ticket_month.index.values.tolist()]
 #Add title, x axis label and y axis label.
ticket_chart = df_ticket_month.plot.bar(title = "Total Tickets per Month ",width = 0.75,figsize = (10,5),rot = 30,alpha = 0.75 )
ticket_chart.set_xticklabels(mn)
ticket_chart.set_xlabel("Tickets Months")
ticket_chart.set_ylabel("Total Tickets Count")
plt.text(12,100000,"The bars indicate ......",bbox=dict(facecolor='lightblue',alpha =0.5))
  # Save Figure
plt.savefig("Images/2_Tickets_per_Month.png")
  # Print out in the window
plt.show()

'-----------------------------------
  'Daily count

      # Slice dataframe by day of the week to find out the most popular day.
busy_day = df_ticket_cl['Ticket Day of Week'].value_counts()
    # Print out in the window
print(busy_day)
    # Add the legend
plt.xlabel = "Days of a week "
plt.ylabel = "Ticket count"
week_chart = busy_day.plot(kind = "bar" , title = " Busiest Day of the Week  ",width = 0.75,figsize = (10,5),rot = 30,alpha = 0.75)
plt.text(6.9,190000,"XXX is the most popular day of the week.",bbox=dict(facecolor='lightblue',alpha =0.5))
    # Save Figure
plt.savefig("Images/3_Busy_Week.png",bbox_inches = "tight")
     # Print out in the window
plt.show()

'-----------------------------------
  'Hourly Count

  # Declare dataframes for the busiest hour of the day 
busy_hour = df_service_cl['Ticket Hour'].value_counts()
   # Print out in the window
print(busy_hour)
   # Create the bar chart and add title, x axis label and y axis label.
hour_chart = busy_hour.plot(kind = "bar" , title = "Busiest Hour of the Day",width = 0.75,figsize = (13,5),rot = 0,alpha = 0.75)
hour_chart.set_xlabel("Hour of the Day")
hour_chart.set_ylabel("Ticket Count")
plt.text(24,80000,"xxxxxx are the peak hours.",bbox=dict(facecolor='Lightblue',alpha =0.5))
  # Save Figure
plt.savefig("4_Images/Busy_Hour.png",bbox_inches="tight")
  # Print out in the window
plt.show()

'-----------------------------------
  'Daily and Houly Count Combined

  # Create an array of the days of the week 
days_arr = ["Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Create function that returns the correct day of the week 
def get_day_of_week(x):
    return days_arr[x.weekday()]

# Use seaborn to create heat map 
df_heat = df_service_cl.groupby(["Ticket Hour", "Ticket Day of Week"])["Ticket ID"].size().reset_index()
df_heat2 = df_heat.pivot("Ticket Hour", "Ticket Day of Week", "Ticket ID")
fig, ax = plt.subplots(figsize=(10,8))       
sns.heatmap(df_heat2[days_arr] , cmap="YlOrRd")
plt.title("Total Number of Tickets by the Hour and Day of the Week.")

# Save heatmap image
plt.savefig("Images/4_Hours-day.png")
plt.show()

