from src.cliFunctionality.helpMenu import helpMenu

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
        
        handleFlag(parseInput(usrInput))
    return

# PARSE THE INPUT, ERROR CHECKING, and TOKENIZE INTO FLAG(S)
def parseInput(usrInput: str) -> str:
    tokens = usrInput.split(' ')    
    # error handling: incorrect command entered
    if tokens[0].upper() != 'MLH':
        handleError('cnf')
        return
    
    # error handle (future): unkown command
    tokens[1] = tokens[1].strip('-')
    return (tokens[1:])

# HANDLE THE FLAGS PASSED IN
def handleFlag(flag: str) -> None:
    type = flag[0]
    options = flag[1:]
    
    flags = {
        'h': helpMenu
    }

    flags[type](options)


# ERROR HANDLING
def handleError(type: str) -> None:
    # CASES 
    def invalid_caf():
        print("Invalid Inpt: Character(s) found after command")

    def invalid_cnf():
        print("Invalid Input: Prefix command is something other than 'MLH'")

    # HANDLING CASES
    options = {
        'caf' : invalid_caf,
        'caf' : invalid_caf,
    }
        
    options[type]()