# LabTeacherApplication


PROBLEM STATEMENT
Write an application to help with the management of laboratory activities for a faculty course.
Students enrolled in the class can be assigned one of the problem statements
from each laboratory, and when they turn it in they are graded. The application will be used by the teacher and
will provide the following functionalities:
- Add a student to the course. Each student has an id, a name and a group. You cannot have more than
one student having the same id, as well as students without a name or group.
- Remove a student from the course. A student can only be removed while they have not received any
grades.
- Assign a laboratory problem statement to a student. You cannot assign more than one problem
statements from the same laboratory to a student. If the student was already assigned a problem, the
program must report the error.
- Assign a laboratory to a group. Each student in the group will be assigned a problem statement.
Implement an algorithm to assign students with problem statements (e.g. each subsequent student is
assigned the next problem in the list of problem statements). In case a student was already assigned a
problem statement, this must not be changed!
- Grade a student for a laboratory, with an integer grade 1 to 10. Validate that the grade is valid. Grades
cannot be changed!
- Best/worst students in a group. Given a group, list its students in decreasing order of their average
grade.
- Students failing the class. Provide the list of all the students (regardless of group), for whom the average
grade is less than 5.
- Undo/redo the last performed operation that changes the list of students or grade assignments.
