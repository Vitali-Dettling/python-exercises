#!/usr/bin/python

""" Task 1.0
In 1973, the University of California-Berkeley (UC-Berkeley) was sued for sex discrimination. Its admission data showed that men applying to graduate school at UC-Berkley were more likely to be admitted than women.

The graduate schools had just accepted 44% of male applicants but only 35% of female applicants. The difference was so great that it was unlikely to be due to chance.

By looking at the data more closely, you may realize that there is more to the story than meets the eye.
"""

import urllib.request as down
import matplotlib.pyplot as plt
import pandas as pd

# Download the csv file
# url = 'http://www.calvin.edu/~stob/data/Berkeley.csv'
# local_filename, headers = down.urlretrieve(url)
# df = pd.DataFrame(pd.read_csv(local_filename))

data = pd.read_csv('../Statistic/data/Berkeley.csv')
df = pd.DataFrame(data)
print(df)

gender_male = df['Gender'] == 'Male'
gender_female = df['Gender'] == 'Female'

admit_admitted = df['Admit'] == 'Admitted'
admit_rejected = df['Admit'] == 'Rejected'

# Sum all male together which are admitted.
sum_male_admitted = df[gender_male & admit_admitted]['Freq'].sum()

# Sum all male together which are rejected.
sum_male_rejected = df[gender_male & admit_rejected]['Freq'].sum()

# Sum all female which are admitted
sum_female_admitted = df[gender_female & admit_admitted]['Freq'].sum()

# Sum all female which are rejected
sum_female_rejected = df[gender_female & admit_rejected]['Freq'].sum()

# Count all together
total_male = sum_male_admitted + sum_male_rejected
total_female = sum_female_admitted + sum_female_rejected

# To verify the display results.
percent_male_admitted = (sum_male_admitted / total_male) *100
percent_male_rejected = (sum_male_rejected / total_male) * 100
percent_female_admitted = (sum_female_admitted / total_female) *100
percent_female_rejected = (sum_female_rejected / total_female) *100

print(percent_male_admitted)
print(percent_male_rejected)
print(percent_female_admitted)
print(percent_female_rejected)

# plot of results
# http://pandas.pydata.org/pandas-docs/version/0.18.1/visualization.html
data = [[sum_male_admitted, sum_female_admitted],[sum_male_rejected, sum_female_rejected]]
df_plot = pd.DataFrame(data, index=['Admitted', 'Rejected'], columns=['Male', 'Female'])
df_plot.plot.pie(subplots=True, figsize=(8, 4), autopct='%.0f', fontsize=12, legend=False)
plt.show()

