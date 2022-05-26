import os, importlib

# Importing the alert_modules folder, all the modules it contains are imported.

for module in os.listdir(os.path.dirname(__file__)):
    if module == '__init__.py' or module[-3:] != '.py':
        continue
    globals()[module[:-3]] = importlib.import_module('.' + module[:-3], package=__name__)
del module
