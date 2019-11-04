def printColumn(e):
    print(e)

import re
def checkFormat(e,Format):
    return re.search(Format,e) is not None

def printFormatError(e,Format):
    if not checkFormat(e,Format):
        print(e)