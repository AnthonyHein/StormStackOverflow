with open('xy.txt', 'r') as f:
    xy = [line.strip() for line in f]

# Take the list of strings, where integers separated by space, and make a list of tuples of integers.
# For each line, separate on spaces, cast each to integer, and put in tuple.
lst = [(int(s.split(" ")[0]), int(s.split(" ")[1])) for s in xy]
print("Unsorted:", lst)

# Sort the list of tuples, using the first element then the second.
# Taken from: https://stackoverflow.com/questions/9376384/sort-a-list-of-tuples-depending-on-two-elements
lst = sorted(lst, key=lambda element: (element[0], element[1]))

print("Sorted:", lst)
