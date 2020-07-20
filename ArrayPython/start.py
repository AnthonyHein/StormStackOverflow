def input_array():                  #Take the list elements as input from user
    array = []
    row = input("Enter the num of rows: ")
    col = input("Enter the num of cols: ")
    for i in range(int(row)):
        arr = []
        for j in range(int(col)):
            a = eval(input("Enter an element: "))
            arr.append(a)
        array.append(arr)
    print(array)
    return array


def print_array(array):             #Print the list as a matrix
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j], end = " ")
        print()


def getRowSum(array):               #To get the sum of rows and print them beside respective rows
    for i in range(len(array)):
        summ = 0
        for j in array[i]:
            print(j, end=" ")
            summ += j
        print(summ)


array = input_array()
print_array(array)
getRowSum(array)
print(array)
