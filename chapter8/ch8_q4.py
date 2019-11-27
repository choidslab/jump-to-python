A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

target_data = list(filter(lambda x: x >= 50, A))

print(target_data)
print(sum(target_data))