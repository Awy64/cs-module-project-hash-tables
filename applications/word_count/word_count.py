def word_count(s):
    # Your code here
    sl = s.lower()
    punc = '":;,.-+=/\|[]{}()*^&'
    for i in punc:
        sl = sl.replace(i, "")
    spl = sl.split()
    dic = dict()
    for i in spl:
        if i in dic:
            dic[i] = dic[i] + 1
        else:
            dic[i] = 1
    return dic



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))