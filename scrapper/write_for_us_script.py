import csv
import check_blog as cbg
import re
from urllib.request import Request, urlopen
import pandas as pd
import api_keys

desktop = api_keys.desktop


def blog_wfs(fname):
    wfs_kw = (
        "write-for", "guest-post", "guest-article", "partner-article", "sponsored-post", "submit-guest",
        "submit-news", "become-a-contributor", "content-submission", "submit-your-news", "submit-article",
        "contribute-a", "guest post", "paid-blog", "write for", "contribute"
        "submit article", "guest blog", "submit-post", "guest-contributor", "guest contributor"
    )
    # kw - tuples with keyword for search on target page
    output = []
    file_test = desktop + "/" + fname + ".csv"
    df = pd.read_csv(file_test)
    with open(file_test) as file_obj:
        next(file_obj)
        reader_obj = csv.reader(file_obj)
        for row in reader_obj:
            url = "https://" + row[0] + "/"  # loop for every site to get analyzed
            data1 = cbg.url_parse(url)

            def gp(word):
                try:
                    m = re.search(word, data1)
                    mStart = int(m.start())
                    mEnd = int(m.end())
                    res = mEnd - mStart
                    if res > 0:
                        return 1
                    else:
                        return 0
                except AttributeError:
                    return 0

            sum_result = 0
            for i in range(len(wfs_kw)):
                sum_result += gp(wfs_kw[i])

            # sum of all values of search for each keyword

            if sum_result > 1:
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


def url_parse(url_test):
    try:
        data0 = Request(url_test, headers={"User-Agent": "Mozilla/5.0"})
        data = urlopen(data0, timeout=5).read()
        data_res = data.decode("utf-8").lower()
    except:
        data_res = "bot"
    return data_res
