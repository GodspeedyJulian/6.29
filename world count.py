def extract_words_from_file(filename):
    file = open(filename,'r')
    file_content = file.read()
    file.close()
    words = file_content.split()
    return words
def find_element(alist,item):
    if len(alist)<=1:
        return False
    elif alist[len(alist)//2] == item:
        return True
    elif alist[len(alist)//2] < item:
        return find_element(alist[len(alist)//2:],item)
    else:
        return find_element(alist[:len(alist)//2],item)
def texts_to_words(text_list):
    words = []
    for i in text_list:
        my_substitutions = i.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      "abcdefghijklmnopqrstuvwxyz                                          ")#？
        cleaned_text = i.translate(my_substitutions)
        wds = cleaned_text.split()
        words += wds
    return words
def word_not_in_count(file,vocab):
    words = uniquelize(texts_to_words(extract_words_from_file(file)))
    words_not_in = []
    vocab_list = extract_words_from_file(vocab)
    for i in words:
        if not find_element(vocab_list,i):
            words_not_in.append(i)
if __name__ == '__main__':           #  read file
    file = r'C:\Users\邓洁\Desktop\AIW.txt'
    vocab = r'C:\Users\邓洁\Desktop\VOCAB.txt'
    print(f'There are {len(texts_to_words(extract_words_from_file(file)))} words in Alice in Wondeland, only {len(uniquelize(texts_to_words(extract_words_from_file(file))))} words are unique.')
    print(f'There are {word_not_in_count(file,vocab)} not in vocabulary')
