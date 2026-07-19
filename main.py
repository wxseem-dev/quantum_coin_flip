import numpy as np
# Normal computing, a bit is represented as a hard 0 (OFF) and 1 (ON)
# In quantum computing, a qubit is in a mixed state between the two as a blend, mixture of 0 and 1
# it could be pure 0 state so [1, 0] meaning 100% towards 0 or it could be pure 1 [0, 1] meaning 100% towards 1

# we can use a state vector which is a list of numbers like above to represent how much 0 and how much 1 our qubit has
qubit_state = np.array([0, 1]) # this represents our qubit as a pure 0 using numpy

print("qubit_state:", qubit_state)

# this state of blend between the two is called a superposition
# we can change the state of qubit using a quantum gate, in numpy this is a 2x2 matrix

# to create the 50/50 we need, we need to use the hadamard gate which is 1/sqrt(2) [1, 1, 1, -1]

# in quantum mechanics the probability of measuring a state is the square of its value. and as 1/sqrt2 squared is 50% thats how we get our exact chance for both 0 and 1

# we use the hadamard gate to get our 50/50 superposition

hadamard_gate  = ((1/np.sqrt(2)) * np.array([[1, 1], [1, -1]]))
print("hadamard gate:", hadamard_gate)

# Hadamard gate ---- #

# A qubit is like a direction perfectly upwards towards 0 or perfectly downwards towards 1
# a hardamard gate is a geometric rotator which rotates the state vertically to 90 degrees so its in the middle and equidistant creating a 50/50 split
# there are many ways a quantum state can achieve 50/50, they have a phase which is an angle/direction
# ------------------ #

altered_gate = hadamard_gate @ qubit_state # true matrix calculation is done with @

print("superposition:", altered_gate)

zero_state_probability = altered_gate[0] ** 2
one_state_probability = altered_gate[1] ** 2

# The superposition is the product/result of the multiplication, the state after the matrix is applied
# a state vector after is just an index of options, so for a single qubit of [0,1] that has two slots
# each slot represents the amplitude of 0 state and 1 state, e.g. how much of each
# to find the probabilities, we square them individually
# say we have a state vector of [0.8, 0.6]
# the probabilities would be 0 = 0.8**2 = 0.64 (64% chance), 1 = 0.6**2 = 0.36 (36% chance)

# the rule of quantum computing is that a qubit must collapse into either 0 or 1 so the squared probabilities
# must add up to 1.0 or 100%

choice = np.random.choice(a=[0,1], size=1000, replace=True, p=[zero_state_probability, one_state_probability])
# choose out of 0 or 1, 1000 times each with its probability so its weighted


count_0 = np.count_nonzero(choice == 0)
count_1 = np.count_nonzero(choice == 1)

print(count_0, '0s')
print(count_1, '1s')

def quantum_coin_flip():
    qubit_state = np.array([0, 1])

    hadamard_gate  = ((1/np.sqrt(2)) * np.array([[1, 1], [1, -1]]))

    altered_gate = hadamard_gate @ qubit_state # true matrix calculation is done with @

    zero_state_probability = altered_gate[0] ** 2
    one_state_probability = altered_gate[1] ** 2

    return np.random.choice(a=[0,1], size=None, replace=True, p=[zero_state_probability, one_state_probability])

