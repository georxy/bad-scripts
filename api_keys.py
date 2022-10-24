import os
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')


f1 = open(desktop + "/hunter_api.txt", "r")
f_api = f1.read()
hunter_api = f_api

openai_api = 'API'
