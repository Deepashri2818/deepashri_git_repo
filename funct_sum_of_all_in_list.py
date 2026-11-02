def sum_in_list(a):
    #my_list = [ 5 ,8, 10, 15]
    
    sum_is = sum(a)
    print("Sum of all the numbers in a list is", sum_is)

sum_in_list([ 5 ,8, 10, 15])

def prod_in_list(a):
    
    prod_is = 1   
   
    for i in a:
        prod_is = prod_is * i
    print("Product in list is", prod_is)
    
prod_in_list([ 5, 10, 10])