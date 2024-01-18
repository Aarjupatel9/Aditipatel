def knapsack(weights, values, weight_limit):
    # Number of items
    n = len(weights)

    # Initiialize a 2 dimensional list to store the max
    #  value achievable for each weight limit
    l = [[0] * (weight_limit + 1) for _ in range(n + 1)]

    # creating the table
    for i in range(1, n + 1):
        for w in range(weight_limit + 1):
            # If current item weight is less than or equal to
            #  the current weight limit
            if weights[i - 1] <= w:
                # it check for , include the current item or not
                l[i][w] = max(values[i - 1] + [i - 1][w - weights[i - 1]], l[i - 1][w])
            else:
                # If the current item's weight
                #  exceeds the current weight limit, skip it
                l[i][w] = l[i - 1][w]

    # The final cell of the table contains the 
    # maximum value achievable with the given weight limit
    max_value = l[n][weight_limit]
    return max_value

# Example usage
weights = [3, 1, 4]
values = [4, 5, 7]
weight_limit = 5

result = knapsack(weights, values, weight_limit)
print("The maximum value achievable:", result) 
