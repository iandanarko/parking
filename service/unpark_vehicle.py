from repo.lot_storage import LotStorage

class UnparkVehicleService:
  storage: LotStorage
  
  def __init__(self, storage: LotStorage) -> None:
    self.storage = storage
  
  def do(self, ticketID: str):
    arr = ticketID.split("_")
    lot = self.storage.find(arr[0])
    if lot is None:
      print("Lot not found")
      return
    v = lot.unpark(int(arr[1]), int(arr[2]))
    if v is not None:
      print("Unparked vehicle with Registration Number: {0} and Color {1}".format(v.getReqNum(), v.getColor()))
    else:
      print("Invalid ticket")