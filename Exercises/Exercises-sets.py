# Exercise 1. Remove duplicates from list:
my_list = [1,2,3,5,6,7,7,8,9,9,9]
my_set = set(my_list)
my_list_no_duplicates = list(my_set)
print(my_list_no_duplicates)

# Exercise 2. We have a database of school students:
school = {'Sam','Randy','Jam','Molly','Dan'}
# The teachers take attendance and compile it into a list. 
attendance_list = ['Jam', 'Dan', 'Molly']
# Create a piece of code to find out which students missed class. It should be the set
print(school.difference(attendance_list))
# or
# if you want to get result in list:
# missing_students = []
# for student in school:
#   if student not in attendance_list:
#     missing_students.append(student)
# print(missing_students)
