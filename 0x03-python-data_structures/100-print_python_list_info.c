// #include <Python.h>
// #include <object.h>
// #include <listobject.h>
// #include <stdio.h>

// /**
//  * print_python_list_info - A function to print the
//  * info about a list in python
//  * @p: A pointer to python object
//  *
//  * Return: Nothing (void)
// */

// void print_python_list_info(PyObject *p)
// {
// 	int mySize = PY_SIZE(p), myAllocation, i;
// 	PyObject *myObject;

// 	printf("[*] Size of the Python List = %d\n", mySize);
// 	myAllocation = (*((PyListObject *)p)).allocated;
// 	printf("[*] Size of the Python List = %d\n", mySize);
// 	printf("[*] Allocated = %d\n", myAllocation);
// 	for (i = 0; i < mySize; i++)
// 	{
// 		myObject = PyList_GET_ITEM(p, i);
// 		printf("Element %d: %s", i, PY_TYPE((myObject)->tp_name));
// 	}
// }


#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
