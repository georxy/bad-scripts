#  modules
from tkinter import *
from random import randint
from tkinter import messagebox
import os
#  program parts
import email_scrape as ems
import write_for_us_script as wfs
import check_blog as cbg
import niche_check_upd as nc
import most_used_words as muk
import location_check as lc
import backlink_check as blc
import email_generator as eg
import h1_gen as headers
import meta_title_generator as meta
#
version = 1.488
login_str = str(os.getlogin())
login = login_str[0].upper() + login_str[1:]
#
root = Tk()
root.title(f"Website Scrapper v{version}")


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


rand_error(10, 1)

welcome_text = f'''
    Hey, {login}!
    Welcome to the Scrapper v{version}.
    Choose tool category you want to use.
    ©Georgy Tech
    '''
welcome_label = Label(root, text=welcome_text, font=("Arial", 10), justify=LEFT)
welcome_label.grid(row=0, column=0)


# filter functions in the UI


def filter_functions():
    entry = Entry(borderwidth=6, font=("Arial", 14), width=20)
    entry.insert(0, 'file_name')
    entry.grid(row=0, column=3)

    def click_blog():
        f_name = entry.get()
        cbg.check_blog(f_name)

    def click_wfs():
        f_name = entry.get()
        wfs.blog_wfs(f_name)

    def info_btt():
        info_text = '''
            Filter functions are made to filter blogs from other websites
            and to find the "write for us" button on the page:
                1. create a .csv file on the desktop with the list of websites you want to filter.
                    (or download it from Google Sheets and save it on the desktop)
                2. Enter the file name that you created on the desktop in the "file_name" field.
                3. Choosing function:
                    3.1 Click on the "blog check" button if you want to filter out blogs.
                    3.2 Click on the "'Write for us' check" button if you want to check if
                        pages from the list have a "write for us" button.
                4. The script starts to work and the UI (web scrapper window) will be "not responding" until the
                    the script will finish its work.
                5. Once the script finished its work, on the desktop will appear new .csv file with the results:
                    5.1 If you choose the "Blog check", in the result .csv will be only blogs, 
                        other sites will be removed from the list.
                    5.2 If you choose "Write for us" check, in the result .csv will be a website list and each
                        website will have its value - TRUE if the website has a button, FALSE if it doesn't and abt
                        if the website has an anti-bot system.
            
            '''

        label_info = Label(root, text=info_text, font=("Arial", 10), justify="left")
        label_info.grid(row=6, column=2)

        def hide_button():
            label_info.destroy()
            btt_hide.destroy()

        btt_hide = Button(root, text="Hide info", command=hide_button, font=("Arial", 12), width=15)
        btt_hide.grid(row=7, column=2)

    def hide_button_filter():
        entry.destroy()
        btt_wfs.destroy()
        btt_blog.destroy()
        btt_filter_info.destroy()
        btt_filter_hide.destroy()

    btt_wfs = Button(root, text="Find 'Write for us'", command=click_wfs, font=("Arial", 12), width=25)
    btt_blog = Button(root, text="Filter Blogs", command=click_blog, font=("Arial", 12), width=25)
    btt_filter_info = Button(root, text="Info", command=info_btt, font=("Arial", 12), width=25)
    btt_filter_hide = Button(root, text="Hide", command=hide_button_filter, font=("Arial", 12), width=25)
    btt_wfs.grid(row=1, column=3)
    btt_blog.grid(row=2, column=3)
    btt_filter_info.grid(row=3, column=3)
    btt_filter_hide.grid(row=4, column=3)


filter_button = Button(root, text="Filter Functions", command=filter_functions, font=("Arial", 12), width=25)
filter_button.grid(row=2, column=0)


#  categorization functions in the UI

