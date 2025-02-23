import os
import importlib

# get all the python files in current folder except __init__.py and test_dfs.py
module_files = [f[:-3] for f in os.listdir(os.path.dirname(__file__))
                if f.endswith(".py") and f not in ("__init__.py", "test_bfs.py")]

# import all modules dynamically
for module in module_files:
    importlib.import_module("." + module, package=__name__)
