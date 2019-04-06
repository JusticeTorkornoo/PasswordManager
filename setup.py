from cx_Freeze import setup, Executable

setup(name='pass', version='1.0', desctription='stuff', executables = [Executable("Show_Accounts.py")])