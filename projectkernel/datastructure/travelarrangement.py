class TravelArrangement:
    def __init__(self):
        self.m_id = None
        self.m_name = None
        self.m_description = None

    def set_id(self, id):
        self.m_id = id

    def set_name(self, name):
        self.m_name = name
    
    def set_description(self, description):
        self.m_description = description

    def get_id(self):
        return self.m_id

    def get_name(self):
        return self.m_name
    
    def get_description(self):
        return self.m_description

    def is_complete(self):
        return ( self.m_name!=None and
                self.m_id!=None and
                self.m_description!=None)
