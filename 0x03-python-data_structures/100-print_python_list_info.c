#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_into - print python list
 *
 * @pyobject: the different pyhton object
 * @p: list
 */

void print_python_list_info(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("[!] Error: Input is not a list.\n");
		return;
	}

	Py_ssize_t list_size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %zd\n", list_size);
	printf("[*] Allocated = %zd\n", allocated);

	for (Py_ssize_t i = 0; i < list_size; i++)
	{
		PyObject *element = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(element)->tp_name);
	}
}
