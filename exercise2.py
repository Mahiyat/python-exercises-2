def count_char(rhyme):
  count_dict = {}
  for ch in rhyme:
    if ch in count_dict:
      count_dict[ch]+=1
    else:
      count_dict[ch]=1
  # print(count_dict)
  count_list = list(count_dict.values())
  max_count = max(count_list)
  most_frequent_chars = []
  for key, value in count_dict.items():
    if value == max_count:
      most_frequent_chars.append(key)
  print("Most frequent characters: ", most_frequent_chars)
  print("Number of occurance: ", max_count)


rhyme = 'Twinkle, twinkle, little star. How I wonder what you are!'
print("Considering white spaces and punctuations: ")
count_char(rhyme)
space_and_punctuation = [' ', ',', '.', '!']
for ch in space_and_punctuation:
  rhyme = rhyme.split(ch)
  rhyme = ''.join(rhyme)
print("Without considering white spaces and punctuations (case-sensitive): ")
count_char(rhyme)
rhyme = rhyme.lower()
print("Without considering white spaces and punctuations (case-insensitive): ")
count_char(rhyme)
