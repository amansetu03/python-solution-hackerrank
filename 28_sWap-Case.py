def swap_case(s):
    m=""
    for i in s:
        if i==i.upper():
            i=i.lower()
            m=m+i
        else:
            i=i.upper()
            m=m+i
    return m

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)