# CMP 269: Programming Methods III [cite: 1]
# Python Introduction Exercises - Mister White [cite: 1]

def exercise_1_basics():
    course = "CMP 269"
    students = 28

    # TODO: Print "The course [course] has [students] students." [cite: 5]
    print(f"The course {course} has {students} students.")

def exercise_2_collections():
    colors = ["red", "blue", "green", "black", "white"]

    colors.append("purple")
    student_data = {"name": "Jane Doe", "gpa": 3.8}

def exercise_3_logic():
    numbers = [1, 5, 8, 12, 15, 22, 33, 40]
    evens = []

    for num in numbers:
        if num % 2 == 0:
            evens.append(num)

if __name__ == "__main__":
    print("--- Exercise 1 ---")
    exercise_1_basics()
    print("\n--- Exercise 2 ---")
    exercise_2_collections()
    print("\n--- Exercise 3 ---")
    exercise_3_logic()