def categorization_functions():
    entry = Entry(borderwidth=6, font=("Arial", 14), width=20)
    entry.insert(0, 'file_name')
    entry.grid(row=0, column=3)

    def niche_click():
        f_name = entry.get()
        nc.niche_check(f_name)

    def location_click():
        f_name = entry.get()
        lc.location_check(f_name)

    def info_btt():
        info_text = '''
            Categorization functions are made to define niches or locations for websites:
                1. create a .csv file on the desktop with the list of websites you want to categorize.
                    (or download it from Google Sheets and save it on the desktop)
                2. Enter the file name that you created on the desktop in the "file_name" field.
                3. Choosing function:
                    3.1 Click on the "Define Niche" button if you want to define niches for websites in the list.
                    3.2 Click on the "Define Location" button if you want to define locations for websites in the list.
                4. The script starts to work and the UI (web scrapper window) will be "not responding" until the
                    the script will finish its work.
                5. Once the script finished its work, on the desktop will appear new .csv file with the results:
                    5.1 If you choose "Define Niche", in the result .csv will appear website list and 
                        the defined niche near each website.
                    5.2 If you choose "Define Location", in the result .csv will appear website list and 
                        the defined location near each website.
            '''

        label_info = Label(root, text=info_text, font=("Arial", 10), justify="left")
        label_info.grid(row=6, column=2)

        def hide_button():
            label_info.destroy()
            btt_hide.destroy()

        btt_hide = Button(root, text="Hide info", command=hide_button, font=("Arial", 12), width=15)
        btt_hide.grid(row=7, column=2)

    def hide_button_cat():
        entry.destroy()
        btt_niche.destroy()
        btt_loc.destroy()
        btt_cat_info.destroy()
        btt_cat_hide.destroy()

    btt_niche = Button(root, text="Define Niche", command=niche_click, font=("Arial", 12), width=25)
    btt_loc = Button(root, text="Define Location", command=location_click, font=("Arial", 12), width=25)
    btt_cat_info = Button(root, text="Info", command=info_btt, font=("Arial", 12), width=25)
    btt_cat_hide = Button(root, text="Hide", command=hide_button_cat, font=("Arial", 12), width=25)
    btt_niche.grid(row=1, column=3)
    btt_loc.grid(row=2, column=3)
    btt_cat_info.grid(row=3, column=3)
    btt_cat_hide.grid(row=4, column=3)


categorization_button = Button(root, text="Categorization Functions",
                               command=categorization_functions, font=("Arial", 12), width=25)
categorization_button.grid(row=3, column=0)


# UI for scraping functions


def scraping_functions():
    entry = Entry(borderwidth=6, font=("Arial", 14), width=20)
    entry.insert(0, 'file_name')
    entry.grid(row=0, column=3)

    def email_parse():
        f_name = entry.get()
        ems.email_io(f_name)

    def click_m_used_kw():
        f_name = entry.get()
        muk.most_used_kw(f_name, 10)

    def backlink_click():
        f_name = entry.get()
        blc.backlink_check(f_name)

    def info_btt():
        info_text = '''
            Scraping functions are made to find something on the websites:
                1. create a .csv file on the desktop with the list of websites you want to categorize.
                    (or download it from Google Sheets and save it on the desktop)
                2. Enter the file name that you created on the desktop in the "file_name" field.
                3. Choosing function:
                    3.1 Click on the "Find Emails" button if you want to find emails for websites in the list.
                    3.2 Click on the "Find Most Used Words" button if you want to find most used words for each website
                     in the list.
                    3.3 Click on the "Check Backlinks" button if you want to check if published backlinks from the 
                    providers are correct. To make script work you need to:
                        3.3.1 link type must be in column A, Target Page in column B, 
                            Anchor - C, and Published backlink - D.
                4. The script starts to work and the UI (web scrapper window) will be "not responding" until the
                    the script will finish its work.
                5. Once the script finished its work, on the desktop will appear new .csv file with the results:
                    5.1 If you choose "Find Emails", in the result .csv will appear website list and 
                        the email near each website. (sites without emails will be removed)
                    5.2 If you choose "Find Most Used Words", in the result .csv will appear website list and 
                        the most used words near each website.
                    5.3 If you choose "Check Backlinks", in the result .csv will appear new column with results - 
                        column E.
            '''

        label_info = Label(root, text=info_text, font=("Arial", 10), justify="left")
        label_info.grid(row=6, column=2)

        def hide_button():
            label_info.destroy()
            btt_hide.destroy()

        btt_hide = Button(root, text="Hide info", command=hide_button, font=("Arial", 12), width=15)
        btt_hide.grid(row=7, column=2)

    def hide_button_scr():
        entry.destroy()
        btt_email.destroy()
        btt_used_words.destroy()
        btt_backlink.destroy()
        btt_scr_info.destroy()
        btt_scr_hide.destroy()

    btt_email = Button(root, text="Find Emails", command=email_parse, font=("Arial", 12), width=25)
    btt_used_words = Button(root, text="Find Most Used Words", command=click_m_used_kw, font=("Arial", 12), width=25)
    btt_backlink = Button(root, text="Check Backlinks", command=backlink_click, font=("Arial", 12), width=25)
    btt_scr_info = Button(root, text="Info", command=info_btt, font=("Arial", 12), width=25)
    btt_scr_hide = Button(root, text="Hide", command=hide_button_scr, font=("Arial", 12), width=25)

    btt_email.grid(row=1, column=3)
    btt_used_words.grid(row=2, column=3)
    btt_backlink.grid(row=3, column=3)
    btt_scr_info.grid(row=4, column=3)
    btt_scr_hide.grid(row=5, column=3)


