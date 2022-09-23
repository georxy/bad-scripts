import csv
import os
import re
import urllib.error
from urllib.request import Request, urlopen
import pandas as pd

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')


def check_blog(fname):
    kw_ok = ("Blog", "blog", "News", "Recent Post")
    kw_maybe = ("advertise-with", "Advertising", "Read More", "work-with", "READ MORE", "read more", "how-to",
                "what-if", "read more", "READ MORE", "Continue Reading", "top-10", "top-ten", "post", "article",
                "Article", "Recent Content", "Lifestyle", "Best Articles", "Best articles", "Popular Posts",
                "Popular Articles", "Popular posts")

    kw_wfs = ("write-for", "contribute-a", "Guest Post", "paid-blog", "Write for", "WRITE FOR", "Write For", "Submit",
              "Submit Article", "Guest blog", "GUEST BLOG", "Guest Blog", "submit-post", "guest-contributor",
              "guest-post", "guest-article", "partner-article", "sponsored-post", "submit-guest", "Pricing",
              "submit-news", "become-a-contributor", "content-submission", "submit-your-news", "submit-article",
              "guest-post")

    red_flag_kw = ("Shop", "Forum", "Service", "Job", "Career", "Consultation", "Customer", "Learn More", "Product",
                   "Company", "Shop Now", "Buy Now", "Order Now", "Case Stud", "Get Help", "Catalog", "to-buy",
                   "Solution", "Radio", "Apply for", "Reserve", "Add to Cart", "Pick", "Try", "Offer", "Order")
    red_flag_kw_x10 = ("Practic", "Review Your Case")

    kw_skip = ("porn", "sex", "fuck", "masturbat", "blowjob", "cum", "dick", "Porn", "Sex", "Fuck", "Masturbat",
               "Blowjob", "Cum", "Dick",)

    kw_skip_x5 = ("dictionary.", "apple.com")
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
                data = urlopen(data0, timeout=5).read()
                data1 = data.decode("utf-8")
            except:
                data1 = "bot"

            def gp(word):
                try:
                    m = re.search(word, data1)
                    mStart = int(m.start())
                    mEnd = int(m.end())
                    res = mEnd - mStart
                    if res > 0:
                        return 1
                    else:
                        return 0  # searches for keyword and returns 1 if kw is on the page and 0 if it's not

                except AttributeError:
                    return 0

            sumGP = 0
            for i in range(len(kw_wfs)):
                sumGP += 30 * gp(kw_wfs[i])

            for i in range(len(kw_maybe)):
                sumGP += 2 * gp(kw_maybe[i])

            for i in range(len(kw_ok)):
                sumGP += 5 * gp(kw_ok[i])

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

            if sumGP - 10 > sumNGP and sumSKIP < 20:
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
