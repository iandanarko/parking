import heapq
from typing import List
from model.parking_floor import ParkingFloor
from model.vehicle import Vehicle


class ParkingLot:
  floors: List[ParkingFloor]

  def __init__(self, id: str):
    self.id = id
    self.floorNum = 0
    self.floors = []
    self.freeTruckFloors = []
    self.freeBikeFloors = []
    self.freeCarFloors = []
  
  def getID(self) -> str:
    return self.id

  def getFloor(self) -> List[ParkingFloor]:
    return self.floors

  def addFloor(self, numOfSlots: int) -> None:
    self.floorNum += 1
    self.floors.append(ParkingFloor(self.id, self.floorNum, numOfSlots))
    if numOfSlots > 0:
      heapq.heappush(self.freeTruckFloors, self.floorNum-1)
    if numOfSlots > 1:
      heapq.heappush(self.freeBikeFloors, self.floorNum-1)
    if numOfSlots > 3:
      heapq.heappush(self.freeCarFloors, self.floorNum-1)

  def park(self, vehicle: Vehicle) -> str:
    if vehicle.getType() == "TRUCK" and len(self.freeTruckFloors) != 0:
      floorNum = heapq.heappop(self.freeTruckFloors)
      return self.floors[floorNum].park(vehicle)
    elif vehicle.getType() == "BIKE" and len(self.freeBikeFloors) != 0:
      floorNum = self.freeBikeFloors[0]
      ticket = self.floors[floorNum].park(vehicle)
      if self.floors[floorNum].isAvail(vehicle.getType()) == False:
        heapq.heappop(self.freeBikeFloors)
      return ticket
    elif vehicle.getType() == "CAR" and len(self.freeCarFloors) != 0:
      floorNum = self.freeCarFloors[0]
      ticket =  self.floors[floorNum].park(vehicle)
      if self.floors[floorNum].isAvail(vehicle.getType()) == False:
        heapq.heappop(self.freeCarFloors)
      return ticket
    else:
      return None
  
  def unpark(self, floorNum: int, slotNum: int) -> Vehicle:
    v = self.floors[floorNum-1].unpark(slotNum)
    if slotNum == 1:
      heapq.heappush(self.freeTruckFloors, self.floorNum-1)
    elif (slotNum <= 3) and (floorNum-1) not in self.freeBikeFloors:
      heapq.heappush(self.freeBikeFloors, self.floorNum-1)
    elif slotNum > 3 and (floorNum-1) not in self.freeCarFloors:
      heapq.heappush(self.freeCarFloors, self.floorNum-1)
    return v
