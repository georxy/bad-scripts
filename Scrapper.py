#  modules
import tkinter
from tkinter import *
import csv
import re
from urllib.request import Request, urlopen
import time
import pandas as pd
from random import randint
from tkinter import messagebox
#  program parts
import email_scrape as ems
import write_for_us_script as wfs
import check_blog as cbg
import niche_check_upd as nc
import most_used_words as muk
import location_check as lc
import backlink_check as blc
import email_generator as eg

#
root = Tk()
root.title("Website Scrapper v1.488")


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
    how_many = int(e_2.get())
    muk.most_used_kw(f_name, how_many)


def location_click():
    f_name = e.get()
    lc.location_check(f_name)


def backlink_click():
    f_name = e.get()
    blc.backlink_check(f_name)


def click_email():
    website = e.get()
    topic = e_2.get()
    eg.email_generator(topic, website)


def error_log():
    binary_code_error = ""
    num = randint(0, 2000)
    for i in range(0, num):
        if i % 8 == 0:
            binary_code_error += ' ' + str(randint(0, 1))
        else:
            binary_code_error += str(randint(0, 1))
    messagebox.showerror("Error " + str(randint(100, 500)), binary_code_error)


def rand_error(num, lucky_num):
    chance = randint(1, num)
    if chance == lucky_num:
        error_log()


rand_error(8, 1)

btt1 = Button(root, text="'Write for us' check", command=click_wfs, font=("Arial", 12), width=25)
btt2 = Button(root, text="Blog check", command=click_blog, font=("Arial", 12), width=25)
btt3 = Button(root, text="Email Scrape", command=email_scrapper, font=("Arial", 12), width=25)
btt4 = ''
btt5 = Button(root, text="Niche filter", command=click_niches, font=("Arial", 12), width=25)
btt6 = Button(root, text="Most used words", command=click_m_used_kw, font=("Arial", 12), width=25)
btt7 = Button(root, text="Location filter", command=location_click, font=("Arial", 12), width=25)
btt8 = Button(root, text="Backlink check", command=backlink_click, font=("Arial", 12), width=25)
btt9 = Button(root, text="Email generator", command=click_email, font=("Arial", 12), width=25)
btt10 = Button(root, text="бля", command=error_log, font=("Arial", 12), width=25)

e = Entry(borderwidth=6, font=("Arial", 14), width=20)
e.insert(0, 'file_name')
e.grid(row=0, column=0)
e_2 = Entry(borderwidth=6, font=("Arial", 14), width=20)
e_2.insert(0, 'num')
e_2.grid(row=0, column=1)

btt1.grid(row=1, column=0)
btt2.grid(row=2, column=0)
btt3.grid(row=3, column=0)
# btt4.grid(row=4, column=0)
btt5.grid(row=5, column=0)
btt6.grid(row=1, column=1)
btt7.grid(row=6, column=0)
btt8.grid(row=4, column=0)  # btt4 place
btt9.grid(row=2, column=1)
btt10.grid(row=3, column=1)

root.mainloop()
