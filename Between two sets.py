arr=[2,4]
brr=[16,32,96]
arr.sort()
brr.sort()

x=max(arr)
y=min(brr)
new_list=[i for i in range(x,y+1)]
ort=[]
def twosets(arr,brr):
    for i in new_list:
        for j in range(len(arr)):
            if i % arr[j] != 0:
                break
            elif i % arr[j] == 0:
                if j == (len(arr) - 1):
                    ort.append(i)
                    break
    yeni=0
    for i in ort:
        for j in range(0,len(brr)):
            if brr[j]%i==0:
                continue

            elif brr[j]%i!=0:
                yeni+=1
                break
    return(len(ort)-yeni)
twosets(arr,brr)