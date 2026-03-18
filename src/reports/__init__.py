import os
import importlib

module_dir = os.path.dirname(__file__)
for filename in os.listdir(module_dir):
    if filename.endswith(".py") and filename != "__init__.py" and filename != "base.py":
        module_name = filename[:-3]
        importlib.import_module(f"src.reports.{module_name}")
