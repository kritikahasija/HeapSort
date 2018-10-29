def heapify(arr,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if l<n and arr[l]>arr[i]:
        largest=l
    if arr[r]>arr[i] and r<n:
        largest=r
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)
def heapsort(arr):
    n=len(arr)
    for i in range(n,-1,-1):
        heapify(arr,n,i)  #maxheap
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i] #swap first & last
        heapify(arr,i,0)
arr=[4,10,3,5,1]
heapsort(arr)
for i in range(len(arr)):
    print("%d" %arr[i]),

