// #include <Python.h>
// #include <stdio.h>
// #include <string.h>

// /**
//  * print_python_list_info - A function to print the
//  * info about a list in Python
//  * @p: A pointer to a Python object
//  *
//  * Return: Nothing (void)
//  */

// void print_python_list_info(PyObject *p)
// {
//     long int mySize = PyList_Size(p);
//     int i;
//     PyListObject *myObject = (PyListObject *)p;

//     printf("[*] Size of the Python List = %li\n", mySize);
//     printf("[*] Allocated = %li\n", myObject->allocated);
//     for (i = 0; i < mySize; i++)
//     {
//         printf("Element %i: %s\n", i, Py_TYPE(myObject->ob_item[i])->tp_name);
//     }
// }