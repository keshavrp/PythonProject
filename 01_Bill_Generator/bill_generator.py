'''Python Program for the Bill Generator'''

import csv
import datetime
import time

SUM=0
ITEM_NUM=0
cart=[]

'''We are taking the input as customer name and customer mobile number'''

name=input('Enter the customer name:').title()
mobile='+91'+input('Enter the customer mobile number:')

'''Here we have created a dynamic file name using the first four letter 
of name + _ + first four digits of the mobile number'''

file_name=name[0:4]+'_'+mobile[3:7]

'''Here we have taken the current time stamp'''

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

'''We have setted the field for csv writer'''

field=[['Date','Customer Name', 'Mobile Number'],
       [f'{current_time} {datetime.date.today()}',f'{name}',f'{mobile}'],
       [' ',' ',' '],
       ['Item No','Item Name','Price(Rs.)']]

if len(mobile)==13:
    #Here we are writing csv file to set the field
    with open(f'{file_name}.csv', mode='a',encoding="utf8") as file:
        csvwriter3=csv.writer(file)
        csvwriter3.writerows(field)
    while True:
        #Here we are taking input item name and the price of item separated by comma
        item_name,price=map(str,input('Enter item,item price (q for exit):').split(','))

        if item_name != 'q':
            SUM+=int(price)
            ITEM_NUM+=1
            cart.append([f'{ITEM_NUM}',f'{item_name.title()}',int(price)])
            #Here we are appending the item number, item name and item price in the cart
            #.title() method works same as PROPER() method in excel
        else:
            with open(f'{file_name}.csv', mode='a',encoding="utf8") as file1:
                csvwriter1=csv.writer(file1)
                csvwriter1.writerows(cart)

            with open(f'{file_name}.csv', mode='a',encoding="utf8") as file2:
                csvwriter2=csv.writer(file2)
                csvwriter2.writerow(['Total Bill',' ',SUM])
            break
else:
    print('Mobile number should be of 10 digits.\n')