class Vehicle:
  def __init__(self, vtype: str, regNum: str, color: str) -> None:
    self.vtype = vtype
    self.regNum = regNum
    self.color = color
  
  def getType(self)-> str:
    return self.vtype
  
  def getReqNum(self) -> str:
    return self.regNum
  
  def getColor(self) -> str:
    return self.color
  