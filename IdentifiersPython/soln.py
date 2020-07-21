VAL = 5 # can change this
f = open("lists.py", "w")
for i in range(1, VAL + 1):
    f.write("list" + str(i) + " = []\n")
f.close()
