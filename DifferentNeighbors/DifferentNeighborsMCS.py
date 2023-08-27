import random
import numpy as np
import matplotlib.pyplot as plt

# 10 blue balls 8 red balls lined up in a queue.
# What is the expected # of balls that have a neighbor of a different color?
#Monte Carlo Simulation:

#Empty list to store the probability values
list1 = []

def monte_carlo(n):
    results = 0
    for i in range(n):
        ball_list = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
        random.shuffle(ball_list)
        balls_with_different_neighbor = 0
        for ball in range(len(ball_list)):
            if ball == 0:
                if ball_list[1] != ball_list[0]:
                    balls_with_different_neighbor += 1
            elif ball == 17:
                if ball_list[ball - 1] != ball_list[ball]:
                    balls_with_different_neighbor += 1
            elif ball_list[ball - 1] != ball_list[ball] or ball_list[ball + 1] != ball_list[ball]:
                    balls_with_different_neighbor += 1
        
        results = results + balls_with_different_neighbor
        #Calculating probability value:
        prob_value = results/(i+1)

        #Append the probability values to the list :
        list1.append(prob_value)

        #Plot the results:
        plt.xlabel("Iterations")
        plt.ylabel("Neighbors")
        plt.plot(list1)

    return results/n

#Call the function
answer = monte_carlo(50000)
print("Final value: ", answer)
