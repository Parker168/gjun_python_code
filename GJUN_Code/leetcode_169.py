from collections import Counter # class
list_nums = [1,1,2,2,3,3,4,5,6,7,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]
number_counter = Counter(list_nums)  # instance 實體

print(number_counter, len(list_nums))
print("most_common(1): ", number_counter.most_common(1))
print("most_common(1)[0]: ", number_counter.most_common(1)[0])
print("most_common(1)[0][0]: ", number_counter.most_common(1)[0][0])