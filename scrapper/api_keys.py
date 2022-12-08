import os
from tkinter import messagebox

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'georgy@onthemapmarketing.co'  # This is another valid field
}

try:
    f1 = open(desktop + "/api_keys.txt", "r")
    content = f1.readlines()

    if content[0][:6].lower() == 'hunter':
        hunter_api = content[0][-41:]
        openai_api = content[1][-51:]
    else:
        openai_api = content[0][-51:]
        hunter_api = content[1][-41:]
except FileNotFoundError:
    messagebox.showerror("API Keys Error", "API keys are missing. \nPlease check if you have 'api_keys.txt' file with"
                                           "API keys for Openai & Hunter on your desktop")
