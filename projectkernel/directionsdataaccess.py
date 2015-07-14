"""
 @author Lingyan Zhou
"""
from . import directions

import configparser

class DirectionsDataAccess:
    def __init__(self, filename):
        self.m_config_parser = configparser.ConfigParser()
        self.m_config_file_name = filename;
        self.m_directions = None;

    def load(self):
        self.m_config_parser.read(self.m_config_file_name)
        areaList = self.m_config_parser.sections();
        self.m_directions = directions.Directions()
        for a1 in areaList:
            for a2 in areaList:
                if a1==a2:
                    self.m_directions.add_direction(a1, a2, "You are already here")
                else :
                    self.m_directions.add_direction(a1, a2, "No route")
        
        for a1 in areaList:
            for a2 in areaList:
                if self.m_config_parser.has_option(a1, a2):
                     self.m_directions.add_direction(a1, a2, self.m_config_parser[a1][a2])

    def save(self):
        pass

    def get(self):
        return self.m_directions

