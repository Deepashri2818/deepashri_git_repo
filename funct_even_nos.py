def even_nos_from_range(num):
    
    print("Even nos from given range are:")
    
    for i  in range(0, num):
        if i  % 2 == 0:
             print(i, end=" ")
    print()         
    print()         

       
even_nos_from_range(31)

def even_nos_from_list(num):
    
    print("Even nos from list are:")
    
    for i  in num:
        if i  % 2 == 0:
             print(i, end=" ")
       
even_nos_from_list([ 5, 10, 2 ,6, 8])