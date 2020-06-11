#!/usr/bin/env python3

import sys
import os
import subprocess

base_cfg_file = "/Development/DOS/Borland/base.cfg"
temp_cfg_file = "/Development/DOS/Borland/temp.cfg"

cpp_exts = ['cpp', 'cc', 'c', 'CPP', 'CC', 'C']
exe_exts = ['EXE', 'exe']
asm_exts = ['asm']

def make(file_path: str, strs):
  file_dir = os.path.dirname(os.path.abspath(file_path))
  print(f'file dir: {file_dir}')
  with open(base_cfg_file, 'r') as base:
    with open(temp_cfg_file, 'w+') as file:
      file.write(base.read())
      file.write('\n')
      file.write(f'mount x "{file_dir}"\n')
      file.write('\n'.join(strs))
 
def file_name(f: str):
  return f.split('/')[-1]

def make_for_cpp(cpp: str, extra):
  cpp_file = file_name(cpp) 
  make(cpp, [f'c:\\Borland\\Borlandc\\bin\\bc.exe x:\\{cpp_file}\n', f'exit\n'])

def make_for_exe(exe: str, extra):
  exe_file = file_name(exe) 
  args = ' '.join(extra)
  make(exe, [f'x:\\{exe_file} {args}'])

def make_for_asm(asm: str, extra):
    asm_file = file_name(asm)
    name = '.'.join(asm_file.split('.')[:-1])
    args = ' '.join(extra)
    make(asm, ['x:', 'mkdir out', 'cd out', f'del {name}.*', f'tasm ..\\{asm_file}', f'tlink {name}.obj', f'{name}.exe {args}'])

def start_with_temp():
  subprocess.run(["open", "-W", "-a", "dosbox", "--args", "-conf", temp_cfg_file])

def consume_file(argv):
  return argv[1], argv[2:]

def main(argv):
  if len(argv) > 1:
    file, extra = consume_file(argv)
    ext = file.split('.')[-1]
    if ext in cpp_exts:
      make_for_cpp(file, extra)
    elif ext in exe_exts:
      make_for_exe(file, extra)
    elif ext in asm_exts:
      make_for_asm(file, extra)
    start_with_temp()
  else:
    print('Invalid arguments')
    return 1
  return 0

if __name__ == '__main__':
  exit(main(sys.argv))
