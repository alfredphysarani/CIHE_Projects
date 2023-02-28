import numpy as np
signal = np.array([1, 2, 2, 1, 2, 5, 5, 3])
order = 4
coeArray = np.zeros(order)



def multiLinearEq(signal, order):
    eqDict = {}
    for i in range(0, order):
        eqDict['eq'+str(i+1)] = signal[i:order+i+1]
        
    # Handling Layers
    for i in range (1, order):
        for j in range (i, order):
            eqDict['eq'+str(j+1)] = eqDict['eq'+str(j+1)] - eqDict['eq'+str(j+1)][i-1]/eqDict['eq'+str(i)][i-1]*eqDict['eq'+str(i)]
    
    return eqDict

arrangedEq = multiLinearEq(signal, order)