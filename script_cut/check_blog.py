import csv
import re
from urllib.request import Request, urlopen
import pandas as pd
import api_keys
import certifi

desktop = api_keys.desktop


def check_blog(fname):
    kw_ok = [
        "blog", "news", "recent post", "latest", "posts", "latest news", "magazine", 'journal'
    ]
    kw_maybe = [
        "advertise-with", "advertising", "work-with", "read more", "how-to",
        "what-if", "read more", "continue reading", "top-10", "top-ten", "post", "article",
        "recent content", "lifestyle", "best articles", "popular posts"
    ]

    kw_wfs = [
        "write-for", "contribute-a", "Guest Post", "paid-blog", "write for", "Submit",
        "submit article", "guest blog", "submit-post", "guest-contributor",
        "guest-post", "guest-article", "partner-article", "sponsored-post", "submit-guest", "pricing",
        "submit-news", "become-a-contributor", "content-submission", "submit-your-news", "submit-article",
        "guest-post"
    ]

    red_flag_kw = [
        "shop", "service", "consultation", "customer", "learn more", "product",
        "company", "shop now", "buy now", "order now", "case stud", "get help", "catalog", "to-buy",
        "solution", "radio", "apply for", "reserve", "add to cart", "pick", "try", "offer", "order"
    ]
    red_flag_kw_x10 = [
        "practice", "review Your case"
    ]

    kw_skip = [
        "porn", "sex", "fuck", "masturbat", "blowjob", "cum", "dick"
    ]

    kw_skip_x5 = [
        "dictionary.", "apple.com"
    ]
    # kw - lists with keyword for search on target page

    names = [
        'blog', 'news', 'latest', 'magazine', 'journal', 'story'
    ]

    output = []
    file_test = desktop + "/" + fname + ".csv"
    df = pd.read_csv(file_test)

    with open(file_test, encoding='utf-8') as file_obj:
        next(file_obj)
        reader_obj = csv.reader(file_obj)
        for row in reader_obj:
            url = "https://" + row[0] + "/"  # loop for every site to get analyzed

            data1 = url_parse(url)

            def gp(word):
                try:
                    m = re.search(word, data1)
                    start_pos = int(m.start())
                    end_pos = int(m.end())
                    res = end_pos - start_pos
                    if res > 0:
                        return 1
                    else:
                        return 0  # searches for keyword and returns 1 if kw is on the page and 0 if it's not

                except AttributeError:
                    return 0

            sum_name = 0
            for i in range(len(names)):
                if names[i] in row[0]:
                    sum_name += 1

            if sum_name > 0:
                output.append("Blog")
                print(row, 'b name')
            else:
                sumGP = 0
                for i in range(len(kw_wfs)):
                    sumGP += 30 * gp(kw_wfs[i])

                for i in range(len(kw_maybe)):
                    sumGP += 4 * gp(kw_maybe[i])

                for i in range(len(kw_ok)):
                    sumGP += 7 * gp(kw_ok[i])

                sumNGP = 0
                for i in range(len(red_flag_kw)):
                    sumNGP += 5 * gp(red_flag_kw[i])

                for i in range(len(red_flag_kw_x10)):
                    sumNGP += 10 * gp(red_flag_kw_x10[i])

                sumSKIP = 0
                for i in range(len(kw_skip)):
                    sumSKIP += gp(kw_skip[i])

                for i in range(len(kw_skip_x5)):
                    sumSKIP += gp(kw_skip_x5[i])

                if sumGP - 7 > sumNGP and sumSKIP < 20:
                    output.append("Blog")
                    print(row, "b", sumGP, sumNGP, sumSKIP)

                elif data1 == "bot":
                    output.append("anti-bot")
                    print(row, "abt")

                else:
                    output.append("Not blog")
                    print(row, "nb", sumGP, sumNGP, sumSKIP)

    df["Test_result"] = output
    output.append(row)

    df = df[df.Test_result == "Blog"]
    df.to_csv(desktop + "/" + fname + "_result.csv", index=False)


def url_parse(url_test):
    try:
        data0 = Request(url_test, headers=api_keys.headers)
        data = urlopen(data0, timeout=5).read()
        data_res = str(data.decode("utf-8").lower())
    except:
        data_res = "bot"
    return data_res
