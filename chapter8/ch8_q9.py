with open('sample.txt', 'r') as f:
    data_list = f.readlines()
    sum_of_data = 0
    for data in data_list:
        sum_of_data += int(data)
    print("합계: %d" % sum_of_data)
    print("평균: %.2f" % float(sum_of_data / len(data_list)))
