class Directions:
    def __init__(self):
        self.m_directions = {}

    def get_locations(self):
        return list(self.m_directions.keys())

    def add_direction(self, source, destination, direction):
        if None == self.m_directions.get(source):
            self.m_directions[source] = {}
        self.m_directions[source][destination] = direction;
        
        if None == self.m_directions.get(destination):
            self.m_directions[destination] = {}
        if None == self.m_directions[destination].get(source):
            self.m_directions[destination][source] = "No route"
    
    def get_direction(self, source, destination):
        if None== self.m_directions.get(source):
            return None
        else :
            return self.m_directions[source].get(destination);
