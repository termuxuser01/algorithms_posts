import json

with open('linux.json', 'r') as f:
    linux_distros = json.load(f)

distros_list = list()

for distro in linux_distros:
    distros_list.append(distro['Name'])

sorted_distros = sorted(distros_list)

def contains(elements, value):
  lower, upper = 0, len(elements) -1
  print(elements)
  
  if lower <= upper:
    middle = (lower + upper) // 2

    if elements[middle] == value:
      return True
    
    elif elements[middle] < value:
      return contains(elements[middle + 1:], value)
    elif elements[middle] > value:
      return contains(elements[:middle], value)

  return False

print(contains(sorted_distros, "Debian"))

def contains(elements, value):
  def recursive(lower, upper):
    if lower <= upper:
      middle = (lower + upper) // 2

      if elements[middle] == value:
        return True
      
      elif elements[middle] < value:
        return recursive(middle + 1, upper)
      elif elements[middle] > value:
        return recursive(lower, middle - 1)

    return False

  return recursive(0, len(elements) - 1)

print(contains(sorted_distros, 'CentOS'))     
print(contains(sorted_distros, 'Knoppix'))     
