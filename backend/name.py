def getName(title):
    title = title.lower()
    title = title.replace("-", " ")
    title = title.replace(",", "")
    title = title.replace("+", " ")
    words = title.split(" ")
    name = []
    if "star" in words:
        name.append(words[0]) 
        lit = "empty"
        if "l" in words:
            lit = "l"
        elif "litre" in words:
            lit = "litre"
        elif "litres" in words:
            lit = "litres"
        elif "ton" in words:
            lit = "ton"
        elif "tons" in words:
            lit = "tons"
        else:
            for word in words:
                if word.endswith('l') and word[:-1].isdigit():
                    # Extract the number and add it to the list of numbers
                    number = word[:-1]  # Extracting the digits before 'l'
                    name.append(number)
                    name.append("l")
        if lit!="empty":
            i = words.index(lit)
            name.append(words[i-1])
            if lit == "l" or lit == "litre" or lit == "litres":
                name.append("l")
            else:
                name.append("ton")
            i = words.index("star")
            name.append(words[i-1])
            name.append(words[i])
        else:
            i = words.index("star")
            name.extend(words[:i+1])
    elif "gb" in title:
        if "5g" in words:
            i = words.index("5g")
            name.extend(words[:i])
        else:
            title = title.split("(")[0]
            name = title.split(" ")
    rname = " ".join(name)
    if not name:
        return title
    else:
        return rname