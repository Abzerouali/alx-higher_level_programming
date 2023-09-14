#include "/usr/include/python3.4/Python.h"
#include <stdio.h>
/**
*print_hexn - print hexn.
*@str: pointer
*@n : int
*Return: No return value.
*/
void print_hexn(const char *str, int n)
{
	int count = 0;

	for (; count < n - 1; ++count)
		printf("%02x ", (unsigned char) str[count]);

	printf("%02x", str[count]);
}
/**
*print_python_bytes - Print information about bytes objects in Python.
*
*@p: Python bytes object.
*Return: No return value.
*/
void print_python_bytes(PyObject *p)
{
	PyBytesObject *clone = (PyBytesObject *) p;
	int count_bytes, clone_size = 0;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(clone))
	{
		clone_size = PyBytes_Size(p);
		count_bytes = clone_size + 1;

		if (count_bytes >= 10)
			count_bytes = 10;

		printf("  size: %d\n", clone_size);
		printf("  trying string: %s\n", clone->ob_sval);
		printf("  first %d bytes: ", count_bytes);
		print_hexn(clone->ob_sval, count_bytes);
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}
/**
*print_python_list - Print information about Python lists.
*@p: Python list object.
*
*Return: No return value.
*/
void print_python_list(PyObject *p)
{
	int i = 0, len = 0;
	PyObject *item;
	PyListObject *clone = (PyListObject *) p;

	printf("[*] Python list info\n");
	len = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", (int) clone->allocated);

	for (; i < len; ++i)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %d: %s\n", i, item->ob_type->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
