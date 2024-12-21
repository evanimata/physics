import numpy as np

def atmospheric_pressure(P0, m, T, z, z0):
    '''
    m: molecular mass of the gas
    '''
    g = 9.81 # gravitational acceleration
    kb = 1.3806452e-23 # stefan-boltzmann constant
    P = P0 * np.exp(-(((m*g)/(kb*T))*(z-z0)))
    return P
















