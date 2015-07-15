"""
 @author Lingyan Zhou
"""
from ..datastructure import Ranch

from .basedataaccess import BaseDataAccess

import configparser

class RanchDataAccess(BaseDataAccess):
    def __init__(self, filename):
        BaseDataAccess.__init__(self)
        self.m_config_parser = configparser.ConfigParser()
        self.m_config_file_name = filename;
        self.m_ranch = None;

    def load(self):
        self.m_config_parser.read(self.m_config_file_name)
        self.m_ranch = Ranch()
        self.m_ranch.set_name(self.m_config_parser["Ranch"]["name"])
        self.m_ranch.set_location(self.m_config_parser["Ranch"]["location"])
        self.m_ranch.set_description(self.m_config_parser["Ranch"]["description"])

    def save(self):
        with open(self.m_config_file_name, 'wt') as f:
            self.m_config_parser.write(f);

    def get(self):
        return self.m_ranch

    def update(self, ranch):
        if ranch.is_complete():
            self.m_ranch.set_name(ranch.get_name())
            self.m_ranch.set_location(ranch.get_location())
            self.m_ranch.set_description(ranch.get_description())

            self.m_config_parser["Ranch"]["name"] = ranch.get_name()
            self.m_config_parser["Ranch"]["location"] = ranch.get_location()
            self.m_config_parser["Ranch"]["description"] = ranch.get_description()
