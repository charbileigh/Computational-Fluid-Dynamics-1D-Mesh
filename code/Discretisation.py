import numpy as np

def isConverged(nodeVariableN, nodeVariableNP1, convergenceTolerance):

    issimulationConverged = True # In real simulations this should start off as false.
    l2Norm = 0.0
# code here...
    return issimulationConverged, l2Norm

def Stability(nodeCoordinate, nodeVelocity, viscosity, CLF):

    stableTimeStepSize = 10.0
# code here...
    return stableTimeStepSize

def Diffusion1D(nodeVariable, nodeCoordinate, nodeVolume, viscocity, deltaTime, irow):

    diffusionContribution = 0.0
# code here...
    return diffusionContribution

def Advection1D(nodeVariable, nodeVelocity, nodeVolume, density, deltaTime, irow):

    advectionContribution = 0.0
# code here...
    return advectionContribution
