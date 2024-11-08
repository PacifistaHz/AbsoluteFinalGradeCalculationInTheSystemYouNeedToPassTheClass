midterm=input("Enter the midterm note: ")
final=input("Enter the final note: ")
midterm=float(midterm)
final=float(final)

passingGrade=midterm * 0.4 + final * 0.6
situation=""
if passingGrade>70:
    situation="Passed"
else:
    situation="Failed"

print("Passing Grade: {0}".format(passingGrade))
print("Your situation is: {0}".format(situation))