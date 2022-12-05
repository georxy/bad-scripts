import csv
import re
from urllib.request import Request, urlopen
import pandas as pd
import api_keys as ak
import check_blog as cbg


#  Email scrapper + hunter.io
api_key = ak.hunter_api
desktop = ak.desktop


def email_io(fName):
    output = []
    file_test = desktop + "/" + fName + ".csv"
    df = pd.read_csv(file_test)
    with open(file_test) as file_obj:

        next(file_obj)
        reader_obj = csv.reader(file_obj)
        for row in reader_obj:
            url = row[0]
            email_request = "https://api.hunter.io/v2/domain-search?domain=" + url + "&api_key=" + api_key
            data1 = cbg.url_parse(email_request)
            try:
                word_start = '''"value": "'''
                word_end = '''"type"'''
                m = re.search(word_start, data1)
                Start = int(m.end())
                mEnd = re.search(word_end, data1)
                End = int(mEnd.start()) - 11

                email_result = data1[Start:End]
            except AttributeError:
                email_result = "no mail"

            if email_result == "no mail":
                output.append("no mail")
                print("nm")
            else:
                output.append(email_result)
                print(email_result)
        df["Email"] = output
        output.append(row)

        df = df[df.Email != "no mail"]
        df.to_csv(desktop + "/" + fName + "_result.csv", index=False)
