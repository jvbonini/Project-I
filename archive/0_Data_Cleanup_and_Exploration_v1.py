  'PyHR Services Data Cleanup and Exploration
'-----------------------------------  
  'Introduction
'-----------------------------------
  'Data Extraction
'-----------------------------------
  'Import Dependencies

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import csv
import requests

'-----------------------------------

  # File to Load 
ticket_data = "Resources//ticket_data.csv"
  # Read the Ticket file and store Pandas data frame
df_ticket = pd.read_csv(ticket_data)
   # Print out in the window
df_ticket.head()

'-----------------------------------
  'Initial Data Exploration

   'On an initial exploration of the data... 

I   # Count rows and columns 
    # Check for missing values 
    # Check  last values of our dataframe are missing the month and year
    # Count how many rows are missing 
    # Create summary table of the missing values 

'-----------------------------------
  'Initial Data Clean Up

   'In this section..

    # Checkthe Closing Date and extract the Month, Year, and Day of the Week 
    # Inspect the filled in values 
    # Split the hour 
    # Inspect the filled in values 
    # Check for missing values 
    # Verify Data types

'-----------------------------------
  'Reorganized and Updated Data Frame

     # Export to csv