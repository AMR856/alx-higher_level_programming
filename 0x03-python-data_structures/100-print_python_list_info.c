#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - A function to print the
 * info about a list in python
 * @p: A pointer to python object
 *
 * Return: Nothing (void)
*/

void print_python_list_info(PyObject *p)
{
	int mySize = PyList_Size(p), i;
	PyListObject *myObject = (PyListObject *)p;
	printf("[*] Size of the Python List = %d\n", mySize);
	printf("[*] Allocated = %d\n", myObject->allocated);
	for (i = 0; i < mySize; i++)
	{
		print("Element %i: %s\n",i,
		Py_TYPE(myObject->ob_item[i])->tp_name);
	}
}
