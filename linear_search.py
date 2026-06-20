arr = [30, 40,50,60, 70, 80,90, 100, 150, 200, 300, 400, 500]
def linear_serach(arr, x_list):
    result= {}
    for x in x_list:
        found =-1
        for i in range(len(arr)):
            if (arr[i]== x):
                found = i
                break
        result[x]= found
    return result
            
    
x= [90, 200, 500]
result= linear_serach(arr, x)
print(result)

 