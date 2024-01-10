#include <Python.h>
#include <object.h>
#include <unicodeobject.h>


void print_python_string(PyObject *p)
{
    const char *write = NULL;
    Py_ssize_t len = 0;
    wchar_t *str = NULL;

    printf("[.] string object info\n");
    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    if (PyUnicode_IS_COMPACT_ASCII(p))
        write = "compact ascii";
    else
        write = "compact unicode object";

    str = PyUnicode_AsWideCharString(p, &len);

    printf("  type: %s\n", write);
    printf("  length: %ld\n", len);
    printf("  value: %ls\n", str);
}
