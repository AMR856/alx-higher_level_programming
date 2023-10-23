#!/usr/bin/python3
import dis
bytecode = dis.Bytecode(magic_calculation)
for instruction in bytecode:
    line_number = instruction.starts_line if instruction.starts_line is not None else ''
    print(f"Line {line_number}: {instruction.opname.ljust(20)} {instruction.argrepr}")