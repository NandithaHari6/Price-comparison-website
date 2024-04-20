def process_title(title):
    title=title.lower()
    if '(' in title:
        title=title.split('(')[0]
    elif '5g' in title:
        title=title.split('5g')[0]
    else:
        array=title.split(' ')[:6]
        for i in array:
            title+=str(i)
            

    
    return title
