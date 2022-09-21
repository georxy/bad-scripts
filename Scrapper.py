from tkinter import *
import csv
import os
import re
from urllib.request import Request, urlopen
import time
import pandas as pd
from random import randint
import email_scrape as ems
import write_for_us_script as wfs
import check_blog as cbg

root = Tk()
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
root.title("Website Scrapper v0.5")


def click_wfs():
    f_name = e.get()
    wfs.blog_wfs(f_name)


def click_blog():
    f_name = e.get()
    cbg.check_blog(f_name)


def email_scrapper():
    f_name = e.get()
    ems.email_io(f_name)


btt1 = Button(root, text="'Write for us' check", command=click_wfs, font=("Arial", 12))
btt2 = Button(root, text="Blog check", command=click_blog, font=("Arial", 12))
btt3 = Button(root, text="Email Scrape", command=email_scrapper, font=("Arial", 12))
e = Entry(borderwidth=6, font=("Arial", 14))
e.grid(row=0, column=0)

btt1.grid(row=1, column=0)
btt2.grid(row=2, column=0)
btt3.grid(row=3, column=0)


root.mainloop()
