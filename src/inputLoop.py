from src.cliFunctionality.helpMenu import helpMenu
from src.cliFunctionality.openPorts import openPorts
from src.cliFunctionality.closePorts import closePorts
from src.cliFunctionality.listPorts import listPorts
from src.cliFunctionality.funFacts import funFacts

# MAIN EVENT LOOP
def mainLoop() -> None:
    usrInput = ''
    terminate = False

    while (not terminate):
        usrInput = str(input('> '))
        # CASE: Break in event of a 'q' or 'Q' entered
        if usrInput.lower() == 'q':
            terminate = True
            continue
        
        parsed = parseInput(usrInput)
        if parsed:
            handleFlag(parsed)
    return

def getFlags() -> dict:
    return {
        'h': helpMenu,
        'help': helpMenu,
        'o': openPorts,
        'c': closePorts,
        'l': listPorts,
        'f': funFacts
    }


# PARSE THE INPUT, ERROR CHECKING, and TOKENIZE INTO FLAG(S)
def parseInput(usrInput: str) -> str:
    tokens = usrInput.split(' ')
    flags = getFlags()
    
    # ERROR CASES
    if len(tokens) == 0:
        handleError('nc')
        return

    if tokens[0].upper() != 'MLH':
        handleError('cnf')
        return
    
    if tokens[1][0] != '-':
        handleError('nf')
        return

    tokens[1] = tokens[1].strip('-')

    if not tokens[1] in flags:
        handleError('fnf')
        return
    
    # error handle (future): unkown command
    return (tokens[1:])

# HANDLE THE FLAGS PASSED IN
def handleFlag(command: str) -> None:
    # Seperate flag from options
    options = command[1:]
    type = command[0]
    # Retreive flags from function above
    flags = getFlags()

    flags[type](options)


# ERROR HANDLING
def handleError(type: str) -> None:
    # CASES 
    def invalid_caf():
        print("Invalid Inpt: Character(s) found after command")

    def invalid_cnf():
        print("Invalid Input: Prefix command is something other than 'MLH'")

    def invalid_nc():
        print("Invalid Input: No characters found")

    def invalid_nf():
        print("Invalid Input: No flag found")

    def invalid_fne():
        print("Invalid Input: Flag does not exist")

    # HANDLING CASES
    options = {
        'caf' : invalid_caf,
        'caf' : invalid_caf,
        'cn' : invalid_nc,
        'nf' : invalid_nf,
        'fne' : invalid_fne
    }

    # CASE TO CATCH UNHANDLED ERROR -> TO BE CHANGED LATER
    if not type in options:
        print("Invalid Input: Unknown Error")
    else:
        options[type]()