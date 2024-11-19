from model.parking_lot import ParkingLot
from repo.lot_storage import LotStorage
from service.create_parking_lot import CreateParkingLotService
from service.park_vehicle import ParkVehicleService
from service.unpark_vehicle import UnparkVehicleService
from service.display import DisplayService

def main():
  db = LotStorage()
  createSvc = CreateParkingLotService(db)
  parkSvc = ParkVehicleService(db)
  unparkSvc = UnparkVehicleService(db)
  displaySvc = DisplayService(db)
  currLot = None
  while True:
    command = input("$ ")
    commands = command.split(" ")
    if command == "exit":
      break
    elif len(commands) == 0:
      continue
    elif commands[0] == "create_parking_lot":
      if len(commands) != 4:
        print("invalid params")
        continue
      currLot = createSvc.do(commands[1], int(commands[2]), int(commands[3]))
      print("Created parking lot with {0} floors and {1} slots per floor".format(int(commands[2]), int(commands[3])))
    elif commands[0] == "display":
      if len(commands) != 3:
        print("invalid params")
        continue
      if commands[1] == "free_count":
        displaySvc.displayFreeCount(currLot.getID(), commands[2])
      elif commands[1] == "free_slots":
        displaySvc.displayFreeSlots(currLot.getID(), commands[2])
      elif commands[1] == "occupied_slots":
        displaySvc.displayOccupied(currLot.getID(), commands[2])
    elif commands[0] == "park_vehicle":
      if len(commands) != 4:
        print("invalid params")
        continue
      ticket = parkSvc.do(currLot.getID(), commands[1], commands[2], commands[3])
      if ticket is None:
        print("Parking Lot Full")
        continue
      print("Parked vehicle. Ticket ID: {0}".format(ticket))
    elif commands[0] == "unpark_vehicle":
      if len(commands) != 2:
        print("invalid params")
        continue
      unparkSvc.do(commands[1])
    else:
      print("invalid command")

main()