grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
st_1_av = sum(grades[0])/len(grades[0])  # среднее значение для первого студента
st_2_av = sum(grades[1])/len(grades[1])
st_3_av = sum(grades[2])/len(grades[2])
st_4_av = sum(grades[3])/len(grades[3])
st_5_av = sum(grades[4])/len(grades[4])
students_sort = sorted(list(students))  # перевод из множества в список с последующей сортировкой по алфавиту
students_av = {students_sort[0]: st_1_av, students_sort[1]: st_2_av, students_sort[2]: st_3_av,
               students_sort[3]: st_4_av, students_sort[4]: st_5_av}  # создание словаря по имени из списка и вычисленному значению
print(students_av)
