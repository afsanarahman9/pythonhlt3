import random
permarks = int(input("enter the percentage marks "))
target_grade = int(
    input("enter the target grade, for grade a-1, grade b-2,c-3,f-4 **"))


def mark_grade(permarks):

    if (permarks > 40 and permarks < 60):
        mark_grade = "c"
    elif (permarks > 60):
        mark_grade = "b"
    elif (permarks > 80):
        mark_grade = "a"
    else:
        mark_grade = "f"

        return mark_grade(permarks)

        mark_grade(permarks)


if (target_grade < permarks):
    print("well done")
elif (target_grade > permarks):

    print("you can improve next time")
else:
    print("you got what you expected")
