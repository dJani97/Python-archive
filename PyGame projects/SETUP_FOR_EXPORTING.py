import cx_Freeze

executables = [cx_Freeze.Executable("pygame_snake OOP.py")]

cx_Freeze.setup(
    name = "Snake",
    options = {"build_exe":{"packages":["pygame"], "include_files":["SnakeHeadGreen.png", "SnakeHeadPurple.png", "Apple.png"]}},
    description = "Snake with pygame",
    executables = executables
    )
