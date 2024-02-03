#include <stdio.h>
#include <stddef.h>
#include <Python.h>

void print_python_list(PyObject *p)
{
	int i;
	Py_ssize_t list_size = 0;

	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List object\n");
		return;
	}
	
	while (PyList_GET_ITEM(p, list_size) != NULL)
		list_size++;
	printf("  size: %zd\n", list_size);

	for (i = 0; i < list_size && i < 10; i++)
		printf("  [%d] %s\n", i, Py_TYPE(PyList_GET_ITEM(p, i))->tp_name);
	
	if (list_size > 10)
		printf("  [...]\n");
}

void print_python_bytes(PyObject *p)
{
	int i;
	char *bytes_data = (char *)PyBytes_AS_STRING(p);
	Py_ssize_t bytes_size = ((PyBytesObject *)p)->ob_shash;
	
	printf("[*] Python bytes info\n");
	
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes object\n");
		return;
	}
	
	printf("  size: %zd\n", bytes_size);
	printf("  first %zd bytes: ", (bytes_size > 10) ? 10 : bytes_size);
	
	for (i = 0; i < bytes_size && i < 10; i++)
		printf("%02x ", bytes_data[i]);
	
	printf("\n");
}
