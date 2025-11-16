class BrightNess:
  def __init__(self,port:str):
    pass
  def measurement(self) -> int:
    """Return current brightness measurement."""
    return 0

  def range(self,min_val: int, max_val: int):
    """Set brightness range."""
    pass
def light_level(port:str):
  return BrightNess(port)