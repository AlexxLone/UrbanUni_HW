def all_variants(text):
    len_txt = len(text)
    for len_ in range(1, len_txt + 1):
        for start_ in range(0, len_txt - len_ + 1):
            yield text[start_:(start_ + len_)]


a = all_variants('abcdefgh')
for i in a:
    print(i)
