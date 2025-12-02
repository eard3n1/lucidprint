# lucidprint
A small Python utility library offering conditional styles for CLIs.

## Features
- Coherent printing style for different conditions
- Lightweight, easy to use
- No dependencies

## Installation
```bash
pip install lucidprint
```

## Examples
- #### Printing:
```python
from lucidprint import success, info, note, warn, error

success("Success") # Green, bold, italic
info("Info")       # Blue, italic
note("Note")       # Faint
warn("Warn")       # Yellow, bold, underline
error("Error")     # Red, underline
```
- #### Progress Bar:
```python
from lucidprint import progress
import time # for better visualization

total = 100
for current in range(total + 1):
    progress(current=current, total=total)
    time.sleep(0.05)
```

## Reference
- <code>success(msg: str)</code><br>Green, bold, italic<br><br>
- <code>info(msg: str)</code><br>Blue, italic<br><br>
- <code>note(msg: str)</code><br>Faint<br><br>
- <code>warn(msg: str)</code><br>Yellow, bold, underline<br><br>
- <code>error(msg: str)</code><br>Red, underline<br><br>
- <code>progress(current: int, total: int, length: int = 40)</code><br>A simple progress bar that updates in place

## License
MIT License