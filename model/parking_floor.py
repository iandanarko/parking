import heapq
from typing import List
from model.parking_slot import ParkingSlot
from model.vehicle import Vehicle


class ParkingFloor:
  slots: List[ParkingSlot]

  def __init__(self, parkID: int, floorNum: int, numOfSlots: int):
    self.parkID = parkID
    self.floorNum = floorNum
    self.slots = []
    self.freeSlots = []
    for i in range(numOfSlots):
      self.addSlot()
  
  def getFloorNum(self) -> int:
    return self.floorNum
  
  def addSlot(self):
    n = len(self.slots)
    t = "TRUCK"
    if n > 1 or n < 3:
      t = "BIKE"
    if n >= 3:
      t = "CAR"
    slot = ParkingSlot(t, self.parkID, self.floorNum, n+1)
    self.slots.append(slot)
    if n >= 3:
      heapq.heappush(self.freeSlots, n)
  
  def getAvailSlots(self, vtype: str) -> List[int]:
    if vtype == "TRUCK":
      return [1] if self.isAvail(vtype) else []
    elif vtype == "BIKE":
      res = []
      if len(self.slots) >= 2 and self.slots[1].getVehicle() is None:
        res.append(2)
      if len(self.slots) >= 3 and self.slots[2].getVehicle() is None:
        res.append(3)
      return res
    else:
      return [i+1 for i in self.freeSlots]

  def getOccupied(self, vtype: str) -> List[int]:
    if vtype == "TRUCK":
      return [] if self.isAvail(vtype) else [1]
    elif vtype == "BIKE":
      res = []
      if len(self.slots) >= 2 and self.slots[1].getVehicle() is not None:
        res.append(2)
      if len(self.slots) >= 3 and self.slots[2].getVehicle() is not None:
        res.append(3)
      return res
    else:
      return [i+1 for i in range(3,len(self.slots)) if self.slots[i].getVehicle() is not None]

  def getAvailCount(self, vtype: str) -> int:
    if vtype == "TRUCK":
      return 1 if self.isAvail(vtype) else 0
    elif vtype == "BIKE":
      if len(self.slots) < 2:
        return 0
      count = 0
      if len(self.slots) >= 2 and self.slots[1].getVehicle() is None:
        count += 1
      if len(self.slots) >= 3 and self.slots[2].getVehicle() is None:
        count += 1
      return count
    return len(self.freeSlots)

  def isAvail(self, vtype: str):
    if vtype == "TRUCK":
      return True if len(self.slots) > 0 and self.slots[0].getVehicle() is None else False
    elif vtype == "BIKE":
      if len(self.slots) > 1 and self.slots[1].getVehicle() is None:
        return True
      if len(self.slots) > 2 and self.slots[2].getVehicle() is None:
        return True
      return False
    else:
      return len(self.freeSlots) > 0
  
  def park(self, vehicle: Vehicle):
    vtype = vehicle.getType()
    if vtype == "TRUCK":
      return self.slots[0].setVehicle(vehicle)
    elif vtype == "BIKE":
      if len(self.slots) > 2 and self.slots[1].getVehicle() is None:
        return self.slots[1].setVehicle(vehicle)
      elif len(self.slots) > 3 and self.slots[2].getVehicle() is None:
        return self.slots[2].setVehicle(vehicle)
    else:
      i = heapq.heappop(self.freeSlots)
      return self.slots[i].setVehicle(vehicle)
  
  def unpark(self, slotNum: int) -> Vehicle:
    if slotNum > len(self.slots)-1:
      return None
    v = self.slots[slotNum-1].getVehicle()
    self.slots[slotNum-1].freeVehicle()
    if v is not None and slotNum > 3:
      heapq.heappush(self.freeSlots, slotNum-1)
    return v
