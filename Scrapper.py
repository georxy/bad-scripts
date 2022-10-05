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
import blogs_with_emails as bwe
import niche_check as nc
import most_used_words as muk

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


def blogs_and_emails():
    f_name = e.get()
    bwe.blog_mail(f_name)


def click_niches():
    f_name = e.get()
    nc.niche_check(f_name)


def click_m_used_kw():
    f_name = e.get()
    how_many = e_num.get()
    muk.most_used_kw(f_name, how_many)


btt1 = Button(root, text="'Write for us' check", command=click_wfs, font=("Arial", 12))
btt2 = Button(root, text="Blog check", command=click_blog, font=("Arial", 12))
btt3 = Button(root, text="Email Scrape", command=email_scrapper, font=("Arial", 12))
btt4 = Button(root, text="Blog check + Email scrape", command=blogs_and_emails, font=("Arial", 12))
btt5 = Button(root, text="Niche check", command=click_niches, font=("Arial", 12))
btt6 = Button(root, text="Most used words", command=click_m_used_kw, font=("Arial", 12))

e = Entry(borderwidth=6, font=("Arial", 14))
e.grid(row=0, column=0)
e_num = Entry(borderwidth=6, font=("Arial", 14))
e_num.grid(row=0, column=1)

btt1.grid(row=1, column=0)
btt2.grid(row=2, column=0)
btt3.grid(row=3, column=0)
btt4.grid(row=4, column=0)
btt5.grid(row=5, column=0)
btt6.grid(row=1, column=1)

root.mainloop()
