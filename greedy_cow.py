def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

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
    solution = []
    
    def findmaxval(dictionary):
        """
        Takes as input a dictionary with names as keys and weights as values.
        
        Returns the value of the heaviest cow in the dictionary.
        """
        value_list = list(dictionary.values())
        value_list.sort(reverse = True)
        return value_list[0]
        
    def findmaxkey(dictionary, max_val):
        """
        Takes as input a dictionary with names as keys and weights as values,
        and a max weight to find.
        
        Returns the name of the heaviest cow in the dictionary.
        """
        for name, weight in dictionary.items():
            if weight == max_val:
                return name
    
    def greedy_list_maker(dictionary):
        """
        Takes as input a dictionary with names as keys and weights as values.
        
        Returns a tuple of:
            A list of the heaviest cows you can take on one trip.
            A dictionary of cows that were not taken on the trip.
        """
        trip_list = []
        total = 0
        cows_considered = {}
        while total <= limit and len(dictionary) > 0:
            # Find the heaviest cow available
            max_val = findmaxval(dictionary)
            # Find the name of the heaviest cow available
            max_key = findmaxkey(dictionary, max_val)
            # Make sure the heaviest cow available can fit on this trip
            if total + dictionary[max_key] > limit:
                # If not, set aside to be considered next time
                cows_considered[max_key] = dictionary[max_key]
                #  and remove from the current possibilities
                del dictionary[max_key]
                continue
            # If yes, add the cow to this trip
            trip_list.append(max_key)
            #  and increase the trip's weight appropriately
            total += dictionary[max_key]
            # Remove the cow from the current possibilities
            del dictionary[max_key]
        return trip_list, cows_considered
        
    while len(dict_copy) > 0:
        # Story results of the trip maker
        my_tuple = greedy_list_maker(dict_copy)
        # Append the trip list to the solution
        solution.append(my_tuple[0])
        # Reset the trip maker to work on all cows remaining
        dict_copy = my_tuple[1]

    return solution
