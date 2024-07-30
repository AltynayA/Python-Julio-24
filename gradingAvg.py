if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    counter = 0
    for i in range(3):
        #counter += scores[i]
        counter += student_marks[query_name][i]
    counter = counter/3
    print("{:.2f}".format(counter))
