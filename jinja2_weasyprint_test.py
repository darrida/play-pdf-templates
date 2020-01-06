import pandas as pd
import matplotlib.pyplot as plt
import csv
import json

interest_rates = [i*.01 for i in range(1,11)]
initial_account_sizes = [100, 500, 20000, 50000]
data_frames = []
for interest_rate in interest_rates:
    df = {}
    for initial_account_size in initial_account_sizes:
        df['Account Size: ' + str(initial_account_size)] = [initial_account_size * (1 + interest_rate) ** year for year in range(1, 21)]
    df = pd.DataFrame(df)
    df.index.name = 'year'
    data_frames.append({'df':df,
        'interest_rate':interest_rate})

df_test = df
df_test.hist()
plt.savefig('myfig2.png')

# IMPORT OFFER TYPE AND AMOUNT
with open('report_data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=";")
    for dct in map(dict, csv_reader):
        print(dct)
        if dct['number']=='1':
            offer_amount_1 = '{:,.0f}'.format(int(dct['amount']))
        if dct['number']=='2':
            offer_amount_2 = '{:,.0f}'.format(int(dct['amount']))
        if dct['number']=='3':
            offer_amount_3 = '{:,.0f}'.format(int(dct['amount']))

# IMPORT OFFER TYPE DEFINITIONS
with open('offer_options.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for i in csv_reader:
        #print(i)
        if i[0] == '1':
            offer_bullets_1 = i[2:]
            offer_number_1=i[1]
            print(offer_bullets_1)
        if i[0] == '2':
            offer_bullets_2 = i[2:]
            offer_number_2=i[1]
            print(offer_bullets_2)
        if i[0] == '3':
            offer_bullets_3 = i[2:]
            offer_number_3=i[1]
            print(offer_bullets_3)

# SETUP TEMPLATE
import jinja2
templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "jinja2_html.html"
template = templateEnv.get_template(TEMPLATE_FILE)

# OPEN TEMPLATE AND EMBED VARIABLES
for d in data_frames:
    outputText = template.render(df=d['df'],
            interest_rate=d['interest_rate'],
            offer_number_1=offer_number_1,
            offer_amount_1=offer_amount_1,
            offer_bullets_1=offer_bullets_1,
            offer_number_2=offer_number_2,
            offer_amount_2=offer_amount_2,
            offer_bullets_2=offer_bullets_2,
            offer_number_3=offer_number_3,
            offer_amount_3=offer_amount_3,
            offer_bullets_3=offer_bullets_3)
    html_file = open(str(int(d['interest_rate'] * 100)) + '.html', 'w')
    html_file.write(outputText)
    html_file.close()


#fig = plt.figure()
# create 2D array of table given above 
data = [['E001', 'M', 34, 123, 'Normal', 350], 
        ['E002', 'F', 40, 114, 'Overweight', 450], 
        ['E003', 'F', 37, 135, 'Obesity', 169], 
        ['E004', 'M', 30, 139, 'Underweight', 189], 
        ['E005', 'F', 44, 117, 'Underweight', 183], 
        ['E006', 'M', 36, 121, 'Normal', 80], 
        ['E007', 'M', 32, 133, 'Obesity', 166], 
        ['E008', 'F', 26, 140, 'Normal', 120], 
        ['E009', 'M', 32, 133, 'Normal', 75], 
        ['E010', 'M', 36, 133, 'Underweight', 40] ] 
  
# dataframe created with 
# the above data array 
df = pd.DataFrame(data, columns = ['EMPID', 'Gender',  
                                    'Age', 'Sales', 
                                    'BMI', 'Income'] ) 

# create histogram for numeric data 
df.hist() 
  
# save plot 
plt.savefig('myfig.png')

import weasyprint
continuing = True
for i in range(1,11):
    if continuing==True:
        weasyprint.HTML(str(i) + '.html').write_pdf(str(i) + '.pdf')
        continuing = False