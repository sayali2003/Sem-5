# Python3 implementation of FIFO page replacement in Operating Systems.
from queue import Queue 

# Function to find page faults using FIFO 
def pageFaults(pages, n, capacity): 
	
	# To represent set of current pages. we use an unordered_set so that we quickly check if a page is present in set or not 
	s = set() 

	# To store the pages in FIFO manner 
	indexes = Queue() 

	# Start from initial page 
	page_faults = 0
	for i in range(n): 

		if (len(s) < capacity): 

			if (pages[i] not in s): 
				s.add(pages[i]) 

				page_faults += 1
 
				indexes.put(pages[i]) 

		else: 

			if (pages[i] not in s): 
				
				val = indexes.queue[0] 

				indexes.get() 

				s.remove(val) 

				s.add(pages[i]) 

				indexes.put(pages[i]) 

				page_faults += 1

		print(pages[i], end="\t\t")
		for q_item in indexes.queue:
			print(q_item, end="\t")

		print()
	return page_faults


# Driver code
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1]
n = len(pages)
capacity = 3
page_faults = pageFaults(pages, n, capacity)
hits = n - page_faults

print("\nPage Faults: " + str(page_faults))
print("Hit: " + str(hits))

