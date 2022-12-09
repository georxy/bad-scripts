import csv
import re
import pandas as pd
import api_keys
import check_blog as cbg


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
            target_page = row[1][:len(row[1]) - 1].lower()
            anchor = row[2][:len(row[2]) - 1].lower()
            url = row[3]

            if url == "":
                result = "TBD"
            else:
                data = cbg.url_parse(url)
                try:
                    anchor_string = anchor_str(anchor, data, target_page)
                    result = result_statement(anchor_string, needed_link_type, target_page, anchor)

                except AttributeError:
                    result = "no_kw"

            result_dictionary = {
                "ok": "Correct",
                "notok": "Wrong Target Page",
                "nf": "Link Type is No-Follow",
                "TBD": "",
                "abt": "Anti Bot / Timeout Error",
                "no_kw": "Manual Check Needed (Search Error)",
                "df": "Link Type is Do-Follow",
                "err": "Unknown Error",
            }
            output.append(result_dictionary[result])
            print(result_dictionary[result])

    df["Link Test"] = output
    df.to_csv(desktop + f"/{fname}_result.csv", index=False)


def anchor_str(anchor_test, data_search, target_page):
    if data_search == 'abt':
        return 'bot'
    else:
        if anchor_test in target_page and "google.com" not in target_page:
            m_anchor_start = re.search(target_page, data_search)
            anchor_pos_start = int(m_anchor_start.end())
            anchor_string0 = data_search[anchor_pos_start:anchor_pos_start + 400]
            m_anchor_end = re.search(anchor_test, anchor_string0)
            anchor_pos_end = int(m_anchor_end.end())
            anchor_string_0 = anchor_string0[:anchor_pos_end]
            return anchor_string_0
        else:
            m_anchor_end = re.search(anchor_test, data_search)
            anchor_pos_end = int(m_anchor_end.end()) + 4
            anchor_string0 = data_search[anchor_pos_end - 400:anchor_pos_end]
            m_anchor_start = re.search('<a href=', anchor_string0)
            anchor_pos_start = int(m_anchor_start.start())
            anchor_string_0 = anchor_string0[anchor_pos_start:anchor_pos_end]
            return anchor_string_0


def result_statement(anchor_string_test, n_link_type, t_page, anchor_test):
    nf = ["no-follow", "nofollow"]
    if anchor_string_test == 'bot':
        res = 'abt'
        return res
    else:
        if anchor_test in t_page:
            if anchor_test in anchor_string_test:
                if nf[0] in anchor_string_test or nf[1] in anchor_string_test:
                    if n_link_type == "do-follow":
                        res = 'nf'
                    elif n_link_type == "no-follow":
                        res = "ok"
                    else:
                        res = 'err'
                else:
                    if n_link_type == "do-follow":
                        res = 'ok'
                    elif n_link_type == "no-follow":
                        res = 'df'
                    else:
                        res = 'err'
            else:
                res = "notok"
            return res
        else:
            if t_page in anchor_string_test:
                if nf[0] in anchor_string_test or nf[1] in anchor_string_test:
                    if n_link_type == "do-follow":
                        res = 'nf'
                    elif n_link_type == "no-follow":
                        res = "ok"
                    else:
                        res = 'err'
                else:
                    if n_link_type == "do-follow":
                        res = 'ok'
                    elif n_link_type == "no-follow":
                        res = 'df'
                    else:
                        res = 'err'
            else:
                res = "notok"
            return res
