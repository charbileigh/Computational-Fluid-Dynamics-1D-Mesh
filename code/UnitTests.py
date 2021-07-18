import random
import unittest
import numpy as np
import MeshGenerator as mg
import Discretisation as dc

class TestMeshGenerator(unittest.TestCase):

    def test_ComputeInitialNodeSpacing_1DEquiSpace(self):
        """
        Tests that the initial node spacing is correct when node spacing is equi-spaced.
        """
        numberofNodes = 11
        stretchFactor = 1.0
        self.assertEqual(mg.ComputeInitialNodeSpacing(numberofNodes, stretchFactor), 1.0/10.0)

        numberofNodes = 50
        stretchFactor = 1.0
        self.assertEqual(mg.ComputeInitialNodeSpacing(numberofNodes, stretchFactor), 1.0/49.0)

    def test_ComputeInitialNodeSpacing_1DStrechSpace(self):
        """
        Tests that the initial node spacing is correct when using a stretching factor.
        """
        numberofNodes = 3
        stretchFactor = 0.5
        self.assertEqual(mg.ComputeInitialNodeSpacing(numberofNodes, stretchFactor), 2.0/3.0)

        numberofNodes = 3
        stretchFactor = 1.5
        self.assertEqual(mg.ComputeInitialNodeSpacing(numberofNodes, stretchFactor), 0.4)

    def test_GenerateMesh1DMesh_1DBoundaryCompliance(self):
        """
        Tests that boundary nodes were correctly identified and have the correct co-ordinate.
        """

        numberofNodes = random.randint(3, 20)
        stretchFactor = 1.0
        nodeTable = mg.GenerateMesh1DMesh(numberofNodes, stretchFactor)

        for inode in range(numberofNodes):
            self.assertEqual(nodeTable.isBoundary[inode], True if inode == 0 or inode == numberofNodes - 1 else False)

    def test_GenerateMesh1DMesh_1DNodalVolumes(self):
        """
        Tests that nodal control volumes are have been correctly computed.
        """
        numberofNodes = 3
        stretchFactor = 1.0
        nodeTable = mg.GenerateMesh1DMesh(numberofNodes, stretchFactor)
        self.assertAlmostEquals(nodeTable.Volume[0], 0.25)
        self.assertAlmostEquals(nodeTable.Volume[1], 0.5)
        self.assertAlmostEquals(nodeTable.Volume[2], 0.25)

        numberofNodes = 3
        stretchFactor = 1.5
        nodeTable = mg.GenerateMesh1DMesh(numberofNodes, stretchFactor)
        self.assertAlmostEquals(nodeTable.Volume[0], 0.2)
        self.assertAlmostEquals(nodeTable.Volume[1], 0.5)
        self.assertAlmostEquals(nodeTable.Volume[2], 0.3)

        numberofNodes = 5
        stretchFactor = 1.0
        nodeTable = mg.GenerateMesh1DMesh(numberofNodes, stretchFactor)
        self.assertAlmostEquals(nodeTable.Volume[0], 0.125)
        self.assertAlmostEquals(nodeTable.Volume[1], 0.25)
        self.assertAlmostEquals(nodeTable.Volume[2], 0.25)
        self.assertAlmostEquals(nodeTable.Volume[3], 0.25)
        self.assertAlmostEquals(nodeTable.Volume[4], 0.125)

    def test_GenerateMesh1DMesh_1DCoordinates(self):
        """
        Tests that nodal control volumes are have been correctly computed.
        """
        numberofNodes = 3
        stretchFactor = 1.0
        nodeTable = mg.GenerateMesh1DMesh(numberofNodes, stretchFactor)
        self.assertAlmostEquals(nodeTable.Coordinate[0][0], 0.0)
        self.assertAlmostEquals(nodeTable.Coordinate[1][0], 0.5)
        self.assertAlmostEquals(nodeTable.Coordinate[2][0], 1.0)

        numberofNodes = 3
        stretchFactor = 1.5
        nodeTable = mg.GenerateMesh1DMesh(numberofNodes, stretchFactor)
        self.assertAlmostEquals(nodeTable.Coordinate[0][0], 0.0)
        self.assertAlmostEquals(nodeTable.Coordinate[1][0], 0.4)
        self.assertAlmostEquals(nodeTable.Coordinate[2][0], 1.0)

        numberofNodes = 5
        stretchFactor = 0.5
        nodeTable = mg.GenerateMesh1DMesh(numberofNodes, stretchFactor)
        self.assertAlmostEquals(nodeTable.Coordinate[0][0], 0.0)
        self.assertAlmostEquals(nodeTable.Coordinate[1][0], 0.53333333)
        self.assertAlmostEquals(nodeTable.Coordinate[2][0], 0.80000000)
        self.assertAlmostEquals(nodeTable.Coordinate[3][0], 0.93333333)
        self.assertAlmostEquals(nodeTable.Coordinate[4][0], 1.0)

        numberofNodes = 5
        stretchFactor = 1.0
        nodeTable = mg.GenerateMesh1DMesh(numberofNodes, stretchFactor)
        self.assertAlmostEquals(nodeTable.Coordinate[0][0], 0.0)
        self.assertAlmostEquals(nodeTable.Coordinate[1][0], 0.25)
        self.assertAlmostEquals(nodeTable.Coordinate[2][0], 0.5)
        self.assertAlmostEquals(nodeTable.Coordinate[3][0], 0.75)
        self.assertAlmostEquals(nodeTable.Coordinate[4][0], 1.0)

class TestDiscretisation(unittest.TestCase):

    def test_Stability_1D(self):
        """
        Tests that delta timec computation, first by comparing to a known value and then by checking that a smaller CFL value gives a smaller times step size.
        """
        CLF = 10.0
        viscosity = 0.25
        nodeCoordinate = np.zeros(dtype=float, shape=(3, 1))
        nodeCoordinate[0] = 0.0
        nodeCoordinate[1] = 0.5
        nodeCoordinate[2] = 1.0
        nodeVelocity = np.zeros(dtype=float, shape=(3, 1))
        nodeVelocity[:] = 0.5
        self.assertAlmostEquals(dc.Stability(nodeCoordinate, nodeVelocity, viscosity, CLF), 1.0)

        self.assertLess(dc.Stability(nodeCoordinate, nodeVelocity, viscosity, 0.2), dc.Stability(nodeCoordinate, nodeVelocity, viscosity, 0.25))

    # def test_Diffusion1D(self):

if __name__ == '__main__':
    unittest.main(verbosity=2)