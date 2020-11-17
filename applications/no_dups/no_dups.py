def no_dups(s):
    # Your code here
    split = s.split()
    dic = dict()
    for sp in split:
        dic[sp] = sp
    str = ""
    for sp in dic:
        if str == "":
            str = sp
            continue
        str = str + " " + sp
    return str


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))