def calc_avg(marks):
  f=False
  for mark in marks:
    if mark<40:
      f=True
      break
  if f == True:
    return "Failed"
  else:
    avg=sum(marks)/len(marks)
    return avg
  
student_1 = [40, 35, 70, 90, 56]
student_2 = [57, 35, 80, 98, 46]

print("Average Marks of Student1: ", calc_avg(student_1))
print("Average Marks of Student2: ", calc_avg(student_2))