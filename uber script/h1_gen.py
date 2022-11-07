import openai
import re
import api_keys


def h1_generator(num, topic, target_page):

    def request_statement():
        text_request_dict = {
            'all_info': f'create {num} original headers for articles on {topic} topics for this website: {target_page}',
            'no_tp': f'create {num} original headers for articles on {topic} topics',
            'no_h1_num': f'create one original header for the article on {topic} topic for this website: {target_page}',
            'no_topic': f'create {num} original headers for articles for this website: {target_page}',
            'topic_only': f'create original header for article on {topic} topics',
            'h1_num_only': f'create {num} original headers for articles',
            'tp_only': f'create original header for the article for this website: {target_page}',
            'no_info': f'create one original header for the article'
        }
        if num == 1:
            res = 'no_h1_num'
            if num == 1 and topic == 'topic':
                res = 'tp_only'
                if num == 1 and topic == 'topic' and target_page == 'target_page':
                    res = 'no_info'
        elif topic == 'topic':
            res = 'no_topic'
            if topic == 'topic' and target_page == 'target_page':
                res = 'h1_num_only'
        elif target_page == 'target_page':
            res = 'no_tp'
            if target_page == 'target_page' and num == 1:
                res = 'topic_only'
        else:
            res = 'all_info'

        return text_request_dict[res]

    text_request = request_statement()
    openai.api_key = api_keys.openai_api
    request = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text_request,
        temperature=0.7,
        max_tokens=90*num,
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

