import pandas
import pandasql
import src.utility.FileManager as util


'''
This function should run a SQL query on a dataframe of
weather data.

You can see the weather data that we are passing in below:
https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/weather_underground.csv

sqlite tutorials
https://www.tutorialspoint.com/sqlite/sqlite_date_time.htm
'''

url = 'https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/weather_underground.csv'
path = util.csv_write_to_data(url, 'Weather')
weather_data = pandas.read_csv(path)





# Execute your SQL command against the pandas frame
rainy_days = pandasql.sqldf(q.lower(), locals())
print(rainy_days)




