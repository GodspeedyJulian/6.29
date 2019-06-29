def Sequential(list1, target):
    global a
    a=False
    for i in range(len(list1)):
        if list1[i]==target:
            a=True
            break
    if a==False:
        missing_words.append(target)
    return missing_words
