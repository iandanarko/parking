from typing import Optional
from model.parking_lot import ParkingLot
class LotStorage:
  def __init__(self) -> None:
    self.dict = {}
  
  def insert(self, lot: ParkingLot):
    self.dict[lot.getID()] = lot

  def find(self, id: str) -> Optional[ParkingLot]:
    return self.dict.get(id)