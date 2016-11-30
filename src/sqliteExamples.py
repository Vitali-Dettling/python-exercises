import pandas
import pandasql
import src.utility.FileManager as util

def print_result():
    # Execute your SQL command against the pandas frame
    rainy_days = pandasql.sqldf(q.lower(), globals())
    print(rainy_days)

'''
This function should run a SQL query on a dataframe of
weather data.

You can see the weather data that we are passing in below:
https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/weather_underground.csv

sqlite tutorials
https://www.tutorialspoint.com/sqlite/sqlite_date_time.htm
'''

url = 'https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/weather_underground.csv'
path = util.csv_writer_to_data(url, 'Weather')
weather_data = pandas.read_csv(path)


# The SQL query should return one column and one row - a count of the number of days in the dataframe where the rain column is equal to 1
q = """
SELECT sum(rain) as rain_sum
FROM weather_data
WHERE rain=1;
"""
print_result()



#  The SQL query should return two columns and two rows - whether it was foggy or not (0 or 1) and the max maxtempi for that fog value
q = '''
    SELECT fog, max(maxtempi) as max_temp
    FROM weather_data
    GROUP BY fog
'''
print_result()



# The SQL query should return one column and one row - the average meantempi on days that are a Saturday or Sunday
q='''
SELECT avg(cast(meantempi as integer)) as avg_mean_temp
FROM weather_data
WHERE cast(strftime('%w', date)as ibteger) = 0
OR cast(strftime('%w', date)as ibteger)  = 6
'''
print_result()



# More specifically you want to find the average minimum temperature (mintempi column of the weather dataframe) on rainy days where the minimum temperature is greater than 55 degrees.
q = '''
SELECT avg(cast(mintempi as integer)) as avg_min_temp
FROM  weather_data
WHERE rain = 1
AND mintempi > 55
'''
print_result()