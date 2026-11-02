def multi_from_list(num):
    
    result = 1
    print("Multiplication result from list is: ", result)
    for i in num:
        print()
        result  = result * i 
    return result    

multi_from_list([2 , 4 , 6, 8])    