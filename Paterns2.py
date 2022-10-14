from datetime import datetime
from typing import List, Any
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class PersonalInfo:
    """Data class with personal information"""

    id: int
    name: str
    adress: str
    phone_number: str
    email: str
    position: int
    rank: str
    salary: float


class Department:
    def __init__(self, title: str):
        self.title = title
        self.students: List[Student] = []
        self.professors: List[Professor] = []
        self.courses: List[Course] = []
        self.requests: List[str] = []
        self.ill_person: List[str] = []

    def get_ill_person(self):
        """Return a list of ill person"""
        return self.ill_person

    def get_requests(self):
        """Return a list of requests"""
        return self.requests


class Staff(ABC):
    def __init__(self, _pesonal_info: PersonalInfo):
        self._persoanl_info = _pesonal_info

    @abstractmethod
    def ask_sick_leave(self, department: Department) -> bool:
        pass

    @abstractmethod
    def send_request(self, department: Department) -> bool:
        pass


class CourseProgress:
    def __init__(
        self,
        received_marks: dict,
        visited_lectures: int,
        completed_assigments: dict,
        notes: dict,
    ):
        self.received_marks = received_marks
        self.visited_lectures = visited_lectures
        self.completed_assigments = completed_assigments
        self.notes = notes

    def get_progress_to_date(self, date: datetime):
        pass  # to do

    def get_final_mark(self):
        """The sum of grades is divided by their number to determine the final grade"""
        final_mark = sum(self.received_marks.values()) / len(self.received_marks)
        return final_mark

    def fill_notes(self):
        """In the cycle, you need to enter the text 5 times, it adds this text to the notes"""
        i = 0
        while i <= 5:
            text = input()
            self.notes[i] = text
            i += 1

    def remove_note(self):
        """Clearing array with notes"""
        self.notes.clear()


class Course:
    def __init__(
        self,
        title: str,
        star_date: datetime,
        end_date: datetime,
        description: str,
        lectures: list[str],
        assigments: list[str],
        limit: int,
    ):
        self.title = title
        self.start_date = star_date
        self.end_date = end_date
        self.description = description
        self.lectures = lectures
        self.assigments = assigments
        self.limit = limit
        self.students = []
        self.seminars: List[int] = []

    # Returns a list of students from the course
    def check_students(self):
        """Returns the list of students enrolled in the course"""
        return self.students


class Seminar:
    def __init__(
        self,
        id: int,
        title: str,
        deadline: datetime,
        assignments: List[dict],
        status: Any,
        related_course: str,
    ):
        pass

    def implement_item(item_name: str) -> str:
        pass


class Student(Staff):
    def __init__(
        self,
        name: str,
        address: str,
        phone_number: str,
        email: str,
        course_progress: CourseProgress,
    ):
        self._personal_info = PersonalInfo(
            None, name, None, None, None, None, None, None
        )
        self.average_mark = 0.0
        self.course_progress = course_progress
        self.courses = []

    def ask_sick_leave(self, department: Department):
        """Add student name to list of ill person and allow not to go to class"""
        department.ill_person.append(f"student {self._personal_info.first_name} is ill")
        print(f"{self._personal_info.first_name} you can not go to class today")

    def send_request(self, department: Department):
        """Add student request to list of requests"""
        reques = input("Write your request:")
        department.requests.append(
            f"Student {self._personal_info.first_name} want to {reques}"
        )

    def taken_course(self):
        """Returns the courses for which the student is enrolled"""
        return self.courses


class PostGraduateStudent(Student):
    def __init__(self, phd_status: str):
        self.phd_status = phd_status


class Professor:
    def __init__(
        self, name: str, address: str, phone_numer: str, email: str, salary: float
    ):
        self._personal_info = PersonalInfo(
            None, name, None, None, None, None, None, None
        )

    def check_assignment(self, assigment: dict):
        """Checks the assignment and assigns a grade for it"""
        if assigment["is_done"]:
            assigment["mark"] = 5.0
        else:
            assigment["mark"] = 1.0
        print(f"{self._personal_info.first_name} check your assigment")
        print(f"Your mark:{assigment['mark']}")

    def request_support(self):
        pass

    def add_postgraduate_student(self, student: PostGraduateStudent):
        pass

    def ask_sick_leave(self, department: Department) -> bool:
        """Add professor name to list of ill person and allows not to conduct the lesson if he finds a replacement"""
        department.ill_person.append(
            f"Professor {self._personal_info.first_name} is ill"
        )
        print(f"{self._personal_info.first_name} you must find a replacement")

    def send_request(self, department: Department) -> bool:
        """Add professor request to list of requests"""
        reques = input("Write your request:")
        department.requests.append(
            f"Professor {self._personal_info.first_name} want to {reques}"
        )


class Enrollment:
    @staticmethod
    def enroll(course: Course, student: Student):
        """If there are places for the course add student name to list of students on the course and course title to list of courses"""
        if (
            course.limit > len(course.students)
            and student._personal_info.name not in course.students
        ):
            course.students.append(student._personal_info.name)
            student.courses.append(course.title)
            print(
                f"Student {student._personal_info.name} as been added to the course {course.title}"
            )
        else:
            print("Too many students or this student is already in the course")

    @staticmethod
    def unenroll(course: Course, student: Student):
        """Remove students from the course and course title from students courses"""
        course.students.remove(student._personal_info.name)
        student.courses.remove(course.title)
        print(f"{student._personal_info.name} remove from course {course.title}")


assigment_1 = {
    "title": "assigment_1",
    "deskription": "deskription_1",
    "is_done": True,
    "mark": 0.0,
}
student1 = Student("Taras", "ds", "dsds", "dsds", None)
course1 = Course("Programing", None, None, None, None, None, 10)
professor1 = Professor("Oleh", None, None, None, None)
department1 = Department("LNY department")
# student1.send_request(department1)
# print(department1.get_requests())
Enrollment.enroll(course1, student1)
Enrollment.unenroll(course1, student1)
