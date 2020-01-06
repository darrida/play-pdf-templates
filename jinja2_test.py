

offer_amount_1 = 12000000

offer_amount_1 = '12000'
offer_amount_1 = int(offer_amount_1)
offer_amount_1 = '{:,.2f}'.format(offer_amount_1)

print(type(offer_amount_1))
print(offer_amount_1)

import csv
with open('offer_options.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for i in csv_reader:
        #print(i)
        if i[0] == '1':
            offer_bullets_1 = i[1:]
            print(offer_bullets_1)
        if i[0] == '2':
            offer_bullets_2 = i[1:]
            print(offer_bullets_2)
        if i[0] == '3':
            offer_bullets_3 = i[1:]
            print(offer_bullets_3)
    for dct in map(dict, csv_reader):
        print(dct)
        if dct['number']=='1':
            offer_amount_1 = '{:,.0f}'.format(int(dct['amount']))
            #print(offer_amount_1)
            #offer_bullets_1 = json.loads("['bullet 1', 'bullet 2', 'bullet 3', 'bullet 4', 'bullet 5', 'bullet 6', 'bullet 7']")#dct['bullets_list'])
            #print(offer_bullets_1)
        if dct['number']=='2':
            offer_amount_2 = '{:,.0f}'.format(int(dct['amount']))
            #offer_bullets_2 = json.loads(dct['bullets_list'])
        if dct['number']=='3':
            offer_amount_3 = '{:,.0f}'.format(int(dct['amount']))
            #offer_bullets_3 = json.loads(dct['bullets_list'])