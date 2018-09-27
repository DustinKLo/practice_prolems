from datetime import datetime
# import csv
import json
from itertools import groupby

from time_spent import time_spent_between_8pm_8am
# from pprint import pprint

'''
inout data structure:
    [
        ['6/01/2017 19:12:35','6/02/2017 09:12:35',34.0207654,-118.5008768],
        ...
    ]
'''
def process_data(data):
    START_DATE_IX = 0
    END_DATE_IX = 1
    LAT_IX = 2
    LNG_IX = 3
    DATE_FORMAT = '%m/%d/%Y %H:%M:%S'

    for row in data:
        # converting the timestamps to python datetime objects %m/%d/%Y %H:%M:%S
        start_date = datetime.strptime(row[START_DATE_IX], DATE_FORMAT)
        end_date = datetime.strptime(row[END_DATE_IX], DATE_FORMAT)

        row[LAT_IX] = round(row[LAT_IX], 3) # rounding to 3 decimal places
        row[LNG_IX] = round(row[LNG_IX], 3)
        
        row.append(time_spent_between_8pm_8am(start_date, end_date))

    max_minutes = 0
    home = None
    for key, group in groupby(data, lambda x: (x[2], x[3])):
        # grouping by each set of lat lng's
        group_minutes = 0
        for item in group:
            group_minutes += item[4] # summing the lat lng's total minutes

        if group_minutes > max_minutes: # setting the max 
            max_minutes = group_minutes
            home = list(key)
    
    return json.dumps({
            'latLng': home,
            'minutesSpent': max_minutes
        })



if __name__ == '__main__':
    test_data = [
        ['6/01/2017 19:12:35','6/02/2017 09:12:35',34.0207654,-118.5008768],
        ['6/02/2017 20:12:35','6/03/2017 06:12:35',34.020432,-118.5007432],
        ['6/03/2017 23:12:35','6/04/2017 07:12:35',34.020098,-118.500654],
        ['6/04/2017 21:12:35','6/05/2017 05:12:35',34.020123,-118.500765],
        ['6/05/2017 22:12:35','6/06/2017 08:12:35',34.020543,-118.500765],
        ['6/07/2017 00:12:35','6/07/2017 05:12:35',34.0207526,-118.5007654445],
        ['6/01/2017 06:12:35','6/01/2017 09:12:35',34.0402425,-118.5016543],
        ['6/02/2017 07:12:35','6/02/2017 06:12:35',34.0402425,-118.5016544],
        ['6/03/2017 06:12:35','6/03/2017 07:12:35',34.0402425,-118.5014324],
        ['6/04/2017 06:12:35','6/04/2017 07:12:35',34.0402425,-118.5014324],
        ['6/05/2017 07:12:35','6/05/2017 08:12:35',34.0402425,-118.501543],
        ['6/07/2017 06:12:35','6/07/2017 06:12:35',34.0402425,-118.5018768],
        ['6/01/2017 10:12:35','6/01/2017 19:05:35',34.0543,-118.391543],
        ['6/02/2017 10:12:35','6/02/2017 18:23:35',34.051465,-118.391543],
        ['6/03/2017 10:12:35','6/03/2017 17:34:35',34.0514432,-118.391543],
        ['6/04/2017 10:12:35','6/04/2017 18:45:35',34.051654,-118.391543],
        ['6/05/2017 10:12:35','6/05/2017 18:04:35',34.05165,-118.391543],
        ['6/07/2017 10:12:35','6/07/2017 19:07:35',34.05146565,-118.391543],
    ]

    print(process_data(test_data))


