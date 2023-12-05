#include <Python.h>

/**
 * print_python_list_info - prints basic info about Python lists
 * @p: list
 */

void print_python_list_info(PyObject *p)
{
	int size, alloc, x;
	PyObject *item;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (x = 0; x < size; x++)
	{
		printf("Element %d: ", x);

		item = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(item)->tp_name);
	}
}
