from typing import Optional
from model.vehicle import Vehicle


class ParkingSlot:
  def __init__(self, vtype: str, parkId: str, floorNum: int, slotsNum: int) -> None:
    self.vtype = vtype
    self.floorNum = floorNum
    self.parkId = parkId
    self.slotNum = slotsNum
    self.vehicle = None

  def getticketid(self) -> str:
      return "{0}_{1}_{2}".format(self.parkId, self.floorNum, self.slotNum)
  
  def park(self, vehicle: Vehicle):
    self.vehicle = vehicle

  def getVehicle(self) -> Vehicle:
    return self.vehicle
  
  def setVehicle(self, v: Vehicle):
    self.vehicle = v
    return "{0}_{1}_{2}".format(self.parkId, self.floorNum, self.slotNum)
  
  def freeVehicle(self):
    self.vehicle = None
  