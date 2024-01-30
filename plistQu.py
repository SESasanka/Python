# Get the arrival and departure times of Anna and Bob from the user
anna_arrival = int(input("Enter the time (in minutes after midnight) when Anna arrived at the restaurant: "))
anna_departure = int(input("Enter the time (in minutes after midnight) when Anna left the restaurant: "))
bob_arrival = int(input("Enter the time (in minutes after midnight) when Bob arrived at the restaurant: "))
bob_departure = int(input("Enter the time (in minutes after midnight) when Bob left the restaurant: "))

# Determine if the time ranges of Anna and Bob's presence at the restaurant overlap
if anna_arrival <= bob_departure and bob_arrival <= anna_departure:
    print("Anna and Bob were at the restaurant at the same time.")
    
    # If there is an overlap, calculate the duration of the overlap
    overlap_start = max(anna_arrival, bob_arrival)
    overlap_end = min(anna_departure, bob_departure)
    overlap_duration = overlap_end - overlap_start
    
    print(f"They overlapped for {overlap_duration} minutes.")
else:
    print("Anna and Bob were not at the restaurant at the same time.")
