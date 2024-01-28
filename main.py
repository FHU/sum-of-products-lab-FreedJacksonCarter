#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    #jackson is testing to make sure they're the same length (As instructed)
    if len(list1) != len(list2):
        return "Jackson, are these the same length?"
    listSum = 0
    #looping to go through the indices
    for i in range(len(list1)):
        listSum += list1[i] * list2[i]
    return listSum
        


if __name__ == '__main__':
    #splitting the lists into strings
    list1 = input().split()
    list2 = input().split()
    #makin 'em integers
    list1 = [int(num) for num in list1]
    list2 = [int(num) for num in list2]
    #finishing n putting out my product :D
    SumOfLists = sum_of_products(list1, list2)
    print(SumOfLists)
