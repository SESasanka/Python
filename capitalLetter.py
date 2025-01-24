def capital(word):

    x = [char for char in word if char .isupper()]
    
    yield x

    # x = []

    # for char in word:
    #     if char .isupper():
    #         x.append(char)

    # return x

print(next(capital("ABcD")))



