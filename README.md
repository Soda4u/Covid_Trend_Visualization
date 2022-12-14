# Covid_Trend_Visualization
This was a custom, practice project I wanted to do in order to visualize the trends of COVID-19 in 4 different states: CA, AZ, CO, and WA.
Organization of the dataset was done through SQLite, and analysis was done through Python.

Furthermore, Tableau was also used to create a second visualization, comparing the daily cases and deaths from each state overtime.  
Click [here](https://public.tableau.com/app/profile/ye.j.kim/viz/My_Covid_Trend_Visualization/Sheet1) to view the Tableau visualization on the Tableau website (an image of the visualization will also be available further down in this README file, Refer to Figure 2).   

The files in this repository include:
- "United_States_COVID-19_by_State.csv" is the original, raw data
- "Covid_Table_csv.csv" is the cleaned data in a csv format
- "Covid_Table_json.json" is the cleaned data in a json format
- "myDatabase.sqbpro" is the database file from DB Browser that holds all the information about SQLite Queries I wrote
- "Covid_Table_csv_Analysis.py" is the Python script I wrote in order to visualize the results of the data

----------


 **Below records the processes, mistakes, and lessons I've learned throughout the whole project.**


## Starting the Project
I first needed a credible source of data that compiled information about COVID-19 across the country.

Thankfully, the US Center for Disease Control has numerous public datasets available to the public, which is where I was able to download the data I needed
([source](https://data.cdc.gov/Case-Surveillance/United-States-COVID-19-Cases-and-Deaths-by-State-o/9mfq-cb36/data)).
An assumption at this step is that, being a government-owned source, the CDC database compiles accurate information about COVID-19 stats. In a real-world situation,
data mining would probably require a lot more attention and data profiling in order to ensure that the data is accurate and clean enough for analysis.
This dataset had information about the spread of COVID across the country from January 2020 to October 2022, which was perfect for me.
I downloaded the dataset as a csv file, and uploaded it onto my local database in DB Browser.


## Data Cleaning
Using SQLite, I wanted to clean up the table and query for the information I was analyzing.

The first step was to create a copy of the original raw data for cleaning, a good practice for data analysis. This was done through the CREATE TABLE statement,
copying over all the contents of the raw data onto a new table that I can freely manipulate and organize.It was a good thing that I created copy tables for cleaning,
because I made a couple mistakes on the way and had to revert back to the original dataset to start over.

I realized that the date format was recorded in a "MM/DD/YYYY" manner on the CDC table. Since the pandas python library, that I decided to use as part of the analysis,
does not recognize this date format, I wanted to change it into a "YYYY-MM-DD" format, which is the default date format used by pandas. Since SQL recognized this field
as a string, I was able to take the substrings of the date and organize the substrings in a way to create the desired date format. My first mistake was accidentally
swapping the day and month substrings. Inadvertently, I made a "YYYY-DD-MM" format, that I caught on later during analysis when I noticed that the "months" had values
13+. While fixing this mistake, I made another error by inadvertently running the substring script twice. This made the dates into an unrecognizable format. I started
all over and corrected all errors, resulting in the "Dates" column having dates stored as "YYYY-MM-DD" formats.

Although irrelevant to the final product, I wanted to practice with one of the most common problems for data analysts: handling missing values. Although different
solutions exist to address missing values, I decided to fill the null values with a string "N/A". I noticed that there were null values only on the records that had 
a null "conf_cases" value. I queried for records that ONLY had a "conf_cases" value, which turned out to be 0, meaning that all records that had null values
would have a "conf_cases" null value. This made things simpler, as I could query for records where "conf_cases" ISNULL, and used the IFNULL command to fill in those
values with "N/A".

I made a final table that queried for the information I wanted, which were: Dates, States, Total Cases, New Cases, Total Deaths, and New Deaths. They were ordered by
state, then submission date in order to create a table that separated the states first, and then in a time-series respective to each state.

This final table was then exported as a csv and json file, that could be uploaded onto VSCode for analysis.

## Data Visualization
Using VSCode, specifically with Python scripts, the data table derived from the previous step was visualized.

The organized and queried table in a csv file was imported onto VSCode. It was converted into a DataFrame through the pandas library "read_csv" function.

I used the "to_datetime" function to ensure that the dates field were converted into a date datatype, and verified that it was by checking the "dtypes" of the 
fields in the DataFrame.

Sub-DataFrames were created by using the "query" function, in order to separate the dataset by the 4 states of interest. Each of the 4 dataframes was  then plotted
using matplotlib.pyplot functions, with the x-axis being the date, and the y-axis being the number of new cases per capita (divided by the population of each state),
with each state being distinguished by a determined color. I noticed in the plot that the x-axis ticks were too cluttered, due to the sheer number of dates that the
dataset had. I was able to organize the dates by the autofmt_xdate() function, decreasing the number of ticks in the x-axis, allowing for a cleaner view.


## Insights
#### Figure 1: Covid Trend Visualization Created Through Python
![covid__trend_visualization](https://user-images.githubusercontent.com/69092102/208278539-981c5bbb-60f0-4542-807c-7c2bd053aa92.png)

Seeing the trend of Covid in each state per capita, it seems CA did a pretty fair job of battling covid during its early stages. However, it seems that something happened a little after January 2022 that caused daily covid cases to reach an all time high. Although this spike can be observed in all states, it is apparent that CA was affected the most. Looking back in the CDC's record of covid-related current events, January 2022 was when the Delta and Omicron variants were at the peak of their spread, bypassing previous vaccinations and reaching the highest rates of cases in many states ([source](https://www.cdc.gov/museum/timeline/covid19.html#Early-2022)). In that case, it makes sense why such a peak in daily new cases can be observed, but why CA was hit so much harder than the other states can be speculated.
Arizona seems to have consisntely high daily cases of covid per capita than the other 3 states.


#### Figure 2: Covid Cases vs Deaths Created Through Tableau
![Daily_Cases_vs_Deaths](https://user-images.githubusercontent.com/69092102/208278786-6ffb28fb-cc15-4bbd-8e7a-af88e0abe9d8.png)

It should be immediately noted that this visualization was created on raw values, NOT on a per-capita basis like the previous visualization was. This is because I wanted to see the raw values of the cases in relation to the number of deaths in each state. For that reason, since CA has a significantly higher population compared to the other 3 states, it was inevitable that the CA trend for both cases and deaths were higher than the other states.   
As noted in the description for Figure 1, there is a large peak of new covid cases around January 2022 due to the spread of the Delta and Omicron variants. However, even though the highest peak of the covid cases can be observed during that time, it's apparent that there are not a lot of deaths. The highest peak of deaths seem to happen during the early stages of covid, around January 2021, and mellow down over time. January 2021 was a time where the general public of the US did not have access to the covid vaccine yet, which may explain why there were so many deaths. That may also explain why the number of deaths trend down into a more consistently low number after covid vaccines became more accessible to the general public.
