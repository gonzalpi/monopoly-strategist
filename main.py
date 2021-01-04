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
    if k <= 3:                          # when no split is needed to store throw3 in P
        P[k,(1 + k):(37 + k)]   = throw3
    else:                               # when throw3 must be split to be stored in P
        P[k,0:(k - 3)]          = throw3[(39 - k):36]
        P[k,(1 + k):40]         = throw3[0:(39 - k)]

# P redistribution from triple doubles
P[:,10]     = P[:,10] + doubles

# P redistribution from "chance" cards
P_temp      = (1/16)*(P[:,7] + P[:,22] + P[:,36])
P[:,0]      = P[:,0]  + P_temp          # go
P[:,5]      = P[:,5]  + P_temp          # reading railroad
P[:,10]     = P[:,10] + P_temp          # jail
P[:,11]     = P[:,11] + P_temp          # st. charles place
P[:,24]     = P[:,24] + P_temp          # illinois avenue
P[:,39]     = P[:,39] + P_temp          # boardwalk

P[:,4]      = P[:,4]   + (1/16)*P[:,7]  # 3 tiles backwards
P[:,19]     = P[:,19]  + (1/16)*P[:,22]
P[:,33]     = P[:,33]  + (1/16)*P[:,36]

P[:,12]     = P[:,12]  + (1/16)*P[:,7]  # nearest utility
P[:,28]     = P[:,28]  + (1/16)*P[:,22]
P[:,12]     = P[:,12]  + (1/16)*P[:,36]

P[:,15]     = P[:,15]  + (1/16)*P[:,7]  # nearest railroad
P[:,25]     = P[:,25]  + (1/16)*P[:,22]
P[:,5]      = P[:,5]   + (1/16)*P[:,36]

P[:,7]      = (7/16)*P[:,7]             # compensate P
P[:,22]     = (7/16)*P[:,22]
P[:,36]     = (7/16)*P[:,36]

# P redistribution from "community chest" cards
P_temp = (1/17)*(P[:,2] + P[:,17] +  P[:,33])
P[:,0]      = P[:,0]  + P_temp  # go

P[:,2]      = (16/17)*P[:,2]    # compensate P
P[:,17]     = (16/17)*P[:,17]
P[:,33]     = (16/17)*P[:,33]

# P redistribution from landing in "go to jail" tile
P[:,10]     = P[:,10] + P[:,30]
P[:,30]     = 0

# matrix power and identity
probM = np.linalg.matrix_power(P,100)
probI = np.dot(np.identity(40) , probM)

# 1-d array
probV = np.zeros(40)
for m in range(40):
    probV[m] = probI[m,m]

# display
np.set_printoptions(threshold=np.inf, precision=2, suppress=True, linewidth=np.inf) # prints whole array, 2 decimal places, no scientific notation, no line wrapping
print("Probability percentage of landing on any given Monopoly tile.\nBegins with \"Go\" tile.")
print("\nTiles 1:20")
print(100*probV[0:20])
print("\nTiles 21:40")
print(100*probV[20:40])

# note: could be made more efficient by using eigvec*eigval^100*eigvec^-1
# further work: analyze profitability taking into account price and rent too