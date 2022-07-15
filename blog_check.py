import csv
import os
import re
from urllib import request
from urllib.request import Request, urlopen
import time
import pandas as pd

kw1 = ("write-for", "guest-post", "guest-article", "submit-article", "sponsored-post", "submit-guest")
kw2 = ("submit-news", "become-a-contributor", "content-submission", "submit-your-news", "submit-article")  # write for us
kw3 = ("advertise", "Blog",  "Article", "advertising") #, "Read More", "Read more", "READ MORE")  # advertise
#kw4 = ("blog", "read more", "Read more", "Read More", "post")
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


            sumGP = gp(kw1[0]) + gp(kw1[1]) + gp(kw1[2]) + gp(kw1[3]) + gp(kw1[4]) + gp(kw1[5]) + \
                \
                + gp(kw2[0]) + gp(kw2[1]) + gp(kw2[2]) + gp(kw2[3]) + gp(kw2[4]) + \
                \
                + gp(kw3[0]) + gp(kw3[1]) + gp(kw3[2]) + gp(kw3[3])# + gp(kw3[4])# + gp(kw3[5]) + gp(kw3[6])  # + \

            # sum of all values of search for each keyword (kw1,kw2,kw3,kw4)


            if sumGP > 1:
                print("TRUE")
                output.append("Blog")
            elif data1 == "bot":
                print("anti-bot")
                output.append("anti-bot")
            else:
                print("FALSE")
                output.append("Not blog")  # test for blog on page

    df["Test_result"] = output
    output.append(row)

    df = df[df.Test_result != "Not blog"]
    df.to_csv(desktop + "/output.csv", index=False)  # writing to new csv file "output"


#except:
#    print("I fucked up")
finally:
    time2 = time.time()
    time = time2 - time1
    print("\nProcess took " + str(round((time), 2)) + " seconds")
