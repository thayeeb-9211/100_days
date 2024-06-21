# You are going to write a program that calculates the highest score from a List of scores.
# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# Important: you are not allowed to use the max or min functions. The output words must match the example. i.e

# The highest score in the class is: x

# Example Input
# 78 65 89 86 55 91 64 89
# In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]
# Example Output
# The highest score in the class is: 91


# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

highest = 0
for high in student_scores:
  if high > highest:
    highest = high
print(f"The highest score in the class is: {highest}")

# alterantive_method..

student_scores = input("Input a list of student scores: \n>> ").split()
print(student_scores)

high_score = 0
for score in student_scores:
    score = int(score)
    if score > high_score:
        high_score = score

print(f"The highest student score is: {high_score}")