#Code for 5 min interval with UDFs and added fields

import requests
import sched, time
import pandas as pd
import json
import urllib.parse
import json
from datetime import datetime
from datetime import timedelta
import os
import shutil
import ast
import re

class genAuthToken:
    url = ""
    payload=""
    header=""
    
    def __init__(self):
        self.auth_url="https://sleepyhead.unicommerce.com/oauth/token?grant_type=password&client_id=my-trusted-client&username=analytics@mysleepyhead.com&password=Unisleepy@123"
        
        self.headers = {}    
        payload = {}

    def gen_token(self):
        response = requests.request("GET", self.auth_url, headers=self.headers, data=self.payload)

        print(response.text)
        with open("D:/Duroflex-Uniware/token.txt","a") as token_file:
            token_file.write(response.text)
        token_file.close()

obj = genAuthToken()
obj.gen_token()
        

