# Node.py
# Author: Bevan Jones

import numpy as np

class NodeTable:
    def __init__(self, numberofNodesX, numberofNodesY, dimension):
        """
        Initialises a node with various nodal properties.
        :param numberofNodes: Number of nodes
        :param dimension: dimension of simulation
        """

        # General attributes of node
        self.isBoundary = np.zeros(dtype=bool, shape=(numberofNodesX, 1))
        self.Coordinate = np.zeros(dtype=float, shape=(numberofNodesX, dimension))
        self.Volume = np.zeros(dtype=float, shape=(numberofNodesX, 1))

        # Flow Variables
        self.VelocityN = np.zeros(dtype=float, shape=(numberofNodesX, dimension))
        self.PressureN = np.zeros(dtype=float, shape=(numberofNodesX, 1))
        self.TemperatureN = np.zeros(dtype=float, shape=(numberofNodesX, 1))

        # Flow at n+1 hand side
        self.VelocityNP1 = np.zeros(dtype=float, shape=(numberofNodesX, dimension))
        self.PressureNP1 = np.zeros(dtype=float, shape=(numberofNodesX, 1))
        self.TemperatureNP1 = np.zeros(dtype=float, shape=(numberofNodesX, 1))

        # Variable gradients
        self.VelocityGradient = np.zeros(dtype=float, shape=(numberofNodesX, dimension*dimension))
        self.PressureGradient = np.zeros(dtype=float, shape=(numberofNodesX, dimension))
        self.TemperatureGradient = np.zeros(dtype=float, shape=(numberofNodesX, dimension))

