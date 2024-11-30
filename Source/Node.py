class node:

    def __init__(self, latitude:float, longitude:float, name:str):
        """
        Initialise a node object

        :param latitude: The latitude of the desired location
        :param longitude: The longitude of the desired location
        :param name: The name of the desired location
        """
        self.__latitude=latitude
        self.__longitude=longitude
        self.__name=name
    
    def GetLatitude(self)->float:
        """
        Get the latitude of the node.

        :return: returns the float of the latitude
        """
        return self.__latitude
    
    def GetLongitude(self)->float:
        """
        Get the longitude of the node.

        :return: returns the float of the longitude
        """
        return self.__longitude
    
    def GetName(self)->str:
        """
        Get the name of the node.

        :return: returns the string of the name
        """
        return self.__name
    
