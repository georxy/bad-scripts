from typing import Counter
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import csv
import time
import api_keys

desktop = api_keys.desktop


def most_used_kw(fname, how_many):
    file_test = desktop + "/" + fname + ".csv"
    df = pd.read_csv(file_test)

    stop_list = [
        "about", "blog", "contact", "find", "full", "have", "list", "need", "news", "their", "with", "your", "login",
        "tool", "service", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "january", "february", "march", "april",
        "may", "june", "july", "august", "september", "october", "november", "december"
    ]
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'georgy@onthemap.com'  # This is another valid field
    }
    output = []

    with open(file_test) as file_obj:
        next(file_obj)
        reader_obj = csv.reader(file_obj)
        for row in reader_obj:
            word_count = Counter()
            base_url = "https://" + row[0] + "/"  # loop for every site to get analyzed
            try:
                r = requests.get(base_url, headers=headers)
                soup = BeautifulSoup(r.text, 'html.parser')
                all_words = soup.get_text(" ", strip=True).lower().split()

            except requests.exceptions.RequestException:
                all_words = "error"

            for word in all_words:
                cln_word = word.strip('.,?')
                if len(cln_word) > 4:
                    if cln_word in stop_list:
                        continue
                    word_count[cln_word] += 1
            most_occur = word_count.most_common(how_many)
            output.append(most_occur)

            print(most_occur)

    df["Most_used_kw"] = output
    output.append(row)
    df.to_csv(desktop + "/" + fname + "_result.csv", index=False)
