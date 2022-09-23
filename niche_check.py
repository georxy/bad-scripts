import csv
import os
import re
from urllib.request import Request, urlopen
import pandas as pd

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

#  niche keywords
#  auto niche (1-44 kw)
akw = ("auto", "Auto", "car", "Car", "bike", "Bike", "automotive", "Automotive", "drive", "Drive", "Retro car",
       "Tuning", "tuning", "Motorcycle", "motorcycle", "Truck", "truck", "Car Accident", "car accident", "Accident",
       "DUI charge", "Company Car", "Luxury Car", "Car accident", "Toyota", "Nissan", "Hummer", "SUV", "Jeep",
       "Car Crash", "Car crash", "Speeding", "Car Review", "Car review", "DUI Attorney", "Car Comparison", "Cheap Cars",
       "Electric Cars", "Vehicle", "vehicle", "automobile", "Automobile", "automotive news", "car news")

#  law niche (1-39 kw)
lkw = ("law", "legal", "attorney", "Law", "Legal", "Attorney", "Lawsuit", "lawsuit", "Social Security",
       "Criminal Charges", "Criminal", "Personal Injury", "personal injury", "DUI", "File a Claim", "Accident",
       "Sexual Harassment", "Brutality Law", "Legal News", "Legal news", "Legal Insight", "Law News", "Law news",
       "bankruptcy", "Civil Rights", "Divorce", "Family Law", "Employment", "Labor", "Insurance", "Immigration",
       "EB-2", "Criminal Appeal", "Arrest", "arrest" "Settlement", "Law Firm", "Law firm", "Malpractice")

#  health niche (1-45 kw)
hkw = ("Health", "health", "Healthcare", "Medicine", "medicine", "medicine", "Medical", "medical", "health insurance",
       "Health Insurance", "Dental", "dental", "dentist", "Dentist", "Weight", "weight", "Heart", "heart", "Procedure",
       "Acne", "Hormone", "Doctor", "doctor", "Hospital", "hospital", "Syndrome", "syndrome", "Disorder", "disorder",
       "Medicare", "Symptom", "symptom", "Recovery", "Healthy", "healthy", "Symptoms", "symptoms", "Nutrient",
       "nutrient", "Diabetes", "Poison", "poison", "Mental Health", "Rehab")

#  fashion niche (1-54 kw)
fkw = ("Fashion", "Beauty", "Collection", "Apparel", "Clothes", "Makeup", "Design", "Women", "Men", "Hair", "Style",
       "fashion", "beauty", "collection", "apparel", "clothes", "makeup", "design", "women", "men", "hair", "style",
       "Dress", "Clothing", "Magazine", "Fashion Trends", "Fashion Week", "Accessory", "Accessories", "Skirt",
       "dress", "clothing", "magazine", "fashion trends", "fashion week", "accessory", "accessories", "skirt",
       "Jacket", "Jeans", "Fitness", "Fashionable", "Fashion Show", "Stylist", "Designer", "Fashion Blog",
       "jacket", "jeans", "fitness", "fashionable", "fashion show", "stylist", "designer", "fashion blog")

#  home niche (1-44)
hokw = ("Home", "Interior", "Interior Design", "Decor", "Outdoor", "Garden", "Roof", "DIY", "Architecture",
        "home", "interior", "interior design", "decor", "outdoor", "garden", "roof", "diy", "architecture",
        "Construction", "Handyman", "Renovation", "Bathroom", "Remodeling", "Kitchen", "Repair", "Remodel",
        "construction", "handyman", "renovation", "bathroom", "remodeling", "kitchen", "repair", "remodel",
        "Home Improvement", "Air Filter", "Air Quality", "Home Value", "Flower", "home improvement", "air filter",
        "air quality", "home value", "flower")

# summing keyword scores


def niche_check(fname):
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
                        return 0  # searches for keyword and returns len of the keyword

                except AttributeError:
                    return 0


            sum_health, sum_auto, sum_law, sum_home, sum_fashion = 0, 0, 0, 0, 0

            for i in range(len(akw)):
                sum_auto += gp(akw[i])

            for i in range(len(lkw)):
                sum_law += gp(lkw[i])

            for i in range(len(hkw)):
                sum_health += gp(hkw[i])

            for i in range(len(fkw)):
                sum_fashion += gp(fkw[i])

            for i in range(len(hokw)):
                sum_home += gp(hokw[i])

            sum_general = 10  # general niche score & dictionaries for niches : keyword count values
            niches = {
                sum_auto: "Auto",
                sum_law: "Law",
                sum_health: "Health",
                sum_fashion: "Fashion",
                sum_home: "Home",
                sum_general: "General"
            }
            niche_max_result = max(sum_general, sum_auto, sum_law, sum_health, sum_fashion, sum_home)
            niche = niches[niche_max_result]

            output.append(niche)
            print(row, niche, sum_auto, sum_law, sum_health, sum_fashion, sum_home)
    df["Niche"] = output
    output.append(row)
    df.to_csv(desktop + "/" + fname + "_result.csv", index=False)
