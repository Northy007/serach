def GreterLess(arr,n,k,res) :
    if n >= 0:
        if res == 0 and arr[n] > k:
            return GreterLess(arr,n-1,k,arr[n])
        if arr[n] > k and arr[n] < res :
            return GreterLess(arr,n-1,k,arr[n])
        else :
            return GreterLess(arr,n-1,k,res)
    else :
        if res == 0:
            return "No First Greater Value"
        return res

inp = input('Enter Input : ').split('/')
arr1 = list(map(int, inp[0].split()))
arr2 = list(map(int, inp[1].split()))

for i in arr2 :
    print(GreterLess(arr1,len(arr1)-1,i,0))