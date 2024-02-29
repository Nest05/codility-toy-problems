def grader(subject_one, subject_two, subject_three, subject_four, subject_five):
    grade = ""

    total = subject_one+ subject_two+ subject_three+ subject_four+ subject_five

    average_score = total/5

    print(average_score)

    if average_score >= 80:
        grade = "A"
    elif average_score >= 60:
        grade = "B"
    else:
        grade = "FAIL"

    return grade

print(grader(60,90,70,40,75))


full_name = "Nestor Masinde"


for i in full_name:
    
    print(i.upper())

n = 0

while n <= 10:
    print ("I am being executed")
    n += 1

for x in range(10):
    if x == 7:
        print(x)
        break
    continue