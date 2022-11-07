import csv
import re
import urllib.error
from urllib.request import Request, urlopen
import pandas as pd
import os
import api_keys


def backlink_check(fname):

    desktop = api_keys.desktop
    file_test = desktop + "/" + fname + ".csv"
    df = pd.read_csv(file_test)
    output = []

    with open(file_test) as file_obj:
        next(file_obj)
        reader_obj = csv.reader(file_obj)
        for row in reader_obj:
            needed_link_type = row[0].lower()
            target_page = row[1].lower()
            target_page_plus = target_page[:len(target_page) - 1]
            anchor = row[2].lower()
            anchor_plus = anchor[:len(anchor) - 1]
            url = row[3]

            if url == "":
                result = "TBD"
            else:
                data = parse_url(url)
                try:
                    anchor_string = anchor_str(anchor, data)
                    result = result_statement(anchor_string, needed_link_type, target_page)

                except AttributeError:
                    try:
                        anchor_string = anchor_str(anchor_plus, data)
                        result = result_statement(anchor_string, needed_link_type, target_page_plus)
                    except AttributeError:
                        result = "no_kw"

            result_dictionary = {
                "ok": "Correct",
                "notok": "Wrong Target Page",
                "nf": "Link Type is No-Follow",
                "TBD": "",
                "abt": "Anti Bot / Timeout Error",
                "no_kw": "Wrong Anchor / No Anchor Found"
            }
            output.append(result_dictionary[result])
            print(result_dictionary[result])

    df["Link Test"] = output
    df.to_csv(desktop + f"/ {fname}_result.csv", index=False)


def anchor_str(anchor_test, data_search):
    if data_search == 'abt':
        return 'bot'
    else:
        m_anchor_end = re.search('>' + anchor_test + '</a>', data_search)
        anchor_pos_end = int(m_anchor_end.end()) + 4
        anchor_string0 = data_search[anchor_pos_end - 400:anchor_pos_end]
        m_anchor_start = re.search('<a href=', anchor_string0)
        anchor_pos_start = int(m_anchor_start.start())
        anchor_string_0 = anchor_string0[anchor_pos_start:anchor_pos_end]

        return anchor_string_0


def result_statement(anchor_string_test, n_link_type, t_page):
    nf = ["no follow", "no-follow", "nofollow"]
    if anchor_string_test == 'bot':
        res = 'abt'
    else:
        if nf[0] in anchor_string_test or nf[1] in anchor_string_test or nf[2] in anchor_string_test:
            if n_link_type == "do-follow" or n_link_type == "do follow":
                res = "nf"
            else:
                res = "ok"
            return res
        if t_page in anchor_string_test:
            res = "ok"
        else:
            res = "notok"
    return res


def parse_url(url_test):
    try:
        data01 = Request(url_test, headers={"User-Agent": "Mozilla/5.0"})
        data02 = urlopen(data01, timeout=5).read()
        data03 = data02.decode("utf-8")
        output = data03.lower()
    except:
        output = "abt"
    return output
