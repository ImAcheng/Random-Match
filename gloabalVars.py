# global used variables
LeftButtonPressingTime: int = 0
ResultMessage: str = ""
isProgramRunning: bool = True
InputFieldType = "name"
isCursorStatementChanged: bool = False
ResNeedsUpdate: bool = False
Matched_Groups: list = []
detected_unknown_error = None

mousePos: tuple = (0, 0)

# global used components
import fileManager
fM = fileManager.FileManager()