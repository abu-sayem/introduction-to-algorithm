#Heapsort and priority queue
def parent(i):
	return (i-1)>>1

def left(i):
	return (i<<1)+1

def right(i):
	return (i<<1)+2
#================max_heap===============
def max_heapify(list, i, size):
	L = left(i)
	R = right(i)
	largest = i
	if(L<=size and list[L]>list[i]):
		largest = L
	if(R<=size and list[R]>list[largest]):
		largest =R
	if largest != i:
		list[i], list[largest] = list[largest], list[i]
		max_heapify(list,largest,size)

def build_max_heap(list,size):
	for i in range(size//2,-1,-1):
		max_heapify(list,i,size)

def max_heapsort(list,size):
	build_max_heap(list, size)
	for i in range(size,0,-1):
		list[0], list[size] = list[size], list[0]
		size = size - 1
		max_heapify(list,0, size-1)

#=================min_heap===================
def min_heapify(list, i, size):
	L = left(i)
	R = right(i)
	largest = i
	if(L<=size and list[L]<list[i]):
		largest = L
	if(R<=size and list[R]<list[largest]):
		largest =R
	if largest != i:
		list[i], list[largest] = list[largest], list[i]
		min_heapify(list,largest,size)

def build_min_heap(list,size):
	for i in range(size//2,-1,-1):
		min_heapify(list,i,size)

def min_heapsort(list,size):
	build_min_heap(list, size)
	for i in range(size,0,-1):
		list[0], list[size] = list[size], list[0]
		size = size - 1
		min_heapify(list,0, size)

#============heap_extract_max=================== =
def heap_extract_max(list,size):
	max = list[0]
	list[0] = list[size]
	del(list[-1])
	max_heapify(list,0,size)

#=============heap_increase_key==================
def heap_increase_key(list,key,i,size):
	if(key<list[i]):
		assert "New key is smaller than current key"
	list[i] =key
	while i>0 and list[parent(i)<a[i]]:
		list[i], list[parent(i)]=list[parent(i)],list[i]
		i=parent(i)

#=============max_heap_increase=============
def max_heap_insert(list,size,key):
	size = size+1
	list[size] = float('-inf')
	heap_increase_key(list,key,size,size)
#===============main_function===============
if __name__ == '__main__':
	list = [1,2,3,4,7,8,9,10,14,16]
	size = len(list)-1
	min_heapsort(list,size)
	print(list)
	heap_extract_max(list,size)
	print(list)
