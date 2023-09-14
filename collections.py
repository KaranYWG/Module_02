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

# dictionary
# key value pair
# not ordered
# {}
fruit_dictionary = {'apples': 23 , 'bananas': 59 , 'oranges' : 10 }

print(fruit_dictionary[ 'apples']) #23

fruit_dictionary['apples'] = 100
print(fruit_dictionary)

fruit_dictionary['plums'] = 49
print(fruit_dictionary)

print(fruit_dictionary.keys())
print(fruit_dictionary.values())


# print(fruit_dictionary['bbbbbbb'])

print(fruit_dictionary.get('bbbbbbbb' , 'not found'))
print(fruit_dictionary.get('bananas' , 'not found'))


fruit_dictionary['banana'] = 500

print(fruit_dictionary)

fruit_dictionary.pop('apples')
print(fruit_dictionary)

fruit_dictionary.clear()


# sets
# unordered
# every element is unique
# muables
# tuples starts with {}

# SETS

primes = {2, 3, 5, 7, 11, 13, 17, 19, 23 }

# fives = {} this will produce an empty dictionary
fives = set() # uses the sets function to create an empty repository
 
fives.add(5)
fives.add(10)
fives.add(15)
fives.add(20)

print(primes)
print(fives)

primes.remove(13)
 # primes.remove(100)

primes.discard(11)
primes.discard(100)

print(primes)
print(fives)

union = primes.union(fives)
print(union)


common = primes.intersection(fives)
print(common)

primes_difference = primes.difference(fives)
print(primes_difference)




