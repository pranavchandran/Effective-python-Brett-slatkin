#module_from_spec(spec)
#Create a new module based on spec and spec.loader.create_module.

import importlib.util

def check_module(mod):
    spec = importlib.util.find_spec(mod)
    if spec is None:
        print('Module: {} not found'.format(mod))
        return None
    else:
        print('Module: {} can be imported!'.format(mod))
        return spec

def import_module(spec):
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

if __name__ == '__main__':
    spec = check_module('not a module')
    spec = check_module('module1')
    if spec:
        mod = import_module(spec)
        mod.main()

