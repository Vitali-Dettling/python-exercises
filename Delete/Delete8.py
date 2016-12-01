import pandas

def add_full_name(path_to_csv, path_to_new_csv):
    #Assume you will be reading in a csv file with the same columns that the
    #Lahman baseball data set has -- most importantly, there are columns
    #called 'nameFirst' and 'nameLast'.
    #1) Write a function that reads a csv
    #located at "path_to_csv" into a pandas dataframe and adds a new column
    #called 'nameFull' with a player's full name.
    #
    #For example:
    #   for Hank Aaron, nameFull would be 'Hank Aaron',
	#
	#2) Write the data in the pandas dataFrame to a new csv file located at
	#path_to_new_csv

    data = pandas.read_csv(path_to_csv)
    df = pandas.DataFrame(data)

    df_first_aname = df['nameFirst']
    df_last_name = df['nameLast']

    concatenate_names = df_first_aname + ' ' + df_last_name
    df['nameFull'] = pandas.Series(concatenate_names, index=df.index)

    df.to_csv(path_to_new_csv)



if __name__ == "__main__":
    # For local use only
    # If you are running this on your own machine add the path to the
    # Lahman baseball csv and a path for the new csv.
    # The dataset can be downloaded from this website: http://www.seanlahman.com/baseball-archive/statistics
    # We are using the file Master.csv
    path_to_csv = "External/baseballdatabank-master/core/Master.csv"
    path_to_new_csv = "External/New_Master.csv"
    add_full_name(path_to_csv, path_to_new_csv)


