import os
import pandas

def csv_writer_to_data(url, filename):

    path = '../data/' + filename + '.csv'
    if(path_exist(path, '.csv')):
        return(path)

    # Gets the data from an API and saves the data into a csv file.
    data = pandas.read_csv(url)
    pandas.DataFrame.to_csv(data, path)

    return(path)


def txt_write_to_data(url, filename):

    path = '../data/' + filename + '.txt'
    if(os.path.isfile(path) and os.path.getsize(path) > 0):
        return(path)


    # Gets the data from an API and saves the data into a csv file.
    data = pandas.read_csv(url, header=False, index=False)
    pandas.DataFrame.to_csv(data, path, header=False, index=False)

    return (path)


def path_exist(path, extension):
    # If the file already exists and is not empty.
    path_ext = path + extension
    if(os.path.isfile(path_ext) and os.path.getsize(path_ext) > 0):
        return(True)


