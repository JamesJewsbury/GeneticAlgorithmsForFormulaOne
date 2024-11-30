class calendar:

    def __init__(self):
        """
        Initialise the calendar (possible solution) to store the agenda and fitness of the solution.
        """
        self._agenda=[]
        self._fitness=0

    def GetAgenda(self)->list:
        """
        Get the list of nodes which make up this calendar.

        :return: A list of nodes.
        """
        return self._agenda
    
    def GetFitness(self)->float:
        """
        Get the fitness of this calendar.

        :return: returns a float of the distance.
        """