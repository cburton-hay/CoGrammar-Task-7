from statistics import mean
number_list = [] #creating an empty list so the input can be added into it.
counter = 0 # counter used to check the number of items in the list and could be used in mean calculation.
while True: 
    number = input("Enter a whole number. ")
    number = int(number) # making sure the numbers have numerical value.
    if number != -1:
        number_list.append(number)
        counter = counter + 1
    else:
       # print(counter) - can use to check the number of items in the list
       # print(number_list) - can use to see the list in full
       # print(sum(number_list)) - see the total of the list to check calculations
        print(mean(number_list))
        break
    
