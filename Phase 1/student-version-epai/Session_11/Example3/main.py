# main.py

import os.path
import types
import sys

module_name = "module1"
module_file = 'module1_source.py'
module_path = '.'

module_rel_file_path = os.path.join(module_path, module_file)
module_abs_file_path = os.path.abspath(module_rel_file_path)

with open(module_rel_file_path, 'r') as code_file:
    source_code = code_file.read()

# create a module object
mod = types.ModuleType(module_name)
mod.__file__ = module_abs_file_path

sys.modules[module_name] = mod

code = compile(source_code, filename=module_abs_file_path, mode='exec')

exec(code, mod.__dict__)

mod.hello()
