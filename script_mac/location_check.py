#  location scrapper
import csv
import os
import re
from urllib.request import Request, urlopen
import pandas as pd
import api_keys

desktop = api_keys.desktop

#  niche keywords
#  florida location keywords
fl_kw = [
    "florida", "miami", "orlando", "miami local", "florida local", "miami beach", "tampa bay", "jacksonville",
    "florida weather", "miami news", "florida news", "miami business", "florida business", "florida man", "tampa",
    "latest in florida", "miami magazine", "florida magazine"
]

#  california location keywords
ca_kw = [
    "california", "los angeles", "san francisco", "california local", "silicon valley", "san francisco local",
    "los angeles news", "san francisco news", "los angeles local", "california business", 'california weather',
    'los angeles weather', 'san francisco weather', 'los angeles magazine', 'california post', 'california magazine',

]

#  arizona location keywords
az_kw = [

]

#  new york location keywords
ny_kw = [

]

#  washington location keywords
wa_kw = [

]

#  georgia keywords
ga_kw = [

]

#  canada location keywords
canada_kw = [

]

#  colorado location keywords
co_kw = [

]

#  indiana location keywords
in_kw = [

]

# missouri l. kw
mi_kw = [

]

# pennsylvania l. kw
pn_kw = [

]

#  texas l. kw
tx_kw = [

]

# illinois l. kw
il_kw = [

]

# australia l. kw
au_kw = [

]


def location_check(fname):
    output = []
    file_test = desktop + "/" + fname + ".csv"
    df = pd.read_csv(file_test)

    with open(file_test) as file_obj:
        next(file_obj)
        reader_obj = csv.reader(file_obj)
        for row in reader_obj:
            url = "https://" + row[0] + "/"  # loop for every site to get analyzed

            data1 = parse_url(url)

            def find_words(word):
                try:
                    spec_word_count = data1.lower().count(word)
                    return spec_word_count  # counts words word from lists on the site

                except AttributeError:
                    return 0


            sum_general = 50
            location_sum_list = [
                sum_fl, sum_ca, sum_az, sum_ny, sum_wa, sum_ga, sum_canada, sum_co, sum_in, sum_mi, sum_pn, sum_tx,
                sum_il, sum_au
            ]

            kw_list = [
                fl_kw, ca_kw, az_kw, ny_kw, wa_kw, ga_kw, canada_kw, co_kw, in_kw, mi_kw, pn_kw, tx_kw, il_kw, au_kw
            ]

            def loc_sum(loc_kw):
                needed_sum = 0
                for i in range(len(loc_kw)):
                    needed_sum += find_words(loc_kw[i])
                return needed_sum

            sum_fl = loc_sum(fl_kw)
            sum_ca = loc_sum(ca_kw)
            sum_az = loc_sum(az_kw)
            sum_ny = loc_sum(ny_kw)
            sum_wa = loc_sum(wa_kw)
            sum_ga = loc_sum(ga_kw)
            sum_canada = loc_sum(canada_kw)
            sum_co = loc_sum(co_kw)
            sum_in = loc_sum(in_kw)
            sum_mi = loc_sum(mi_kw)
            sum_pn = loc_sum(pn_kw)
            sum_tx = loc_sum(tx_kw)
            sum_il = loc_sum(il_kw)

            # dictionary for locations : keyword count values
            locations = {
                sum_fl: "Florida",
                sum_ca: "California",
                sum_az: "Arizona",
                sum_ny: "New York",
                sum_wa: "Washington",
                sum_ga: "Georgia",
                sum_canada: "Canada",
                sum_co: "Colorado",
                sum_in: "Indiana",
                sum_mi: "Michigan",
                sum_pn: "Pennsylvania",
                sum_tx: "Texas",
                sum_il: "Illinois",
                sum_general: "General"
            }

            loc_max_result = max(sum_general, sum_fl, sum_ca, sum_az, sum_ny, sum_wa, sum_ga, sum_canada,
                                 sum_co, sum_in, sum_mi, sum_pn, sum_tx, sum_il)
            location = locations[loc_max_result]

            output.append(location)
            print(row, location, sum_fl, sum_ca, sum_az, sum_ny, sum_wa, sum_ga, sum_canada,
                  sum_co, sum_in, sum_mi, sum_pn, sum_tx, sum_il)
    df["Niche"] = output
    output.append(row)
    df.to_csv(desktop + "/" + fname + "_result.csv", index=False)


def parse_url(url_test):
    try:
        data01 = Request(url_test, headers={"User-Agent": "Mozilla/5.0"})
        data02 = urlopen(data01, timeout=5).read()
        data03 = data02.decode("utf-8")
        output = str(data03.lower())
    except:
        output = "abt"
    return output
