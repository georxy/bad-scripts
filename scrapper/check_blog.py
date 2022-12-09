import asyncio
import aiohttp
import csv
import certifi
import ssl
import pandas as pd
import api_keys

desktop = api_keys.desktop

kw_ok = [
    "blog", "news", "recent post", "latest", "posts", "latest news", "magazine", 'journal'
]
kw_maybe = [
    "advertise-with", "advertising", "work-with", "read more", "how-to",
    "what-if", "read more", "continue reading", "top-10", "top-ten", "post", "article",
    "recent content", "lifestyle", "best articles", "popular posts"
]

kw_wfs = [
    "write-for", "contribute-a", "Guest Post", "paid-blog", "write for", "Submit",
    "submit article", "guest blog ", "submit-post", "guest-contributor",
    "guest-post", "guest-article", "partner-article", "sponsored-post", "submit-guest", "pricing",
    "submit-news", "become-a-contributor", "content-submission", "submit-your-news", "submit-article",
    "guest-post"
]

not_blog = [
    "shop", "service", "consultation", "customer", "learn more", "product",
    "company", "shop now", "buy now", "order now", "case stud", "get help", "catalog", "to-buy",
    "solution", "radio", "apply for", "reserve", "add to cart", "pick", "try", "offer", "order"
]
not_blog_x10 = [
    "practice", "review Your case"
]

kw_skip = [
    "porn", "sex", "fuck", "masturbat", "blowjob", "cum", "dick"
]

kw_skip_x5 = [
    "dictionary.", "apple.com", "case studies", "case study"
]
# kw - lists with keyword for search on target page

names = [
    'blog', 'news', 'latest', 'magazine', 'journal', 'story', 'post'
]


def check_blog(fname):
    output = []
    file_test = desktop + "/" + fname + ".csv"
    df = pd.read_csv(file_test)

    def blog_result_test(html_code, url_test):
        def gp(word):
            spec_word_count = html_code.lower().count(word)
            if spec_word_count > 0:
                return 1
            else:
                return 0

        sum_name = 0
        for i in range(len(names)):
            if names[i] in url_test:
                sum_name += 1

        if sum_name > 0:
            return "Blog"
        else:
            sumGP = 0
            for i in range(len(kw_wfs)):
                sumGP += 30 * gp(kw_wfs[i])

            for i in range(len(kw_maybe)):
                sumGP += 4 * gp(kw_maybe[i])

            for i in range(len(kw_ok)):
                sumGP += 7 * gp(kw_ok[i])

            sumNGP = 0
            for i in range(len(not_blog)):
                sumNGP += 5 * gp(not_blog[i])

            for i in range(len(not_blog_x10)):
                sumNGP += 10 * gp(not_blog_x10[i])

            sumSKIP = 0
            for i in range(len(kw_skip)):
                sumSKIP += gp(kw_skip[i])

            for i in range(len(kw_skip_x5)):
                sumSKIP += gp(kw_skip_x5[i])

            if sumGP - 7 > sumNGP and sumSKIP < 20:
                return "Blog"
            elif html_code == "abt":
                return "Anti-Bot"

            else:
                return "Not Blog"

    async def get_html(session, url):
        try:
            async with session.get(url, headers=api_keys.headers, timeout=10) as response:
                html_response = await response.text()
        except:
            html_response = "abt"

        test_result = blog_result_test(html_response, url)
        return test_result

    async def main():
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        my_conn = aiohttp.TCPConnector(ssl=ssl_context, limit=80)
        async with aiohttp.ClientSession(connector=my_conn) as session:
            url_list = []
            with open(file_test, encoding='utf-8') as file_obj:
                next(file_obj)
                reader_obj = csv.reader(file_obj)
                for row in reader_obj:
                    url_list.append(row[0])

            tasks = []
            for i in range(len(url_list)):
                url = f'https://{url_list[i]}/'
                tasks.append(asyncio.ensure_future(get_html(session, url)))

            html_tasks = await asyncio.gather(*tasks)
            for task in html_tasks:
                output.append(task)
                print(task)

    asyncio.run(main())
    df["Test_result"] = output
    df = df[df.Test_result == "Blog"]
    df.to_csv(desktop + "/" + fname + "_result.csv", index=False)


def url_parse(url_test):
    try:
        data0 = Request(url_test, headers=api_keys.headers)
        data = urlopen(data0, timeout=5, cafile=certifi.where()).read()
        data_res = str(data.decode("utf-8").lower())
    except:
        data_res = "bot"
    return data_res
