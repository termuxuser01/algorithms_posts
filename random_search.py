import json

with open('linux.json', 'r') as f:
  linux_distros = json.load(f)

distros_list = list();

for distro in linux_distros:
  distros_list.append(distro['Name'])

sorted_distros = sorted(distros_list)



import random

def random_search(elements, value):
  while True:
    if random.choice(elements) == value:
      return 'Found item {}'.format(value)


print(random_search(distros_list, 'Debian'))
print(random_search(sorted_distros, 'Debian'))
