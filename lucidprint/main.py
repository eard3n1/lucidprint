class Styles:  
    RESET     = "\033[0m"
    BOLD      = "\033[1m"
    FAINT     = "\033[2m"
    ITALIC    = "\033[3m"
    UNDERLINE = "\033[4m"
    
class Colors:
    RED    = "\033[91m"
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    BLUE   = "\033[94m" 

def _print(msg: str, color: str="", bold=False, faint=False, italic=False, underline=False):
    style = ""

    if bold:      style += Styles.BOLD
    if faint:     style += Styles.FAINT
    if italic:    style += Styles.ITALIC
    if underline: style += Styles.UNDERLINE

    print(f"{style}{color}{msg}{Styles.RESET}")

def success(msg: str):
    """
    Green, bold, italic
    """
    _print(msg, color=Colors.GREEN, bold=True, italic=True)

def info(msg: str):
    """
    Blue, italic
    """
    _print(msg, color=Colors.BLUE, italic=True)

def note(msg: str):
    """
    Faint
    """
    _print(msg, faint=True)

def warn(msg: str):
    """
    Yellow, bold, underline
    """
    _print(msg, color=Colors.YELLOW, bold=True, underline=True)

def error(msg: str):
    """
    Red, underline
    """
    _print(msg, color=Colors.RED, underline=True)

def progress(current: int, total: int, length: int = 40):
    """
    A progress bar that updates in place.

    Args:
        current (int): Current progress value.
        total   (int): Total value for completion.
        length  (int): Length of the progress bar.
    """
    if total <= 0: raise ValueError("Total value must be greater than zero.")
    if current < 0: raise ValueError("Current value cannot be negative.")
    if total < current: raise ValueError("Current value cannot exceed total value.")

    percent = min(current / total, 1.0)
    filled = int(length * percent)
    bar = "#" * filled + "-" * (length - filled)

    print(f"\r|{bar}| {percent:.1%}", end='\r')
    if current >= total: print()