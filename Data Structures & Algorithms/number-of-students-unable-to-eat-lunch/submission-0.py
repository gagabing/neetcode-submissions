class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n_stud = len(students)
        i_stud, i_sand, tries = 0, 0, n_stud

        while tries > 0:
            if students[i_stud] == sandwiches[i_sand]:
                i_stud += 1
                i_sand += 1
                n_stud -= 1
                tries = n_stud
            else:
                students.append(students[i_stud])
                i_stud += 1
                tries -= 1
        return n_stud
