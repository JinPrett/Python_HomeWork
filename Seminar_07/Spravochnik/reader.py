def read_1():

    data = open('form_01.txt', 'r')
    for string in data:
        print(string, end = '')
    data.close()

def read_2():
    data = open('form_02.txt', 'r')
    for string in data:
        print(string, end = '')
    print()
    data.close()

