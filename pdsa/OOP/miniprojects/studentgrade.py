print("Jesus is lord and wellcome to leli's student grading system")
# A system that help to enhance the education 
# having add Students
# view ,update ,delete,add_grades, Calculate gpa,Display_info
class Students:
    def __init__(self,Fisrt_name ,second_name,age, id,grades):
        self.fn= Fisrt_name
        self.sn= second_name
        self.age = age
        self.id =id
        self.which_class = grades
        self.subject = []
    
    def add_subject(self ,subject_name , score,credit_hour,ects):
        grade = Grade(score)
        subject = Subject(subject_name,credit_hour ,ects)
        self.subject.append(subject)

    def calculate_gpa(self):
        if not self.subject:
            return 0.0
        total_gpa = sum(Grade.grade_in_gpa() for subject in self.subject )
        return round(total_gpa/len(self.subject),2)
    
    def display_info(self ):
        print("\n🎓 Student Information")
        print(f"First Name: {self.fn}")
        print(f"Second Name: {self.sn}")
        print(f"ID: {self.id}")
        print(f"Age: {self.age}")
        print("Subjects:")
        if not self.subject:
            print("  No subjects yet.")
        else:
            for subject in self.subject:
                subject.define_sub()
        print(f"GPA: {self.calculate_gpa()}")


class Subject:
    def __init__(self,sub_name,credit_hour ,ects):
        self.sub_name = sub_name 
        self.credit_hour = credit_hour 
        self.ects = ects

    def define_sub(self):
        print(f"The subject name is {self.sub_name}\n It has credit hour of {self.credit_hour}\t and it has an ects of {self.ects}.")        


class Grade:
    def __init__(self,score ):
        self.score = score
    
    def grade_in_letterform(self):
        if self.score>=90:
            return 'A'
        elif self.score>=80:
            return 'B'
        elif self.score>=70:
            return 'C'
        elif self.score>=60:
            return 'D'
        else:
            return 'F'
    def grade_in_gpa(self):
        if self.score >= 90:
            return 4.0
        elif self.score >= 80:
            return 3.0
        elif self.score >= 70:
            return 2.0
        elif self.score >= 60:
            return 1.0
        else:
            return 0.0
    
class StudentManager:
    def __init__(self):
        self.students = {}
    
    def add_student(self, student):
        self.students[student.id] = student
        print(f"✅ Student '{student.fn} {student.sn}' added.")
    
    def find_student(self, student_id):
        return self.students.get(student_id)
    
    def view_all(self):
        if not self.students:
            print("No students available.")
        else:
            for student in self.students.values():
                student.display_info()
    
    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("🗑️ Student deleted.")
        else:
            print("❌ Student not found.")

def main():
    manager = StudentManager()
    
    while True:
        print("\n===== 🎓 Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Add Subject and Grade")
        print("4. Calculate GPA")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            sid = input("Enter Student ID: ")
            first_name = input("Enter Name: ")
            second_name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grade = int(input("enter the which class he or she is :"))
            s = Students(first_name,second_name,age, sid,grade)
            manager.add_student(s)
        
        elif choice == "2":
            manager.view_all()
        
        elif choice == "3":
            sid = input("Enter Student ID: ")
            student = manager.find_student(sid)
            if student:
                subject = input("Enter Subject Name: ")
                score = float(input("Enter Score: "))
                credit_hour = int(input("Enter Credit Hour: "))
                ects = int(input("Enter ECTS: "))
                student.add_subject(subject, score, credit_hour, ects)
            else:
                print("❌ Student not found.")
        
        elif choice == "4":
            sid = input("Enter Student ID: ")
            student = manager.find_student(sid)
            if student:
                print(f"{student.fn}'s GPA = {student.calculate_gpa()}")
            else:
                print("❌ Student not found.")
        
        elif choice == "5":
            sid = input("Enter Student ID: ")
            manager.delete_student(sid)
        
        elif choice == "6":
            print("👋 Exiting...")
            break
        
        else:
            print("❌ Invalid choice.")
if __name__ == "__main__":
    main()