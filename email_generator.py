import openai
import re
import api_keys


def email_generator(topic, website):
    email_pitch_request = \
        f'create a personalized outreach email asking to publish an article on the {topic} topic for ' \
        f'{website}\n with an email subject'

    openai.api_key = api_keys.openai_api
    request = openai.Completion.create(
        engine="text-davinci-002",
        prompt=email_pitch_request,
        temperature=0.7,
        max_tokens=200,
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
    text = text_string.replace('\\n', '\n')
    print(text)
