input_data = input("입력: ")
preprocessed_data = input_data.split(',')

sum = 0
for item in preprocessed_data:
    sum += int(item)

print(sum)
