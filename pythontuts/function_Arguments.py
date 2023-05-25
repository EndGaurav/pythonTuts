# types of arguments
# Default argument
# keyword argument
# Variable length argument
# Required argument
# return statement

# def average(a=4, b=4): #default example
#     print("The average is:", (a+b)/2)
#
# average()

# def average(a, b): #Keyword example
#     print("The average is:", (a+b)/2)
#
# average(b=2, a=2) #Order doesn't matter

def average(*nums): #Variable length arguments
    sum = 0
    for i in nums:
        sum = sum + i

    print("The average is: ", sum/len(nums))

average(2,4,5)