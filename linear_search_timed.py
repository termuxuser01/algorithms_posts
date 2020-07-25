import timeit

a = '#' * 50
print(a)
print('unsorted time:\t', end='')

print(timeit.timeit('''

def linear_search(elements, value):
  for index, element in enumerate(elements):
    if element == value:
      return "found {} at index {}".format(element, index)


distros_list = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch Linux', 'Gentoo']

linear_search(distros_list, 'Fedora')
'''))

print(a)
print('sorted time:\t', end='')


print(timeit.timeit('''

def linear_search(elements, value):
  for index, element in enumerate(elements):
    if element == value:
      return "found {} at index {}".format(element, index)


sorted_distros = ['Arch Linux', 'CentOS', 'Debian', 'Fedora', 'Gentoo','OpenSUSE', 'Ubuntu']

linear_search(sorted_distros, 'Fedora')
'''))

print(a)
