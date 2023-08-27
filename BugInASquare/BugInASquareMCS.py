import random
import numpy as np
import matplotlib.pyplot as plt

# Bug is at one corner of a square.
# What is the expected number of steps it would take for it to get to the opposite corner?
# Each step takes it to an adjacent corner, with each corner equally likely.

def move_bug(bug_position):
    if (bug_position == '[0,0]'):
        return random.choice(['[0,1]','[1,0]'])
    if (bug_position == '[1,0]'):
        return random.choice(['[0,0]','[1,1]'])
    if (bug_position == '[0,1]'):
        return random.choice(['[0,0]','[1,1]'])
    else: return 'error'


#Monte Carlo Simulation:

#Empty list to store the probability values
list1 = []

def monte_carlo(n):
    results = 0
    for i in range(n):
        bug_position = '[0,0]'
        numMoves = 0
        while bug_position != '[1,1]':
            bug_position = move_bug(bug_position)
            numMoves += 1
        
        results = results + numMoves
        #Calculating probability value:
        prob_value = results/(i+1)

        #Append the probability values to the list :
        list1.append(prob_value)

        #Plot the results:
        plt.xlabel("Iterations")
        plt.ylabel("Steps")
        plt.plot(list1)

    return results/n

#Call the function
answer = monte_carlo(5000)
print("Final value: ", answer)
