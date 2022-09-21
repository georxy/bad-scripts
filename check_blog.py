import csv
import os
import re
from urllib.request import Request, urlopen
import pandas as pd

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')


def check_blog(fname):
    kw1 = ("write-for", "Advertise", "Advertising", "Article")
    # kw - tuples with keyword for search on target page

    output = []
    file_test = desktop + "/" + fname + ".csv"
    df = pd.read_csv(file_test)

    with open(file_test) as file_obj:
        next(file_obj)
        reader_obj = csv.reader(file_obj)
        for row in reader_obj:
            url = "https://" + row[0] + "/"  # loop for every site to get analyzed
            try:
                data0 = Request(url, headers={"User-Agent": "Mozilla/5.0"})
                data = urlopen(data0, timeout=7).read()
                data1 = data.decode("utf-8")
            except AttributeError:
                data1 = "bot"

            def gp(word):
                try:
                    m = re.search(word, data1)
                    mStart = int(m.start())
                    mEnd = int(m.end())
                    return mEnd - mStart  # searches for keyword and returns len of the keyword

                except AttributeError:
                    return 0

            sumGP = gp(kw1[0]) + gp(kw1[1]) + gp(kw1[2]) + gp(kw1[3])

            # sum of all values of search for each keyword (kw1,kw2,kw3,kw4)
            if sumGP > 1:
                output.append("Blog")
                print("b")
            elif data1 == "bot":
                output.append("anti-bot")
                print("abt")
            else:
                output.append("Not blog")
                print("nb")  # test for blog on page
    df["Test_result"] = output
    output.append(row)

    df = df[df.Test_result != "Not blog"]
    df.to_csv(desktop + "/" + fname + "_result.csv", index=False)  # writing to new csv file "output"
