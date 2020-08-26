import matplotlib.pyplot as plt


fname="DataLog(E).txt"
file=open(fname, "r")
#lines= file.readlines()
faulty=[]
count=[]
"""
#for x in lines:
for line_num, x in enumerate(file):
    num=x.count(' ')
    if num!=3:
        print(line_num)
        faulty.append(line_num)
    count.append(num)
file.close()
"""

#deletes line
initial_line = 1
file_lines = {}
with open(fname) as f:
    content = f.readlines() 

for line_num, line in enumerate(content):
    num= line.count(' ')
    if num!=3:
        faulty.append(line_num)
    count.append(num)

for line in content:
    file_lines[initial_line] = line.strip()
    initial_line += 1

print(faulty)

f = open(fname, "w")
for line_number, line_content in file_lines.items():
    if line_number not in faulty:
        f.write('{}\n'.format(line_content))

f.close()
print('Deleted line: {}'.format(faulty))


#test after
#"""
file=open(fname, "r")
for line_num, x in enumerate(file):
    num=x.count(' ')
    if num!=3:
        print(line_num)
        faulty.append(line_num)
    count.append(num)
file.close()
plt.scatter([i for i in range(len(count))], count)
plt.xlabel("Line Number")
plt.ylabel("Number of Columns")
plt.show()
#"""