scraping_button = Button(root, text="Scraping Functions",
                         command=scraping_functions, font=("Arial", 12), width=25)
scraping_button.grid(row=4, column=0)


def ai_functions():
    entry_number = Entry(borderwidth=6, font=("Arial", 14), width=20)
    entry_number.insert(0, 'how_many')
    entry_number.grid(row=0, column=1)
    entry_topic = Entry(borderwidth=6, font=("Arial", 14), width=20)
    entry_topic.insert(0, 'topic')
    entry_topic.grid(row=0, column=2)
    entry_t_page = Entry(borderwidth=6, font=("Arial", 14), width=20)
    entry_t_page.insert(0, 'target_page')
    entry_t_page.grid(row=0, column=3)

    def click_email():
        website = entry_t_page.get()
        topic = entry_topic.get()
        res = eg.email_generator(topic, website)
        text_result(res)

    def click_h1():
        num = int(entry_number.get())
        topic = entry_topic.get()
        target_page = entry_t_page.get()
        res = headers.h1_generator(num, topic, target_page)
        text_result(res)

    def click_meta():
        t_page = entry_t_page.get()
        res = meta.meta_generator(t_page)
        text_result(res)

    def text_result(text):
        entry_result = Entry(borderwidth=6, font=("Arial", 14), width=20)
        entry_result.insert(0, text)
        entry_result.grid(row=2, column=1)

        def copy_click():
            root.clipboard_clear()
            root.clipboard_append(text)

        def hide_copy():
            entry_result.destroy()
            btt_copy.destroy()
            btt_hide_copy.destroy()

        btt_copy = Button(root, text="Copy", command=copy_click, font=("Arial", 12), width=25)
        btt_copy.grid(row=3, column=1)

        btt_hide_copy = Button(root, text="Hide Result", command=hide_copy, font=("Arial", 12), width=25)
        btt_hide_copy.grid(row=4, column=1)

    def info_btt():
        info_text = '''
        This H1/Email/Meta Description generator is built on the OpenAI GPT-3 text generation model.
        To generate H1 or email you want:
            1. In "how_many" field type how many H1 you need (for emails leave this field empty)
            2. In the "topic" field enter the topic for the H1/Email you want to generate
            3. In the "target_page" field enter the target page for which you want to generate H1/Email
            4. Press "Generate H1" or "Generate Email"
            5. In a few seconds will appear field with H1 and the button "Copy"
            6. Press the button "Copy" to copy the H1 or email to the clipboard
        To generate Meta Description you want:
            1. Leave all fields empty, except of the "target page" field
            2. In the "target_page" field enter the target page for which you want to create meta description.
            3. Press the "Generate Meta Description" button ad wait.
            4. Press the button "Copy" to copy the meta description to the clipboard.
        P.S. You can leave the "topic" or/and "target_page" fields empty, 
        but the H1 and Email in the result will have worse quality.
        '''

        label_info = Label(root, text=info_text, font=("Arial", 10), justify="left")
        label_info.grid(row=6, column=2)

        def hide_button():
            label_info.destroy()
            btt_hide.destroy()

        btt_hide = Button(root, text="Hide info", command=hide_button, font=("Arial", 12), width=15)
        btt_hide.grid(row=7, column=2)

    def hide_button_ai():
        entry_t_page.destroy()
        entry_topic.destroy()
        entry_number.destroy()
        btt_email.destroy()
        btt_h1.destroy()
        btt_meta.destroy()
        btt_ai_info.destroy()
        btt_ai_hide.destroy()

    btt_email = Button(root, text="Generate email", command=click_email, font=("Arial", 12), width=25)
    btt_h1 = Button(root, text="Generate H1", command=click_h1, font=("Arial", 12), width=25)
    btt_meta = Button(root, text="Generate Meta Description", command=click_meta, font=("Arial", 12), width=25)
    btt_ai_info = Button(root, text="Info", command=info_btt, font=("Arial", 12), width=25)
    btt_ai_hide = Button(root, text="Hide", command=hide_button_ai, font=("Arial", 12), width=25)

    btt_email.grid(row=1, column=3)
    btt_h1.grid(row=2, column=3)
    btt_meta.grid(row=3, column=3)
    btt_ai_info.grid(row=4, column=3)
    btt_ai_hide.grid(row=5, column=3)


