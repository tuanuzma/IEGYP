import heapq

def connect_ropes(N, k, ropes):
    # Convert the list of ropes into a min-heap (priority queue)
    heapq.heapify(ropes)
    
    # To store the total cost of connecting ropes
    total_cost = 0
    
    # Connect ropes until only one rope remains
    while len(ropes) > 1:
        # Pop the two smallest ropes
        first = heapq.heappop(ropes)
        second = heapq.heappop(ropes)
        
        # Calculate the new rope length after connection
        new_rope = first + second - 2 * k
        total_cost += new_rope
        
        # Push the new rope back into the heap
        heapq.heappush(ropes, new_rope)
    
    # The length of the final remaining rope is the only element left in the heap
    return ropes[0]

# Reading input
N, k = map(int, input().split())  # number of ropes and k value
ropes = list(map(int, input().split()))  # lengths of the ropes

# Get the final length of the connected rope
final_length = connect_ropes(N, k, ropes)

# Output the result
print(final_length)