def process_title(title):
    title=title.lower()
    if '(' in title:
        title=title.split('(')[0]
    elif '5g' in title:
        title=title.split('5g')[0]
    else:
        title = ' '.join(title.split(' ')[:6])  # Join the first 6 words into a single string
    return title