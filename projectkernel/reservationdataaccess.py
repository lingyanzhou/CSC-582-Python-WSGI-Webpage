"""
 @author Lingyan Zhou
"""
from . import reservation

import configparser

class ReservationDataAccess:
    def __init__(self, filename):
        self.m_config_parser = configparser.ConfigParser()
        self.m_config_file_name = filename;
        self.m_reservations = []

    def load(self):
        self.m_config_parser.read(self.m_config_file_name)
        self.m_reservations = list()
        for id in self.m_config_parser.sections():
            r = reservation.Reservation()
            r.set_id(id)
            r.set_start_time_by_str(self.m_config_parser[id]["start_time"], "%x %X")
            r.set_end_time_by_str(self.m_config_parser[id]["end_time"], "%x %X")
            r.set_reserver_name(self.m_config_parser[id]["reserver"])
            r.set_reserved_room_id(self.m_config_parser[id]["room_id"])
            self.m_reservations.append(r)

    def save(self):
        with open(self.m_config_file_name, 'wt') as f:
            self.m_config_parser.write(f);

    def list_all_reservations(self):
        return list(self.m_reservations)

    def list_reservations_by_reserver(self, name):
        l = list()
        for rsv in self.m_reservations:
            if rsv.get_resever_name() == name:
                l.append(rsv)
        return l

    def list_reservations_by_room_id(self, room_id):
        l = list()
        for rsv in self.m_reservations:
            if rsv.get_room_id() == room_id:
                l.append(rsv)
        return l
    
    def add_reservation(self, rsv):
        if (not rsv.is_reservation_complete()
                and not rsv.is_reservation_time_valid()
                and  rsv.has_expired()):
            return False
        
        for existing_rsv in self.m_reservations:
            if rsv is existing_rsv:
                return False

        for existing_rsv in self.m_reservations:
            if rsv.conflict_with(existing_rsv):
                return False

        newid = rsv.get_id();
        if newid!=None and newid not in self.m_config_parser.sections():
            pass
        else :
            id = 0;
            while True:
                if str(id) not in self.m_config_parser.sections():
                    newid = str(id)
                    break
                id += 1
            rsv.set_id(newid);
            
        newrsv = reservation.Reservation()
        newrsv.set_id(rsv.get_id())
        newrsv.set_start_time_by_str(rsv.get_start_time_as_str())
        newrsv.set_end_time_by_str(rsv.get_end_time_as_str())
        newrsv.set_reserver_name(rsv.get_reserver_name())
        newrsv.set_reserved_room_id(rsv.get_reserved_room_id())
        self.m_reservations.append(newrsv)

        self.m_config_parser[newid] = {}
        self.m_config_parser[newid]["start_time"] = rsv.get_start_time_as_str()
        self.m_config_parser[newid]["end_time"] = rsv.get_end_time_as_str()
        self.m_config_parser[newid]["reserver"] = rsv.get_reserver_name()
        self.m_config_parser[newid]["room_id"] = rsv.get_reserved_room_id()

        return True;

    def update_reservation(self, rsv):
        if (self.m_config_parser.has_section(rsv.get_id())):
            for existing_rsv in self.m_reservations:
                if existing_rsv.get_id()!= rsv.get_id() and rsv.conflict_with(existing_rsv):
                    return False

            for existing_rsv in self.m_reservations:
                if existing_rsv.get_id()== rsv.get_id():
                    existing_rsv.set_start_time_by_str(rsv.get_start_time_as_str())
                    existing_rsv.set_end_time_by_str(rsv.get_end_time_as_str())
                    existing_rsv.set_reserver_name(rsv.get_reserver_name())
                    existing_rsv.set_reserved_room_id(rsv.get_reserved_room_id())
            self.m_config_parser[rsv.get_id()]["start_time"] = rsv.get_start_time_as_str()
            self.m_config_parser[rsv.get_id()]["end_time"] = rsv.get_end_time_as_str()
            self.m_config_parser[rsv.get_id()]["reserver"] = rsv.get_reserver_name()
            self.m_config_parser[rsv.get_id()]["room_id"] = rsv.get_reserved_room_id()
            return True
        else :
            return False
        
    def delete_reservation_by_id(self, id):
        for i in range(len(self.m_reservations)):
            if self.m_reservations[i].get_id()==id:
                self.m_reservations.remove(self.m_reservations[i])
                break
        self.m_config_parser.remove_section(id)