import json

with open('linux.json', 'r') as f:
    linux_distros = json.load(f)

distros_list = list()

for distro in linux_distros:
    distros_list.append(distro['Name'])

sorted_distros = sorted(distros_list)

print(sorted_distros)

import bisect

print(bisect.bisect_left(sorted_distros, 'Gentoo'))
print(bisect.bisect_left(sorted_distros, 'Knoppix'))


def binary_search(elements, value):
    index = bisect.bisect_left(elements, value)
    try:
        if index <= len(elements) and elements[index] == value:
            print("{} found at index {}!".format(value, index))
    except IndexError:
        return None


print(binary_search(sorted_distros, 'Ubuntu'))
print(binary_search(sorted_distros, 'zebra'))

bisect.insort(sorted_distros, 'Knoppix')

print(sorted_distros)

from dataclasses import dataclass, field


@dataclass(order=True)
class Person:
    name: str
    num: int = field(compare=False)

    def __repr__(self):
        return f'{self.name}({self.num})'


p1 = Person('Hank', 1)
p2 = Person('Hank', 2)

print(p1 == p2)

print(p1 is p2)

p3, p4 = Person('Alice', 3), Person('Bob', 3)

print(p3 < p4)

sorted_people = [Person('Alice', 1)]
bisect.insort_left(sorted_people, Person('Alice', 2))
bisect.insort_right(sorted_people, Person('Alice', 3))

print(sorted_people)


def find_index(elements, value):
    lower, upper = 0, len(elements) - 1

    while lower <= upper:
        middle = (upper + lower) // 2

        if elements[middle] == value:
            return f'found {elements[middle]} in index {middle}'
            break
        elif elements[middle] < value:
            lower = middle + 1
        elif elements[middle] > value:
            upper = middle - 1
            print(upper)


print(find_index(sorted_distros, 'Gentoo'))

distros_by_chars = sorted(distros_list, key=len)


# add this
def find_by_key(elements, value, key):
    lower, upper = 0, len(elements) - 1

    while lower <= upper:
        middle = (lower + upper) // 2
        # and this
        middle_element = key(elements[middle])

        if middle_element == value:
            return middle

        elif middle_element < value:
            lower = middle + 1
        elif middle_element > vaule:
            upper = lower - 1


print(find_by_key(distros_by_chars, key=len, value=10))

from collections import namedtuple

People = namedtuple('People', 'name lastname')

people = [
    People('Bob', 'Williams'),
    People('John', 'Doe'),
    People('Paul', 'Brown'),
    People('Alice', 'Smith'),
    People('John', 'Smith'),
]


from operator import attrgetter

firstname = attrgetter('name')
lastname = attrgetter('lastname')

people_by_first = sorted(people, key=firstname)
people_by_last = sorted(people, key=lastname)

print(find_by_key(people_by_last, key=lastname, value='Smith'))

def find_left(elements, value, key):
  index = find_by_key(elements, value, key)

  if key is not None:
    while index >= 0 and key(elements[index]) == value:
      index -= 1
    index += 1
  
  return index

def find_right(elements, value, key):
  index = find_by_key(elements, value, key)

  if key is not None:
    while index >= 0 and key(elements[index]) == value:
      index += 1
    index -= 1
  
  return index

print(find_right(people_by_last, key=lastname, value='Smith'))

def find_all(elements, value, key):
  left = find_left(elements, value, key)
  right = find_right(elements, value, key)
  if left and right:
    return set(range(left, right + 1))
  else: 
    return set()

print(find_all(people_by_last, key=lastname, value='Smith'))
