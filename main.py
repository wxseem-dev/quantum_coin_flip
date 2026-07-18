import numpy as np
# Normal computing, a bit is represented as a hard 0 (OFF) and 1 (ON)
# In quantum computing, a qubit is in a mixed state between the two as a blend, mixture of 0 and 1
# it could be pure 0 state so [1, 0] meaning 100% towards 0 or it could be pure 1 [0, 1] meaning 100% towards 1

# we can use a state vector which is a list of numbers like above to represent how much 0 and how much 1 our qubit has
qubit_state = np.array([1, 0]) # this represents our qubit as a pure 0 using numpy

print("qubit_state:", qubit_state)

# this state of blend between the two is called a superposition
# we can change the state of qubit using a quantum gate, in numpy this is a 2x2 matrix

# to create the 50/50 we need, we need to use the hadamard gate which is 1/sqrt(2) [1, 1, 1, -1]

# in quantum mechanics the probability of measuring a state is the square of its value. and as 1/sqrt2 squared is 50% thats how we get our exact chance for both 0 and 1

hadamard_gate  = ((1/np.sqrt(2)) * np.array([[1, 1], [1, -1]]))
print("hadamard gate:", hadamard_gate)


altered_gate = qubit_state * hadamard_gate

print("superposition:", altered_gate)