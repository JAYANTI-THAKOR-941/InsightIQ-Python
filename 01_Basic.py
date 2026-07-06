# Basic Python Program
studentId = 111
studentName = "Jayanti Thakor"
courseName = "Python Programming"
courseFees = 32000.99
courseDuration = 3.5
isAvailble = False
pythonLibrary = ["Numpy","Pandas","Seaborn","Matplotlib"]
studentAddress = {
    "city":"Gandhinagar",
    "state":"Gujarat",
    "pincode":382650
}

print("||-==== STUDENT INFO ====---||")
print("studentId:",studentId)
print("studentName:",studentName)
print("courseName:",courseName)
print("courseFees:",courseFees)
print("courseDuration:",courseDuration)

if(isAvailble):
    print("Course is available.!")
else:
    print("Course is not available")

print(pythonLibrary)

print(studentAddress)