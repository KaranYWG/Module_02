"""
Descriptionm: To demonstrate python collection types.
Author: Karanpreet Singh
Date: September 13, 2023
Usage: Run using the play button in the IDE.
"""

# lists 
# a list of integers
daily_step_count = [10343, 93885, 7029, 10931, 5921]

employee_data = ["A123", 55024.24, 47, True]

list_of_lists = [["A", "B", "C", ], [1, "x", True], [False, 12, 5.5]]

print(daily_step_count[2])
daily_step_count[4] = 100
print(daily_step_count)

daily_step_count.append(8694)

print(daily_step_count)

# inserts the value 4473 before current element 3
daily_step_count.insert(3, 4473)
print(daily_step_count)

# removes the first instance of 7029 from the list
daily_step_count.remove(7029)
print(daily_step_count)

# pop removes the last element of the list 
popped = daily_step_count.pop()
print(daily_step_count)
print(popped)

# returns the index value of the element matching the arguement
index_value = daily_step_count.index(100)
print(index_value)

"""index_value = daily_step_count.index(55555555)"""

# index_value_ = daily_step_count.index(55555555)
daily_step_count[2] = 5555
daily_step_count[3] = 5555

# count returns the number of instances of a specific value in the list
count_5555 = daily_step_count.count(5555)

print(count_5555)

print(daily_step_count)
daily_step_count.sort()
print(daily_step_count)

# reverse reverses the list
daily_step_count.reverse()
print(daily_step_count)

#  Slicing
red_river_college = "RRC Polytechnic"
red_river_list = list(red_river_college)
print(red_river_list)

# start, stop, step
print(red_river_list[2: 12: 2])
print(red_river_list[: 10: 1])

# o t h c
print(red_river_list[5: : 3])

# R o c
print(red_river_list[::5])

# c
print(red_river_list[-1])

# c i n h 
print(red_river_list[-1: -5: -1])

#
provinces = ('BC', 'AB', 'MB', 'SK')
print(provinces[2])

# tuples are immutable. The only way to change a value is to redefine the tuple
# provinces = ('BC', 'AB', 'Manitoba', 'SK')

single_string = ('string')
print("single_string: " , type(single_string))

single_tuple = ('one_item')
print("single_tuple:" , type(single_tuple))

random_tuple = (1, 66, 3, 7, 42, 78, 12, 55)
length = len(random_tuple)
print(length)

maximum = max(random_tuple)
minimum = min(random_tuple)
print("max: ", maximum, "min: ", minimum) 

sum = sum(random_tuple)

# returns the sorted list
sorted_list = sorted(random_tuple)
print(sorted_list)

list_of_numbers = [1, 2, 3]
tuple_of_numbers = tuple(list_of_numbers)
print(list_of_numbers)
print(tuple_of_numbers)