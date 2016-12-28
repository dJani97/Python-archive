import cx_Freeze

executables = [cx_Freeze.Executable("Legi_csata.py")]

cx_Freeze.setup(
    name = "Test",
    options = {"build_exe":{"packages":["pygame"], "include_files":["plane3.png"]}},
    description = "Snake with pygame",
    executables = executables
    )
