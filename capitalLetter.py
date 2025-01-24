# def capital(word):

#     x = [char for char in word if char .isupper()]
    
#     yield x

#     # x = []

#     # for char in word:
#     #     if char .isupper():
#     #         x.append(char)

#     # return x

# print(next(capital("ABcD")))



def capital(s):
    return [i for i in range(len(s)) if s[i].isuppser()]

print(capital("Hello"))

