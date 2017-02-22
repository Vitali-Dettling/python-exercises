import os
import pandas

def csv_writer_to_data(url, filename):

    path = '../Statistic/data/' + filename + '.csv'
    if(path_exist(path, '.csv')):
        return(path)

    # Gets the data from an API and saves the data into a csv file.
    data = pandas.read_csv(url)
    pandas.DataFrame.to_csv(data, path)

    return(path)


def txt_write_to_data(url, filename):

    path = '../Statistic/data/' + filename + '.txt'
    if(path_exist(path, '.txt')):
        return(path)

    # Gets the data from an API and saves the data into a txt file.
    data = pandas.read_csv(url)
    pandas.DataFrame.to_csv(data, path, header=None, index=None)

    return (path)

def txt_print_header(path, nlines):
    N = nlines
    count = 0
    with open(path) as f:
        for row in f:
            if (count >= N):
                break
            count += 1
            print(row)


def path_exist(path, extension):
    # If the file already exists and is not empty.
    path_ext = path + extension
    if(os.path.isfile(path_ext) and os.path.getsize(path_ext) > 0):
        return(True)
