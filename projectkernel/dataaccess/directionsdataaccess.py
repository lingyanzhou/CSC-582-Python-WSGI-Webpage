"""
 @author Lingyan Zhou
"""
from ..datastructure import Directions

from .basedataaccess import BaseDataAccess

import configparser

class DirectionsDataAccess(BaseDataAccess):
    def __init__(self, filename):
        BaseDataAccess.__init__(self)
        self.m_config_parser = configparser.ConfigParser()
        self.m_config_file_name = filename;
        self.m_directions = None;

    def load(self):
        self.m_config_parser.read(self.m_config_file_name)
        areaList = self.m_config_parser.sections();
        self.m_directions = Directions()
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
        with open(self.m_config_file_name, 'wt') as f:
            self.m_config_parser.write(f);

    def get(self):
        return self.m_directions

    def update(self, directions):
        self.m_config_parser = configparser.ConfigParser()
        self.m_directions = Directions()
        for loc in directions.get_locations():
            self.m_config_parser[loc] = {}
            for loc2 in directions.get_locations():
                self.m_config_parser[loc][loc2] = directions.get_direction(loc, loc2)
                self.m_directions.add_directions(loc, loc2, directions.get_direction(loc, loc2))
