#Code for 5 min interval with UDFs and added fields

import requests
import sched, time
import pandas as pd
import json
import urllib.parse
import json
from datetime import datetime
from datetime import timedelta
import time
import os
import shutil
import ast
import re

class Orders:
    url = ""
    payload=""
    header=""
    dat = ""

    def __init__(self):
        self.url="https://duroflex.vineretail.com/RestWS/api/eretail/v2/order/orderPullV2"
        #self.dat = input("Enter Start time in 24hr format: format -> DD/MM/YYYY HH:MM:SS (Example: 20/12/2021 14:00:00)")

       
        # ----------- Fetch Auth token ---------------------
        with open("D:/Duroflex-Uniware/token.txt","r") as token_file:
            self.token_string = json.loads(token_file.read())
        token_file.close()

        self.auth_token = self.token_string['access_token']
     
        # ----------- Fetch Auth token ---------------------

        # ----------- Define headers -----------------------
        self.headers = {
                    'Authorization': 'Bearer ' + self.auth_token,
                    'Content-Type': 'application/json'
                }
        # ----------- Define headers -----------------------        

        # ----------- Define start time, end time ---------- 
        current_date = datetime.now()
        self.start_date = current_date.replace(hour=00, minute=00, second=00)
        self.end_date = datetime.now()


        # ----------- Define start time, end time ---------- 

        # ----------- Define payload ------------------------- 

        self.payload = json.dumps({
                                    "fromDate": "{{self.start_date}}",
                                    "toDate": "{{self.end_date}}",
                                    "dateType": "UPDATED",
                                    "status": "Processing"
                                    })

        # ----------- Define payload ------------------------- 

        print (" ------------------------------------------ ")
        print (self.headers , "\n" , self.start_date , "\n" , self.end_date , "\n", self.payload)
        print (" ------------------------------------------ ")
        
obj = Orders()        


    