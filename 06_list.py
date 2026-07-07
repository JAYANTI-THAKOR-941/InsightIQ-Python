# LIST IN PYTHON
courses = ["Python","Full Stack Development","InsightIQ","Numpy","Pandas"]
print(courses)
# print(type(courses))
# print("My course is:",courses[2])

# for x in courses:
#     print(x)

# print(courses[1:4])

# if "Numpy" in courses:
#     print("Numpy is available..!!")
# else:
#     print("Not available....!")


# INSERT DATA IN LIST

courses.append("Matplotlib")

courses.insert(1,"Frontend Development")

basicCourses = ["CCC","Tally","Hardware"]

courses.extend(basicCourses)

print(courses)


# REMOVE DATA FROM LIST
# courses.remove("CCC")
# courses.pop(1)
# del courses[1]
# del courses
courses.clear()
print(courses)


