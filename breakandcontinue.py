students = ["ram","shyam","sita","radha","krishna"]

for student in students:
    if student == "radha":
        break;
    print(student)

for student in students:
    if student == "radha":
        continue;
    print(student)