def gen_num():
    for i in range(5):
        yield i

gen = gen_num()
for num in gen:
    print(num)

# output 
# 0
# 1
# 2
# 3
# 4

def capital(word):

    x=[char for char in word if char .isupper()]

    yield x

print(next(capital("Hello")))

# output --> ['H']



def double_char_3(str):
    for x in str:
        yield x * 2

print("".join(double_char_3("hello")))

# output-->hheelllloo


def double_char_4(str):
    return "".join([x + x for x in str])
print(double_char_4("Hello"))

# output --> HHeelllloo


str = "123456789"

str_len = len(str)
mask = str_len - 4
showerstr = str[mask:]


print("*" * mask + showerstr)

def masking(number,mask):

    str = ''
    n = mask

    for x in number[:-n]:
        str +='*'
    str += number[-n:]
    return str


print(masking("123456789",4))