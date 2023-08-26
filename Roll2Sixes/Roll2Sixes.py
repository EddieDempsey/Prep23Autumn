import random
import numpy as np
import matplotlib.pyplot as plt


# What is the expected number of time you need to roll a fair die until you get 2 6's in a row?

def roll_die():
    return random.randint(0,5)

roll_die()

#Monte Carlo Simulation:

#Empty list to store the probability values
list1 = []

def monte_carlo(n):
    results = 0
    for i in range(n):
        RollResults = []
        numRolls = 0
        while numRolls < 2 or (RollResults[-1] != 5 or RollResults[-2] != 5):
            RollResults.append(roll_die())
            numRolls+=1
        
        results = results + numRolls

        #Calculating probability value:
        prob_value = results/(i+1)

        #Append the probability values to the list :
        list1.append(prob_value)

        #Plot the results:
        plt.xlabel("Iterations")
        plt.ylabel("Rolls")
        plt.plot(list1)

    return results/n

#Call the function
answer = monte_carlo(5000)
print("Final value: ", answer)