ai_button = Button(root, text="AI Functions", command=ai_functions, font=("Arial", 12), width=25)
ai_button.grid(row=5, column=0)


def ai_bulk_functions():
    entry = Entry(borderwidth=6, font=("Arial", 14), width=20)
    entry.insert(0, 'file_name')
    entry.grid(row=0, column=1)

    def header_bulk():
        file_name = entry.get()
        headers.h1_bulk(file_name)

    def meta_bulk():
        file_name = entry.get()
        meta.bulk_meta_generator(file_name)

    def info_btt():
        info_text = '''
        This H1/Email generator is built on the OpenAI GPT-3 text generation model.
        To generate H1 or meta description for every site in the list you want:
            1. Create a .csv file on the desktop.
            2. 
                2.1 If you want to generate 3 H1's for every site you need to place websites in the column A and topics 
                in the column B
                2.2 If you want to generate meta descriptions place websites in the column A
            3. Enter the file name in the "file_name" field.
            3. 
                3.1 If you want to generate H1's press "Bulk H1" button
                3.2 If you want to generate Meta Descriptions press "Bulk Meta Description" button.
            4. The script starts to work and the UI (web scrapper window) will be "not responding" until the
                the script will finish its work.
            5. Once the script finished its work, on the desktop will appear new .csv file with the results:
                5.1 If you choose "Bulk H1", in the result .csv will appear website list and 
                    the 3 H1 near each website.
                5.2 If you choose "Bulk Meta Description", in the result .csv will appear website list and 
                    a meta description near each website.
        '''

        label_info = Label(root, text=info_text, font=("Arial", 10), justify="left")
        label_info.grid(row=6, column=2)

        def hide_button():
            label_info.destroy()
            btt_hide.destroy()

        btt_hide = Button(root, text="Hide info", command=hide_button, font=("Arial", 12), width=15)
        btt_hide.grid(row=7, column=2)

    def hide_button_bai():
        entry.destroy()
        btt_h1.destroy()
        btt_meta.destroy()
        btt_bai_info.destroy()
        btt_bai_hide.destroy()

    btt_h1 = Button(root, text="Bulk H1", command=header_bulk, font=("Arial", 12), width=25)
    btt_meta = Button(root, text="Bulk Meta Description", command=meta_bulk, font=("Arial", 12), width=25)
    btt_bai_info = Button(root, text="Info", command=info_btt, font=("Arial", 12), width=25)
    btt_bai_hide = Button(root, text="Hide", command=hide_button_bai, font=("Arial", 12), width=25)

    btt_h1.grid(row=1, column=1)
    btt_meta.grid(row=2, column=1)
    btt_bai_info.grid(row=3, column=1)
    btt_bai_hide.grid(row=4, column=1)


bai_button = Button(root, text="Bulk AI Functions", command=ai_bulk_functions, font=("Arial", 12), width=25)
bai_button.grid(row=6, column=0)

root.update()
root.mainloop()
