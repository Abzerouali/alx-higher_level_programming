#include <stdio.h>
#include <Python.h>

/**
*print_python_bytes - Print information about bytes objects in Python.
*
*@p: Python bytes object.
*Return: No return value.
*/
void print_python_bytes(PyObject *p)
{
	char *str;
	long int size, i, limite;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying str: %s\n", str);

	if (size >= 10)
		limite = 10;
	else
		limite = size + 1;

	printf("  first %ld bytes:", limite);

	for (i = 0; i < limite; i++)
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", 256 + str[i]);

	printf("\n");
}

/**
*print_python_list - Print information about Python lists.
*
*@p: Python list object.
*
*Return: No return value.
*/
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
