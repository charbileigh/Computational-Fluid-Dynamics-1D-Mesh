import MeshGenerator as mg
import Plotter as pl
import Discretisation as dc
import copy

# Simulation Parameters
NumberofNodes = 11
positveStretchFactor = 1.0
viscocity = 0.2
density = 1.0
CFL = 0.95
convergenceTolerance = 1.0e-4

# Set up plotter (customise plotter here)
plotter = pl.Plotter("Assignment 1", 1, 1, 1)
plotter.Add1DPlot(1, "Temperature distrabution", "Co-ordiante", "Temperature", "", "-o", False)

# Create new node table and set initial conditions
nodeTable = mg.GenerateMesh1DMesh(NumberofNodes, positveStretchFactor)

# Set initial conditions
# code here...

# Set up some convergence variables
itimeStep = 1
isconverged = False

# Continue solving while not converged.
while not isconverged:

    # Compute a stable time step size
    deltaTime = dc.Stability(nodeTable.Coordinate, nodeTable.VelocityN, viscocity, CFL)

    # Compute temperature and the next time step.
    for inodeX in range(NumberofNodes):
        nodeTable.TemperatureNP1[inodeX] = nodeTable.TemperatureN[inodeX]
        nodeTable.TemperatureNP1[inodeX] += dc.Diffusion1D(nodeTable.TemperatureN, nodeTable.Coordinate, nodeTable.Volume, viscocity, deltaTime, inodeX) \
                                            - dc.Advection1D(nodeTable.TemperatureN, nodeTable.VelocityN, nodeTable.Volume, density, deltaTime, inodeX)

    # Apply boundary conditions
# code here...

    # Check convergence
    isconverged, residual = dc.isConverged(nodeTable.TemperatureN, nodeTable.TemperatureNP1, convergenceTolerance)

    # Report results (comment out plotter calls to significantly decrease run time)
    print("Time step: " + '{:5}'.format(itimeStep) + "\tdt: " + '{:<.2e}'.format(deltaTime) + "\t Residual: " + '{:<.2e}'.format(residual))
    plotter.Update1DPlotData(1, nodeTable.Coordinate, nodeTable.TemperatureNP1, "")
    plotter.Plot(False)

    # Finalise the time step
    itimeStep = itimeStep + 1
    nodeTable.TemperatureN = copy.copy(nodeTable.TemperatureNP1)

# Report final resutls
print("\nSimulation completed")
# code here...
plotter.Update1DPlotData(1, nodeTable.Coordinate, nodeTable.TemperatureNP1, "")
plotter.Plot(True)
