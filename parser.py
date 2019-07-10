import pandas as pd
import requests
import time
import random


class parser:
    def parse(df, i):
        dob = df['DOB'][i]
        roll_no = df['REG NO'][i]
        a = dob.split('-')
        if a[1] == 'JAN':
            a[1] = '01'
        elif a[1] == 'FEB':
            a[1] = '02'
        elif a[1] == 'MAR':
            a[1] = '03'
        elif a[1] == 'APR':
            a[1] = '04'
        elif a[1] == 'MAY':
            a[1] = '05'
        elif a[1] == 'JUN':
            a[1] = '06'
        elif a[1] == 'JUL':
            a[1] = '07'
        elif a[1] == 'AUG':
            a[1] = '08'
        elif a[1] == 'SEP':
            a[1] = '09'
        elif a[1] == 'OCT':
            a[1] = '10'
        elif a[1] == 'NOV':
            a[1] = '11'
        elif a[1] == 'DEC':
            a[1] = '12'
        dob = a[0]+"-"+a[1]+"-19"+a[2]

        return (roll_no, dob)
