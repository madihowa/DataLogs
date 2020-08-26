import matplotlib.pyplot as plt

fname="DataLog(E).txt"
#countb=[]
#counta=[]


with open(fname, "r+") as f:
    d = f.readlines()
    f.seek(0)
    for i in d:
        num=i.count(' ')
 #       countb.append(num)
        if num == 3:
            f.write(i)
 #           counta.append(num)
    f.truncate()

"""
#test after
plt.scatter([i for i in range(len(countb))], countb, label="before")
plt.scatter([i for i in range(len(counta))], counta, label="after")
plt.xlabel("Line Number")
plt.ylabel("Number of Columns")
plt.legend()
plt.show()
"""

