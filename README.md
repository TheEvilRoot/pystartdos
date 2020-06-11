pystartdos
-----

Little script program to start dosbox from command line.

Now it's allow to open `cpp`, `exe`, `com` and `asm` files in dosbox with specific application.

Code doesn't adapted to another system, only mine. :)

Will refactor this as fast as I can...

Requirements
-----

- Python 3.6 +
- macOS for now (uses `open` command for now, will be refactored)

Installation
-------

Link startdos.py to directory from `PATH` and make it executable

```bash

ln -s startdos.py ~/.local/bin/startdos

```

```bash

chmod +x startdos.py

```

Usage
-----

Simply run

```bash

startdos <exe-file> | <asm-file> | <com-file> | <cpp-file> [arguments...]

```
