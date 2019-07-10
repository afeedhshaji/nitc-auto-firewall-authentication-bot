from login import login
from parser import parser
import pandas as pd
import requests
import time
import random


class bot:
    obj_parser = parser()
    obj_login = login()

    def auto_log():
        file = "data.xlsx"
        df = pd.read_excel('data.xlsx', sheet_name='Export Worksheet')
        for i in range(2000, 4000):
            (roll_no, dob) = obj_parser.parse(df, i)
            logged_in = obj_login.login(roll_no, dob)
            if (logged_in):
                break

obj_bot = bot()
obj_bot.auto_log()
