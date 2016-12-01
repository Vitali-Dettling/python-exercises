import os
import pandas

def csv_write_to_data(url, filename):

    path = '../data/' + filename + '.csv'
    if(path_exist(path, '.csv')):
        return(path)

    # Gets the data from an API and saves the data into a csv file.
    data = pandas.read_csv(url)
    pandas.DataFrame.to_csv(data, path)

    return(path)


def txt_write_to_data(url, filename):

    path = '../data/' + filename + '.txt'
    if(path_exist(path, '.txt')):
        return(path)

    # Gets the data from an API and saves the data into a txt file.
    data = pandas.read_csv(url)
    pandas.DataFrame.to_csv(data, path, header=None, index=None)

    return (path)

def txt_print_header(path, nlines):
    count = 0
    print('\n\n')
    with open(path) as f:
        for row in f:
            if (count >= nlines):
                break
            count += 1
            print(row)


def path_exist(path):
    # If the file already exists and is not empty.
    if(os.path.isfile(path) and os.path.getsize(path) > 0):
        return(True)
    return(False)
