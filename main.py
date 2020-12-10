import numpy as np

# probability (P) array for a single two-dice throw
throw1          = (1/36)*np.array([0, 0, 2, 2, 4, 4, 6, 4, 4, 2, 2, 0])

# P array for up to 2 throws
throw2          = np.zeros(24)
throw2[0:12]    = throw1
for i in range(6):
    throw2[(2 + 2*i):(14 + 2*i)] = throw2[(2 + 2*i):(14 + 2*i)] + (1/36)*throw1

# P array for up to 3 throws and P of throwing doubles 3 times in a row
throw3          = np.zeros(36)
throw3[0:12]    = throw1
for j in range(6):
    throw3[(2 + 2*i):(26 + 2*i)] = throw3[(2 + 2*i):(26 + 2*i)] + (1/36)*throw2
doubles        = (1/6**3)

# P matrix
# redistribution of P from "chance", "community chest" and "go to jail" tiles

# diagonalization of P matrix
# self-multiplying until change is minimal (must define a threshold)
# de-diagonalization

# extra: analyze profitability taking into account cost, rent and probability
