#From codereview.stackexchange.com                    
def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b

# This is a helper function that will fetch all of the available 
# partitions for you to use for your brute force algorithm.
def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]
        
        
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    dict_copy = dict(cows)
    # Initialize a list containing the maximum number of trips possible
    max_trips = []
    # Each cow gets its own trip.
    for cow in dict_copy:
        trip = []
        trip.append(cow)
        max_trips.append(trip)
    # Initialize the current best known solution as the maximum number of 
    #  trips possible.
    solution = max_trips
    
    # Loop through each set of trips as created by the partition helper func.
    for set_of_trips in (get_partitions(dict_copy)):
        # Initialize a trip counter, in order to find out when you have 
        #  exhausted all the trips of a particular set of trips.
        trip_counter = 0
        # Loop through each trip in a set of trips.
        for trip in set_of_trips:
            trip_counter += 1
            # Initialize a weight for the trip.
            weight_of_trip = 0
            # Loop through each cow in the trip and add its weight to the sum.
            for cow in range(len(trip)):
                weight_of_trip += dict_copy[trip[cow]]
            # Break out of the current set of trips if the current trip 
            #  exceeds the weight limit.
            if weight_of_trip > limit:
                break
            # If you are on the last trip of a set of trips, compare the 
            #  number of trips in the set to the current best known solution.
            elif trip_counter == len(set_of_trips):
                # If the number of trips in the current set is less than the
                #  number of trips in the current best known solution,
                #  set the new solution to the current set of trips.
                if len(set_of_trips) < len(solution):
                    solution = set_of_trips
            # If the current trip does not exceed the weight limit, and you are
            #  looking at the last trip in the set, check the next trip in the set.
            else:
                continue

    return solution
