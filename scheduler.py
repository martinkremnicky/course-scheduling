import itertools


# Each course is a tuple: (course_name, quarter, is_mandatory, credits, time_slot)
courses = [
    ("course1", 1, True, 5, 'A'),
    ("course2", 1, False, 5, 'B'),
    ("course3", 1, False, 5, 'C'),
    ("course4", 1, False, 5, 'C'),
    ("course5", 2, False, 5,'A'),
    ("course6", 2, False, 5,'B'),
    ("course7", 2, False, 5,'E'),
    ("course8", 3, False, 5,'B'),
    ("course9", 3, False, 5,'D'),
    ("course10", 3, False, 5,'C'),
    ("course11", 4, False, 5,'B'),
    ("course12", 4, False, 5,'A'),
    ("course13", 4, False, 5,'A'),
]

def get_combinations(courses, mandatory_courses, target_sums):
    for r in range(1, len(courses) + 1):
        for subset in itertools.combinations(courses, r):
            full_subset = mandatory_courses + list(subset)
            credit_sum = sum(course[3] for course in full_subset)
            time_slots = [course[4] for course in full_subset]
            if credit_sum in target_sums and len(set(time_slots)) == len(time_slots):
                yield (credit_sum, full_subset)

def extract_quarter(courses, quarter):
    quarter_courses = []
    for course in courses:
        if course[1] == quarter:
            quarter_courses.append(course)
    return quarter_courses

def extract_mandatory(courses):
    mandatory_courses = []
    for course in courses:
        if course[2] == True:
            mandatory_courses.append(course)
    return mandatory_courses

def generate_quarter(courses, quarter):
    quarter_courses = extract_quarter(courses, quarter)
    mandatory_courses = extract_mandatory(quarter_courses)
    optional_courses = list(set(quarter_courses) - set(mandatory_courses))
    return get_combinations(optional_courses, mandatory_courses, {10,15})

quarter_courses = generate_quarter(courses,1)

for credit_sum, combo in generate_quarter(courses, 2):
    print(f"Combination: {combo}, Credits: {credit_sum}")