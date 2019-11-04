grades_file = open('grades.csv', 'r')

grades_file.readline()

for line in grades_file.readlines():
    l = line.split(",")
    for i in range(len(l)):
        l[i] = l[i].strip()
    l[3] = float(l[3])
    print(l)