def bi_search(l, r, arr, x):
    # Code Here
    m = int((l + r)/2)
    if l <= r and m < len(arr):
        if x == arr[m] :
            return True
        if x < arr[m] :
            r = m - 1
            return bi_search(l,r,arr,x)
        if x > arr[m] :
            l = m + 1
            return bi_search(l,r,arr,x)
        else :
            l = r + 1
            return bi_search(l,r,arr,x)
    else :
        return False 

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))