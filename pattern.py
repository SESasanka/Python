# def myPattern(n):
      
#     for i in range (0,n):
#         for j in range (0, i +1):
#             print("*", end="")
#         print("\r")

# n = 5
# myPattern(n)


def hide_card_num(number,mask):
    str = ''
    n = mask

    for i in number[:-n]:
        str +='*'
    str += number[-n:]
    return str

print(hide_card_num("12365745367353", 4))


# str = "123456789"

# str_len = len(str)
# mask =str_len - 4
# showerstr = str[mask:]

# print("*" * mask +  showerstr)
