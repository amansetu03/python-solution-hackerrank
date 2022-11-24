if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    m=0
    p=0
    for i in student_marks[query_name]:
        m=m+i
        p+=1
    s=m/p
    print("{:.2f}".format(s))
