def process_title(title):
    title=title.lower()
    if '(' in title:
        title=title.split('(')[0]
    elif '5g' in title:
        title=title.split('5g')[0]
    else:
        title=title.split(' ')[:6]
    return title