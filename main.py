import projectkernel
import projectkernel.reservation
from projectkernel.reservation import Reservation
import projectkernel.reservationdataaccess
from projectkernel.reservationdataaccess import ReservationDataAccess
import projectkernel.comment
from projectkernel.comment import Comment
import projectkernel.commentdataaccess
from projectkernel.commentdataaccess import CommentDataAccess

#TODO: an App class

if __name__ == "__main__":
    rda = ReservationDataAccess("./data/Reservation.ini")
    cda = CommentDataAccess("./data/Comment.ini")

    while True:
        print("=========================")
        print("1. Load")
        print("2. Save")
        print("3. List comments")
        print("4. Add a comment")
        print("5. Delete a comment")
        print("6. Update a comment")
        print("7. List reservations")
        print("8. Make a reservation")
        print("9. Delete a reservation")
        print("10. Update a reservation")
        print("11. Quit")
        choice = "";
        try :
            choice = input("Your choice:")
        except EOFError:
            choice = "QUIT"
    
        if choice=="1":
            rda.load()
            cda.load()
        elif choice=="2":
            rda.save()
            cda.save()
        elif choice=="3":
            clist = cda.list_all_comments()
            for c in clist:
                print("=========================")
                print("id:", c.get_id())
                print("user:", c.get_user_name())
                print("time:", c.get_time_as_str())
                print("message:", c.get_message())
        elif choice=="4":
            try :
                c = Comment()
                c.set_id("0")
                name = input("User name:")
                c.set_user_name(name)
                c.set_time_now()
                msg = input("Comment:")
                c.set_message(msg)
                cda.add_comment(c)
            except EOFError:
                print("Action canceled")
        elif choice=="5":
            try :
                id = input("Delete the comment with this id:")
                cda.delete_comment_by_id(id)
            except EOFError:
                print("Action canceled")
        elif choice=="6": 
            try :
                c = Comment()
                id = input("Update the comment with this id:")
                c.set_id(id)
                name = input("User name:")
                c.set_user_name(name)
                c.set_time_now()
                msg = input("Comment:")
                c.set_message(msg)
                cda.update_comment(c)
            except EOFError:
                print("Action canceled")
            except ValueError:
                print("Value Error")
        elif choice=="7":
            rlist = rda.list_all_reservations()
            for r in rlist:
                print("=========================")
                print("id:", r.get_id())
                print("reserver:", r.get_reserver_name())
                print("room id:", r.get_reserved_room_id())
                print("start time:", r.get_start_time_as_str())
                print("end time:", r.get_end_time_as_str())
            pass
        elif choice=="8":
            try :
                r = Reservation()
                r.set_id("0")
                name = input("Reserver name:")
                r.set_reserver_name(name)
                roomid = int(input("Room ID:"))
                r.set_reserved_room_id(roomid)
                year = int(input("start year:"))
                month = int(input("start month:"))
                day = int(input("start day:"))
                hour = int(input("start hour:"))
                r.set_start_time(year, month, day, hour)
                year = int(input("end year:"))
                month = int(input("end month:"))
                day = int(input("end day:"))
                hour = int(input("end hour:"))
                r.set_end_time(year, month, day, hour)
                cda.add_comment(c)
            except EOFError:
                print("Action canceled")
            except ValueError:
                print("Value Error")
        elif choice=="9":
            try :
                id = input("Delete the comment with this id:")
                rda.delete_reservation_by_id(id)
            except EOFError:
                print("Action canceled")
        elif choice=="10":
            try :
                r = Reservation()
                id = input("Update the reservation with this id:")
                r.set_id(id)
                name = input("Reserver name:")
                r.set_reserver_name(name)
                roomid = int(input("Room ID:"))
                r.set_reserved_room_id(roomid)
                year = int(input("start year:"))
                month = int(input("start month:"))
                day = int(input("start day:"))
                hour = int(input("start hour:"))
                r.set_start_time(year, month, day, hour)
                year = int(input("end year:"))
                month = int(input("end month:"))
                day = int(input("end day:"))
                hour = int(input("end hour:"))
                r.set_end_time(year, month, day, hour)
                cda.update_comment(c)
            except EOFError:
                print("Action canceled")
            except ValueError:
                print("Value Error")
        elif choice=="11":
            break
        elif choice=="QUIT":
            break
    print("")
