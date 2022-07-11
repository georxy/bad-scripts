import csv
import os
import re
from urllib import request
from urllib.request import Request, urlopen
import time

kw1 = ("write-for", "guest-post", "guest-article", "partner-article", "sponsored-post", "submit-guest")
kw2 = ("submit-news", "become-a-contributor", "content-submission", "submit-your-news", "submit-article")
kw3 = ("contribute-a", "Guest Post", "paid-blog")
# kw - tuples with keyword for search on target page
time1 = time.time() # start time
try:
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')  # path to desktop
    with open(desktop + "/" + 'test_wf.csv') as file_obj:
        reader_obj = csv.reader(file_obj)
        for row in reader_obj:
            url = "https://" + row[0] + "/"  # for loop to check every row

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
            # sum of all values of search per each keyword

            output = list()
            with open(desktop + "/" + "output.csv") as file:
                csv_reader = csv.reader(file)
                for i, rows in enumerate(csv_reader):
                    if sumGP > 1:
                        output = [rows + ["TRUE"]]
                        continue
                    elif data1 == "bot":
                        output += [rows + ["anti-bot"]]
                    else:
                        output += [rows + ["FALSE"]]
            output.append(row)
            print(output)


#except:
#    print("I fucked up")
finally:
    time2 = time.time()
    time = time2 - time1
    print("\nProcess took " + str(round((time), 2)) + " seconds")