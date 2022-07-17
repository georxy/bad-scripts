from tkinter import *
import csv
import os
import re
from urllib.request import Request, urlopen
import time
import pandas as pd
from random import randint


root = Tk()
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
root.title("Website scrapper")
root.geometry('600x400')


def click_wfs():
    time1 = time.time()
    lbl = Label(root, text="Results for '" + e.get() + ".csv' are in file 'output_wfs.csv'")
    fName = e.get()
    lbl.pack()
    kw1 = ("write-for", "guest-post", "guest-article", "partner-article", "sponsored-post", "submit-guest")
    kw2 = ("submit-news", "become-a-contributor", "content-submission", "submit-your-news", "submit-article")
    kw3 = ("contribute-a", "Guest Post", "paid-blog")
    # kw - tuples with keyword for search on target page
    output = []
    file_test = desktop + "/" + fName + ".csv"
    df = pd.read_csv(file_test)
    try:
        with open(file_test) as file_obj:
            next(file_obj)
            reader_obj = csv.reader(file_obj)
            for row in reader_obj:
                url = "https://" + row[0] + "/"  # loop for every site to get analyzed

                try:
                    data0 = Request(url, headers={"User-Agent": "Mozilla/5.0"})
                    data = urlopen(data0).read()
                    data1 = data.decode("utf-8")
                except:
                    data1 = "bot"

                def gp(word):
                    try:
                        m = re.search(word, data1)
                        mStart = int(m.start())
                        mEnd = int(m.end())
                        return mEnd - mStart  # searches for keyword and returns len of the keyword
                    except:
                        return 0

                sumGP = gp(kw1[0]) + gp(kw1[1]) + gp(kw1[2]) + gp(kw1[3]) + gp(kw1[4]) + gp(kw1[5]) + gp(kw2[0]) + \
                        + gp(kw2[1]) + gp(kw2[2]) + gp(kw2[3]) + gp(kw2[4]) + gp(kw3[0]) + gp(kw3[1]) + gp(kw3[2])
                # sum of all values of search for each keyword

                if sumGP > 1:
                    output.append("TRUE")
                elif data1 == "bot":
                    output.append("anti-bot")
                else:
                    output.append("FALSE")  # test for write for us on page

        df["Test result"] = output
        output.append(row)
        df.to_csv(desktop + "/output_wfs.csv", index=False)  # writing to new csv file "output"
    except:
        Label(root, text="I fucked up").pack()
    finally:
        time2 = time.time()
        time_done = time2 - time1
        lbl1 = Label(root, text="Done!\nProcess took " + str(round(time_done, 2)) + " seconds.")
        lbl1.pack()


def click_blog():
    lbl = Label(root, text="Results for '" + e.get() + ".csv' are in file 'output_blog.csv'")
    fName = e.get()
    lbl.pack()
    kw1 = ("write-for", "guest-post", "guest-article", "submit-article", "sponsored-post", "submit-guest")
    kw2 = ("submit-news", "become-a-contributor", "content-submission", "submit-your-news", "submit-article")
    kw3 = ("advertise", "Blog", "Article", "advertising")  # advertise
    # kw - tuples with keyword for search on target page

    output = []
    file_test = desktop + "/" + fName + ".csv"
    df = pd.read_csv(file_test)

    time1 = time.time()
    try:
        with open(file_test) as file_obj:
            next(file_obj)
            reader_obj = csv.reader(file_obj)
            for row in reader_obj:
                url = "https://" + row[0] + "/"  # loop for every site to get analyzed

                try:
                    data0 = Request(url, headers={"User-Agent": "Mozilla/5.0"})
                    data = urlopen(data0).read()
                    data1 = data.decode("utf-8")
                except:
                    data1 = "bot"

                def gp(word):
                    try:
                        m = re.search(word, data1)
                        mStart = int(m.start())
                        mEnd = int(m.end())
                        return mEnd - mStart  # searches for keyword and returns len of the keyword

                    except:
                        return 0

                sumGP = gp(kw1[0]) + gp(kw1[1]) + gp(kw1[2]) + gp(kw1[3]) + gp(kw1[4]) + gp(kw1[5]) + \
                        \
                        + gp(kw2[0]) + gp(kw2[1]) + gp(kw2[2]) + gp(kw2[3]) + gp(kw2[4]) + \
                        \
                        + gp(kw3[0]) + gp(kw3[1]) + gp(kw3[2]) + gp(kw3[3])

                # sum of all values of search for each keyword (kw1,kw2,kw3,kw4)

                if sumGP > 1:
                    output.append("Blog")
                elif data1 == "bot":
                    output.append("anti-bot")
                else:
                    output.append("Not blog")  # test for blog on page

        df["Test_result"] = output
        output.append(row)

        df = df[df.Test_result != "Not blog"]
        df.to_csv(desktop + "/output_blog.csv", index=False)  # writing to new csv file "output"
    except:
        Label(root, text="I fucked up").pack()
    finally:
        time2 = time.time()
        time_done = time2 - time1
        lbl1 = Label(root, text="Done!\nProcess took " + str(round(time_done, 2)) + " seconds.")
        lbl1.pack()

def rand_joke():
    j1 = '''
    Two cowboys are sitting in a saloon. A couple of other cowboys come in. 
    - John, you see these new ones?
    - Yeah, so?
    - Well, the one with the hat...
    - They're both wearing hats.
    - The one with the jeans...
    - They're both in jeans.
    - The one with the boots...
    - They're both wearing boots.
    Shot. 
    - Well, you see the one that fell?
    - Yeah, I see it now. So?
    - He saved my life last year.
    '''
    j2 = '''
    I was digging in the garden and found a box of gold coins. 
    Excited, I decided to run into the house and tell my wife. 
    But then I remembered why I went to dig the hole in the first place.
    '''
    j3 = '''
    Two cowboys are galloping across the prairie. One says to the other:
    - Joe, I'll bet you a hundred dollars that you won't eat my shit.
    - I will, he says.
    They made a bet. Joe ate it, Bill had to pay a hundred dollars.
    They kept bouncing. Joe felt bad for himself, so he says:
    - Bill, I'll bet you a hundred dollars that you won't eat my shit.
    - I will.
    They made a bet. Bill ate it, Joe put up a hundred dollars.
    They go on. Suddenly Bill says:
    - Joe, I think you and I ate shit for free.
    '''
    j4 = '''
    Who could be more dangerous than an HIV-infected bull terrier? 
    The person from whom he became infected.
    '''
    jokes = {1: j1, 2: j2, 3: j3, 4: j4}
    btt_joke = jokes.get(randint(1, 4))
    Label(root, text=btt_joke, font=("Arial", 11, "italic")).pack()


btt1 = Button(root, text="Start 'Write for us' check", command=click_wfs, font=("Arial", 12))
btt2 = Button(root, text="Start Blog check", command=click_blog, font=("Arial", 12))

e = Entry(borderwidth=6, font=("Arial", 14))
e.pack()

btt1.pack()
btt2.pack()
chance = randint(1, 6)
if chance == 1:
    rand_joke()
else:
    pass

root.mainloop()
