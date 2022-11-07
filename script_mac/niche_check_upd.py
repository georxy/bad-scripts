import csv
import os
import re
import urllib.error
from urllib.request import Request, urlopen
import pandas as pd
import api_keys

desktop = api_keys.desktop

#  request errors

#  niche keywords
#  auto niche keywords
akw = [
    "auto ", "car ", "bike", "automotive", "drive", "retro car", "tuning", "motorcycle", "truck", "car accident",
    "dui charge", "company car", "luxury car", "toyota", "nissan", "hummer", "suv", "jeep",
    "car crash", "speeding", "car review", "dui attorney", "car comparison", "cheap cars",
    "electric cars", "vehicle", "automobile", "automotive news", "car news", "volkswagen", "bmw", "mercedes",
]

#  law niche keywords
lkw = [
    "law ", "legal", "attorney", "lawsuit", "social security", "criminal charges", "criminal", "personal injury",
    "dui", "file a claim", "accident", "sexual harassment", "brutality law", "legal news", "legal insight", "law news",
    "bankruptcy", "civil rights", "divorce", "family law", "employment", "labor", "insurance", "immigration",
    "eb-2", "criminal appeal", "arrest", "settlement", "law firm", "malpractice"
]

#  health niche keywords
hkw = [
    "health", "healthcare", "medicine", "medical", "health insurance", "dental", "dentist", "weight", "heart",
    "procedure", "acne", "hormone", "doctor", "hospital", "syndrome", "disorder", "medicare", "symptom", "recovery",
    "healthy", "symptoms", "nutrient", "diabetes", "poison", "mental health", "rehab"
]

#  fashion niche keywords
fkw = [
    "fashion", "beauty", "lifestyle", "clothes", "makeup", "hairstyle", "style", "fashionable", "travel", "hair",
    "luxury brands", "family", "wedding", "grooming", "fashion ideas", "fashion trends", "fashion design",
    "designer clothes", "jewelry", "fashion magazine", "celebrities", "wellness", "beautiful", "outfit", "parenting",
    "dating", "sewing", "textile", "dress", "celebrity"

]

#  home niche keywords
hokw = [
    "home", "interior", "interior design", "decor", "outdoor", "garden", "roof", "diy", "architecture",
    "construction", "handyman", "renovation", "bathroom", "remodeling", "kitchen", "repair", "remodel",
    "home improvement", "air filter", "air quality", "home value", "flower"
]

#  business niche keywords
bkw = [
    "business", "finance", "company", "real estate", "marketing", "small business", "entrepreneur",
    "businessman", "money", "invest", "investment", "market", "budget", "credit", "loan", "mortgage",
    "startup", "management", "commercial", "industry", "industrial", "sales force", "digital business",
    "digital marketing", "dropshipping", "online business", "start a business", "ecommerce", "e-commerce",
    "drop shipping", "force sales", "start selling"
]


def niche_check(fname):
    output = []
    file_test = desktop + "/" + fname + ".csv"
    df = pd.read_csv(file_test)

    with open(file_test) as file_obj:
        next(file_obj)
        reader_obj = csv.reader(file_obj)
        for row in reader_obj:
            url = "https://" + row[0] + "/"  # loop for every site to get analyzed
            data1 = url_parse(url)

            def find_words(word):
                spec_word_count = data1.lower().count(word)
                return spec_word_count

            def niche_sum(niche_kw):
                needed_sum = 0
                for i in range(len(niche_kw)):
                    needed_sum += find_words(niche_kw[i])
                return needed_sum

            sum_health = niche_sum(hkw)
            sum_auto = niche_sum(akw)
            sum_law = niche_sum(lkw)
            sum_home = niche_sum(hokw)
            sum_fashion = niche_sum(fkw)
            sum_business = niche_sum(bkw)

            sum_general = 400  # general niche score & dictionaries for niches : keyword count values
            niches = {
                sum_business: "Business",
                sum_auto: "Auto",
                sum_law: "Law",
                sum_health: "Health",
                sum_fashion: "Fashion",
                sum_home: "Home",
                sum_general: "General"
            }
            niche_max_result = max(sum_general, sum_auto, sum_law, sum_health, sum_fashion, sum_home, sum_business)
            niche = niches[niche_max_result]

            output.append(niche)
            print(row, niche, sum_auto, sum_law, sum_health, sum_fashion, sum_home, sum_business)

    df["Niche"] = output
    output.append(row)
    df.to_csv(desktop + "/" + fname + "_result.csv", index=False)


def url_parse(url_test):
    try:
        data0 = Request(url_test, headers={"User-Agent": "Mozilla/5.0"})
        data = urlopen(data0, timeout=5).read()
        data_res = data.decode("utf-8")
    except:
        data_res = "bot"
    return data_res
