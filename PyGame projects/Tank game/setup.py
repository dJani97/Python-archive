import cx_Freeze

executables = [cx_Freeze.Executable("Tank game.py")]

cx_Freeze.setup(
    name = "Tank",
    options = {"build_exe":{"packages":["pygame", "random", "math"], "include_files":[]}},
    description = "Snake with pygame",
    executables = executables
    )
