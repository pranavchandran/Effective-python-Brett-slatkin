import importlib
mod = importlib.import_module('module1')
print(mod.__name__)

mod = importlib.import_module('module2')
print(mod.__name__)

mod.main()
