def even_numbers(y):
    for x in range(0,y+1,2):
        yield x


even_numbers_list = even_numbers(10)
for number in even_numbers_list:
    print(number)

