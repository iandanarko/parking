from repo.lot_storage import LotStorage

class DisplayService:
  storage: LotStorage
  
  def __init__(self, storage: LotStorage) -> None:
    self.storage = storage

  def displayFreeCount(self, lotID: str, vtype: str):
    lot = self.storage.find(lotID)
    if lot is None:
      print("Lot not found")
      return
    floors = lot.getFloor()
    for f in floors:
      print("No. of free slots for {0} on Floor {1}: {2}".format(vtype, f.getFloorNum(), f.getAvailCount(vtype)))

  def displayFreeSlots(self, lotID: str, vtype: str):
    lot = self.storage.find(lotID)
    if lot is None:
      print("Lot not found")
      return 
    floors = lot.getFloor()
    for f in floors:
      print("Free slots for {0} on Floor {1}: {2}".format(vtype, f.getFloorNum(), tuple(f.getAvailSlots(vtype))))

  def displayOccupied(self, lotID: str, vtype: str):
    lot = self.storage.find(lotID)
    if lot is None:
      print("Lot not found")
      return
    floors = lot.getFloor()
    for f in floors:
      print("Free slots for {0} on Floor {1}: {2}".format(vtype, f.getFloorNum(), tuple(f.getOccupied(vtype))))
