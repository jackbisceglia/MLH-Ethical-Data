from src.welcome import welcome
from src.end import end
from src.inputLoop import mainLoop
from src.history import History

# Main Execution Context
if __name__ == "__main__":
    welcome()
    history = History()
    mainLoop(history)
    end()
