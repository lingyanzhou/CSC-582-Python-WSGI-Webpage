class Ranch:
    def __init__(self):
        self.m_name = None
        self.m_location = None
        self.m_description = None

    def set_name(self, name):
        self.m_name = name
    
    def set_location(self, location):
        self.m_location = location
    
    def set_description(self, description):
        self.m_description = description

    def get_name(self):
        return self.m_name
    
    def get_location(self):
        return self.m_location

    def get_description(self):
        return self.m_description

    def is_complete(self):
        return ( self.m_name!=None and
                self.m_location!=None and
                self.m_description!=None)
