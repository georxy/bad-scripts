import csv
import os
import re
from urllib import request
from urllib.request import Request, urlopen
import time
import pandas as pd

kw1 = ("write-for", "guest-post", "guest-article", "partner-article", "sponsored-post", "submit-guest")
kw2 = ("submit-news", "become-a-contributor", "content-submission", "submit-your-news", "submit-article")
kw3 = ("contribute-a", "Guest Post", "paid-blog")
# kw - tuples with keyword for search on target page

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
output = []

file_test = desktop + "/" + input("Enter the file name ") + ".csv"

df = pd.read_csv(file_test)

time1 = time.time()
try:
    with open(file_test) as file_obj:
        heading = next(file_obj)
        reader_obj = csv.reader(file_obj)
        for row in reader_obj:
            url = "https://" + row[0] + "/"  # loop for every site to get analyzed

            try:
                data0 = Request(url, headers={"User-Agent": "Mozilla/5.0"})
                data = urlopen(data0).read()
                data1 = data.decode("utf-8")

            except:
                data1 = "bot"
            def gp(word):
                try:
                    m = re.search(word, data1)
                    mStart = int(m.start())
                    mEnd = int(m.end())
                    return mEnd - mStart  # searches for keyword and returns len of the keyword
                except:
                    return 0


            sumGP = gp(kw1[0]) + gp(kw1[1]) + gp(kw1[2]) + gp(kw1[3]) + gp(kw1[4]) + gp(kw1[5]) \
                    + gp(kw2[0]) + gp(kw2[1]) + gp(kw2[2]) + gp(kw2[3]) + gp(kw2[4]) + \
                    + gp(kw3[0]) + gp(kw3[1]) + gp(kw3[2])
            # sum of all values of search for each keyword


            if sumGP > 1:
                print("TRUE")
                output.append("TRUE")
            elif data1 == "bot":
                print("anti-bot")
                output.append("anti-bot")
            else:
                print("FALSE")
                output.append("FALSE")  # test for write for us on page

    df["Test result"] = output
    output.append(row)
    df.to_csv(desktop + "/output.csv")  # writing to new csv file "output"

except:
    print("I fucked up")
finally:
    time2 = time.time()
    time = time2 - time1
    print("\nProcess took " + str(round((time), 2)) + " seconds")
