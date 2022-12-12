#Import the needed libraries
import pandas as pd
import matplotlib.pyplot as plt

#Create a dataframe by reading the csv file exported from SQL
df = pd.read_csv('Covid_Table_csv.csv')
df['Date'] = pd.to_datetime(df['Date'], format = '%Y-%m-%d')

#Confirming the dtypes of each field in the DataFrame
#print(df.dtypes)

#Separate the graphs based on States. In this case, separated by 4 states: AZ, CA, CO, and WA
df_AZ = df.query("State =='AZ'")
df_CA = df.query("State == 'CA'")
df_CO = df.query("State =='CO'")
df_WA = df.query("State =='WA'")

#Define the variable that will be used to visualize the y axis (x-axis will be Date)
y = 'New_Cases'

#plot the graphs of the Dataframes created of each state
fig, ax = plt.subplots()

#Population or each state, in order to analyze the trend of new cases per capita. Raw values could be added to each
#respective plot, but for transparency, the values will be presented as variables. 
#Each population value is x1,000,000
CA_pop = 39.2
CO_pop = 5.8
AZ_pop = 7.4
WA_pop = 7.8

plt.plot(df_CA['Date'],df_CA[y]/CA_pop, label = 'CA_Cases', color = 'blue')
plt.plot(df_CO['Date'],df_CO[y]/CO_pop, label = 'CO_Cases', color = 'red')
plt.plot(df_AZ['Date'],df_AZ[y]/AZ_pop, label = 'AZ_Cases', color = 'orange')
plt.plot(df_WA['Date'],df_WA[y]/WA_pop, label = 'WA_Cases', color = 'green')


#Organizing the format of the X-axis to reduce number of ticks
ax.xaxis_date()
fig.autofmt_xdate()

#Organizing the plot to present necesary information
plt.xlabel("Date")
plt.ylabel("New Cases per Capita")
plt.title("Visualization of New Covid Cases per Capita")
plt.legend()
plt.show()


