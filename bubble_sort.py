list1=[5,6,4,2,3,1]
list2=[5,6,4,2,3,1]
def bubble_sort(obj):
    for i in range(0,len(obj)-1):
        for j in range(len(obj)-1):
            if(obj[j]>obj[j+1]):
                temp=obj[j]
                obj[j]=obj[j+1]
                obj[j+1]=temp
    return list1

def partition(arr,low,high):
    i=(low-1)
    pivot= arr[high]
    for j in range(low,high):
        if arr[j] <= pivot:
            i+=1
            (arr[i],arr[j])=(arr[j],arr[i])
    (arr[i+1],arr[high])=(arr[high],arr[i+1])
    return (i+1)
def quicksort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quicksort(arr, low, pi-1) 
        quicksort(arr, pi+1, high)


n=len(list1)

quicksort(list2,0,n-1)
print(f"bubble sort : {bubble_sort(list1)}")
print(f"quick sort : {list2}")