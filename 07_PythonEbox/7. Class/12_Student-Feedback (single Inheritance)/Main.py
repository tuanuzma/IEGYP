class Student:
    def __init__(self, id, name, department, courseId):
        self.id = id
        self.name = name
        self.department = department
        self.courseId = courseId

    def __str__(self):
        return (
            f"Student :\n"
            f"Id :  {self.id}\n"
            f"Name :  {self.name}\n"
            f"Department :  {self.department}\n"
            f"Course Id :  {self.courseId}"
        )


class StudentRating:
    def __init__(self, id, review, stars, student):
        self.id = id
        self.review = review
        self.stars = stars
        self.student = student

    def __str__(self):
        return (
            f"{self.student}\n"
            f"Rating ID :  {self.id}\n"
            f"Review :  {self.review}\n"
            f"Rating Stars :  {self.stars}"
        )


# Main function to handle input and output
def main():
    print("Enter the student id")
    student_id = int(input())
    print("Enter the student name")
    student_name = input()
    print("Enter the department")
    department = input()
    print("Enter the course id")
    course_id = int(input())

    # Create Student instance
    student = Student(student_id, student_name, department, course_id)

    print("Enter the Rating id")
    rating_id = int(input())
    print("Enter review")
    review = input()
    print("Enter number of stars")
    stars = int(input())

    # Create StudentRating instance
    student_rating = StudentRating(rating_id, review, stars, student)

    # Display the details
    print(student_rating)


if __name__ == "__main__":
    main()   