from repo.lot_storage import LotStorage
from model.parking_lot import ParkingLot

class CreateParkingLotService:
  storage: LotStorage
  
  def __init__(self, storage: LotStorage) -> None:
    self.storage = storage

  def do(self, id: str, numFloor: int, numOfSlots: int) -> ParkingLot:
    lot = ParkingLot(id)
    for i in range(numFloor):
      lot.addFloor(numOfSlots)
    self.storage.insert(lot)
    return lot

