def isEmail(text):
    import re
    email = r'[\w\.]+@[a-zA-Z]+\.[a-zA-Z]+'
    match = re.fullmatch(email, text)
    print(True if match else False)

def isDouble(text):
    import re
    double = r'-?[\d]+\.?[\d]*'
    match = re.fullmatch(double, text)
    print(True if match else False)

def getURLasDict(text):
    import re
    url = r'^(?:.*://)?(?P<sitename>[^/]+)(?:/(?P<path>.+))(?:\?(?P<values>.+))$'
    match = re.match(url, text)
    if match:
        for group in ['sitename','path','values']:
            try:
                print(group,':',match.group(group))
            except: ...
