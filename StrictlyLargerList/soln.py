##### YOUR SOLUTION

X = #list
count = 0
j = 1
for i in range(len(X)-1):

    # This if condition evaluates to true if you are observing the last digit.
    # "Is the last digit greater than all digits to the right?"
    # This is trivial.
    if j == len(X):
        break

    # Is a number greater than the number immediately to the right?
    # (This does not consider all the numbers to the right, only the one directly next to it.)
    if (X[i]>X[j]) == True:
        count+=1

    # j will be each index [0, len(X) - 1] EXACTLY ONCE, not the correct behavior.
    j += 1

print(count)


##### MY SOLUTION

count = 0
j = 1
for i in range(len(X)-1):

    # Set j to be the index one greater than i
    j = i + 1

    # While, for an integer i, there exists more digits to the right.
    while j < len(X):

        # If any integer after i greater than or equal to i ...
        if X[i] <= X[j]:
            break

        # increment j
        j += 1

    # If we got to the last integer without finding an integer greater than i
    # then j now points to one index greater than those in list and increment count
    if j == len(X):
        count += 1

print(count)
