import openai
import re
import api_keys
import csv
import pandas as pd
import os
desktop = api_keys.desktop


def meta_generator(target_page):

    text_request = f'write a meta-description for this target page: {target_page}'

    openai.api_key = api_keys.openai_api
    request = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text_request,
        temperature=0.7,
        max_tokens=90,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
    response = str(request)
    text_start_pos_search = re.search('"text": "', response)
    text_start_pos = int(text_start_pos_search.end())
    text_string_0 = response[text_start_pos:]
    text_end_pos_search = re.search('}', text_string_0)
    text_end_pos = int(text_end_pos_search.start()) - 6
    text_string = str(text_string_0[:text_end_pos])
    text01 = text_string.replace('\\n', '\n')
    text = text01.replace('\\', '')

    return text


def bulk_meta_generator(file_name):
    output = []
    file_test = desktop + "/" + file_name + ".csv"
    df = pd.read_csv(file_test)

    with open(file_test) as file_obj:
        next(file_obj)
        reader_obj = csv.reader(file_obj)
        for row in reader_obj:
            t_page = row[0]
            generated_title = meta_generator(t_page)
            output.append(generated_title)
    df["Meta_title"] = output
    output.append(row)
    df.to_csv(desktop + '/' + file_name + '_result.csv', index=False)
