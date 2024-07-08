data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]
clean_data_list=[]
for data in data_list:
  try:
    clean_data_list.append(int(data))
  except:
    continue
print(clean_data_list)