import heapq

def fmr(sequences):

	sequences = [[(item, n) for item in seq] for n, seq in enumerate(sequences)]
	
	heap = heapq.merge(*sequences)
	
	found_range = None
	last_range = None
	current_items = [None] * len(sequences)
	for item, n in heap:
		current_items[n] = item
		if not all(current_items): 
			continue
		
		minimum = min(current_items)
		maximum = max(current_items)
		current_range = abs(maximum-minimum)
		
		if not last_range or current_range < last_range:
			found_range = [minimum, maximum]
			last_range = current_range
	
	return found_range
l1=[4,7,9,12,15]
l2=[0,8,10,14,20]
l3=[6,12,16,30,50]
l=[]
l.append(l1)
l.append(l2)
l.append(l3)
print(fmr(l))
