import numpy as np

# probability (P) array for a single two-dice throw (landing on 1:12) excluding doubles
throw1          = (1/36)*np.array([0, 0, 2, 2, 4, 4, 6, 4, 4, 2, 2, 0])

# P array for up to 2 throws (landing on 1:24) excluding doubles
throw2          = np.zeros(24)
throw2[0:12]    = throw1
for i in range(6):
    throw2[(2 + 2*i):(14 + 2*i)] = throw2[(2 + 2*i):(14 + 2*i)] + (1/36)*throw1

# P array for up to 3 throws and P of throwing doubles 3 times in a row (landing on 1:36)
throw3          = np.zeros(36)
throw3[0:12]    = throw1
for j in range(6):
    throw3[(2 + 2*i):(26 + 2*i)] = throw3[(2 + 2*i):(26 + 2*i)] + (1/36)*throw2
doubles         = (1/6)**3

# P matrix
P               = np.zeros((40,40))
for k in range (40):
    if k <= 3:  # when no split is needed to store throw3 in P
        P[k,(1 + k):(37 + k)]   = throw3
    else:       # when throw3 must be split to be stored in P
        P[k,0:(k - 3)]          = throw3[(39 - k):36]
        P[k,(1 + k):40]         = throw3[0:(39 - k)]
    P[k,10]     = P[k,10] + doubles # probability of going to jail after triple doubles
    
# redistribution of P from "chance", "community chest" and "go to jail" tiles

# diagonalization of P matrix
# self-multiplying until change is minimal (must define a threshold)
# de-diagonalization

# extra: analyze profitability taking into account cost, rent and probability
