#!/usr/bin/python

""" Task 1
In 1973, the University of California-Berkeley (UC-Berkeley) was sued for sex discrimination. Its admission data showed that men applying to graduate school at UC-Berkley were more likely to be admitted than women.

The graduate schools had just accepted 44% of male applicants but only 35% of female applicants. The difference was so great that it was unlikely to be due to chance.

By looking at the data more closely, you may realize that there is more to the story than meets the eye.
"""

# External
import csv
import urllib.request as down
import numpy as np
# python3-tk need to be installed first, in order to install matplotlib, via apt-get install python3-tk
import matplotlib.pyplot as plt

# Manual
import src.utility as utility


url = 'http://www.calvin.edu/~stob/data/Berkeley.csv'

local_filename, headers = down.urlretrieve(url)
cr = csv.reader(local_filename)

utility.display_table_csv( local_filename )

sum_male_admitted = 0
sum_male_rejected = 0

sum_female_admitted = 0
sum_female_rejected = 0

with open(local_filename) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if(row['Gender'] == 'Male'):
            if(row['Admit'] == 'Admitted'):
                sum_male_admitted = sum_male_admitted + int(row['Freq'])
            elif(row['Admit'] == 'Rejected'):
                sum_male_rejected = sum_male_rejected + int(row['Freq'])
        elif(row['Gender'] == 'Female'):
            if (row['Admit'] == 'Admitted'):
                sum_female_admitted = sum_female_admitted + int(row['Freq'])
            elif (row['Admit'] == 'Rejected'):
                sum_female_rejected = sum_female_rejected + int(row['Freq'])


male_result = sum_male_rejected - sum_male_admitted
femal_result = sum_female_rejected - sum_female_admitted

print('\nMale application admitted: ' + str(male_result) + ' \nSum of all male applications:' , (sum_male_rejected + sum_male_admitted))
print('Female applications admitted: ' + str(femal_result) + ' \nSumm of all female applications: ' , (sum_female_rejected + sum_female_admitted))

divided_male = male_result / (sum_male_rejected + sum_male_admitted)
divided_female = femal_result / (sum_female_rejected + sum_female_admitted)

print('\nPercent (%.2f) of male:' % divided_male)
print('Percent (%.2f) of female: ' % divided_female)

""" Conclusion
According to the data more male application were accepted, but fewer were accually permitted.
In contrary to the femal applications. Fewer application were accepted but more female student were allowed to enter the university.
"""