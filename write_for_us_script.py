import csv
import os
import re
from urllib.request import Request, urlopen
import pandas as pd

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')


def blog_wfs(fname):

    kw1 = ("write-for", "guest-post", "guest-article", "partner-article", "sponsored-post", "submit-guest")
    kw2 = ("submit-news", "become-a-contributor", "content-submission", "submit-your-news", "submit-article")
    kw3 = ("contribute-a", "Guest Post", "paid-blog", "Write for", "WRITE FOR", "Write For")
    kw4 = ("Submit Article", "Guest blog", "GUEST BLOG", "Guest Blog", "submit-post", "guest-contributor")
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
                data = urlopen(data0).read()
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

            sumGP = gp(kw1[0]) + gp(kw1[1]) + gp(kw1[2]) + gp(kw1[3]) + gp(kw1[4]) + gp(kw1[5]) + gp(kw2[0]) + \
                + gp(kw2[1]) + gp(kw2[2]) + gp(kw2[3]) + gp(kw2[4]) + gp(kw3[0]) + gp(kw3[1]) + gp(kw3[2]) + \
                + gp(kw3[3]) + gp(kw3[4]) + gp(kw3[5]) + gp(kw4[0]) + gp(kw4[1]) + gp(kw4[2]) + gp(kw4[3]) + \
                + gp(kw4[4]) + gp(kw4[5])
            # sum of all values of search for each keyword

            if sumGP > 1:
                output.append("TRUE")
                print("+")
            elif data1 == "bot":
                output.append("anti-bot")
                print("abt")
            else:
                output.append("FALSE")  # test for write for us on page
                print("-")

    df["Test result"] = output
    output.append(row)
    df.to_csv(desktop + "/" + fname + "_result.csv", index=False)  # writing to new csv file "output"
