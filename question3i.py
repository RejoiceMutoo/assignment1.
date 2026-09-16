students = {"Joanne":88, "Dexter":85, "Hazel":70, "Tiana":65, "Trevor":55}
for name ,marks in students.items():
    print(name,":",marks)
    top_student =max(students,key=students.get)
    print("top_student:",top_student)
    print("highest mark:",students[top_student])