course_schedule = {
    "CS" : 2110,
    "FREN" : 2010,
    "MUSI" : 3320,
    "ASTR" : 3240
}


def print_schedule():
    for dept in course_schedule:
        print(dept, course_schedule[dept])


def get_course(department):
    return course_schedule[department]


def add_course(department, number):
    if department in course_schedule:
        return False
    course_schedule[department] = number
    return True


def drop_course(department):
    if department in course_schedule:
        course_schedule.pop(department)


def change_course(department, number):
    if department not in course_schedule:
        return False
    course_schedule[department] = number
    return True


print(add_course("STS", 2600))
drop_course("FREN")
drop_course("APMA")
print(change_course("CS", 2102))
print(change_course("APMA", 3100))
print_schedule()
print(get_course("CS"))


def combine_dictionaries(a, b):
    out = {}
    for k in a:
        out[k] = a[k]
    for k in b:
        if k in out:
            if out[k] != b[k]:
                out[k] = "ERROR"
        else:
            out[k] = b[k]
    return out



dict_a = {"2+2": 4, "3+3": 6, "hot":"cold"}
dict_b = {"2+2": 4, "3+3": 7, "high":"low"}

print(combine_dictionaries(dict_a, dict_b))
print(dict_a, dict_b)
