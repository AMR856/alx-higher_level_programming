#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
    int mySize = PY_SIZE(p);
    int myAllocation;
    printf("[*] Size of the Python List = %d\n", mySize);
    myAllocation = 
}
