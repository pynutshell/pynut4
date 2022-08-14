#include <Python.h>
static PyObject*
hello(PyObject* self)
{
    return Py_BuildValue("s", "Hello, Python extensions world!");
}
static char hello_docs[] =
    "hello(): return a popular greeting phrase\n";
static PyMethodDef hello_funcs[] = {
    {"helloworld", (PyCFunction)hello, METH_NOARGS, hello_docs},
    {NULL}
};
static struct PyModuleDef hello_module = {
   PyModuleDef_HEAD_INIT,
   "hello",
   hello_docs,
   -1,
   hello_funcs
};
 
PyMODINIT_FUNC
PyInit_hello(void)
{
   return PyModule_Create(&hello_module);
}
