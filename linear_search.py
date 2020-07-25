# note: this code uses data from random_search example

def linear_search(elements, value):
  for index, element in enumerate(elements):
    if element == value:
      return "found {} at index {}".format(element, index)

print(linear_search(sorted_distros, 'Fedora'))
print(linear_search(distros_list, 'Fedora'))
