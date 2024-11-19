from repo.lot_storage import LotStorage
from model.vehicle import Vehicle

class ParkVehicleService:
  storage: LotStorage
  
  def __init__(self, storage: LotStorage) -> None:
    self.storage = storage
  
  def do(self, lotID: str, vType: str, regNum: str, color: str) -> str:
    vehicle = Vehicle(vType, regNum, color)
    lot = self.storage.find(lotID)
    if lot is None:
      print("Lot not found")
      return "lot not found"
    return lot.park(vehicle)
