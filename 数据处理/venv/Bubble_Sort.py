def Bubble_Sort(arr):
    n=len(arr)

    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr=[1,6,7,9,0,10,20,13,4,32]
Bubble_Sort(arr)

for i in range(len(arr)):
    print('{}'.format(arr[i]))




