import random
import pylab
import numpy

# Global Variables
Max_rabbits = 1000.0
Current_rabbits = 500.0
Current_foxes = 30.0

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global Current_rabbits

    
    Current_rabbits += Current_rabbits * (1.0 - Current_rabbits / Max_rabbits)
    pass
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global Current_rabbits
    global Current_foxes

    Successful_Foxes = Current_foxes * Current_rabbits / Max_rabbits
    Dead_Foxes = (Current_foxes - Successful_Foxes) * 0.1
    Current_foxes =  Current_foxes + Successful_Foxes * 1.0/3.0 - Dead_Foxes
    Current_rabbits -= Current_rabbits / Max_rabbits * Current_foxes
    
    
            
def runSimulation(num_Steps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations = []
    fox_populations = []
    
    for i in range(num_Steps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(Current_rabbits)
        fox_populations.append(Current_foxes)
        
    return (rabbit_populations, fox_populations)

rabbit_populations,fox_populations = runSimulation(100)

rabbits_coeff = numpy.polyfit(range(len(rabbit_populations)),rabbit_populations,2)
pylab.plot(range(len(rabbit_populations)),rabbit_populations,'ro')
pylab.plot(numpy.polyval(rabbits_coeff,range(len(rabbit_populations))),'b')

fox_coeff = numpy.polyfit(range(len(fox_populations)),fox_populations,2)
pylab.plot(range(len(fox_populations)),fox_populations,'mo')
pylab.plot(numpy.polyval(fox_coeff,range(len(fox_populations))),'r')

pylab.show()
    
