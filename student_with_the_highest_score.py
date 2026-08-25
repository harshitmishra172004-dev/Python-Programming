score ={'Ekta': 85, 'Manan': 90, 'Mahak': 78, 'Harshit': 95}

highest_student = max(score, key=score.get)
print("Student with highest score:",
      highest_student)