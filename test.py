#test
'''
with open("requirements.txt") as f:
    content = f.readlines()
    li = [x.strip() for x in content]
print(li)
'''

'''
with open("requirements.txt") as f:
    lines = [line.rstrip() for line in f]
print(lines)
'''
'''
with open("requirements.txt") as f:
    requirement = []
    for line in f:
        requirement.append(line.strip('\n'))
print(requirement)
'''

requirements_list = ([lines.strip() for lines in open("requirements.txt")])
print(requirements_list)