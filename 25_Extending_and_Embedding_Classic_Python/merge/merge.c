#include <Python.h>
 
static PyObject*
merge(PyObject* self, PyObject* args, PyObject* kwds)
{
    static char* argnames[] = {"x","y","override",NULL};
    PyObject *x, *y;
    int override = 0;
    if(!PyArg_ParseTupleAndKeywords(args, kwds, "O!O|i", argnames,
        &PyDict_Type, &x, &y, &override))
            return NULL;
    if(-1 == PyDict_Merge(x, y, override)) {
        if(!PyErr_ExceptionMatches(PyExc_AttributeError))
            return NULL;
        PyErr_Clear();
        if(-1 == PyDict_MergeFromSeq2(x, y, override))
            return NULL;
    }
    return Py_BuildValue("");
}
static char merge_docs[] = "\
merge(x,y,override=False): merge into dict x the items of dict y (or\n\
  the pairs that are the items of y, if y is a sequence), with\n\
  optional override. Alters dict x directly, returns None.\n\
";
static PyObject*
mergenew(PyObject* self, PyObject* args, PyObject* kwds)
{
    static char* argnames[] = {"x","y","override",NULL};
    PyObject *x, *y, *result;
    int override = 0;
    if(!PyArg_ParseTupleAndKeywords(args, kwds, "O!O|i", argnames,
        &PyDict_Type, &x, &y, &override))
            return NULL;
    result = PyObject_CallMethod(x, "copy", "");
    if(! result)
        return NULL;
    if(-1 == PyDict_Merge(result, y, override)) {
        if(!PyErr_ExceptionMatches(PyExc_AttributeError))
            return NULL;
        PyErr_Clear();
        if(-1 == PyDict_MergeFromSeq2(result, y, override))
            return NULL;
    }
    return result;
}
static char mergenew_docs[] = "\
mergenew(x,y,override=False): merge into dict x the items of dict y\n\
  (or the pairs that are the items of y, if y is a sequence), with\n\
  optional override. Does NOT alter x, but rather returns the\n\
  modified copy as the function's result.\n\
";
static PyMethodDef merge_funcs[] = {
    {"merge", (PyCFunction)merge, METH_VARARGS | METH_KEYWORDS, merge_docs},
    {"mergenew", (PyCFunction)mergenew, METH_VARARGS | METH_KEYWORDS, mergenew_docs},
    {NULL}
};
static char merge_module_docs[] = "Example extension module";
static struct PyModuleDef merge_module = {
   PyModuleDef_HEAD_INIT,
   "merge",
   merge_module_docs,
   -1,
   merge_funcs
};
 
PyMODINIT_FUNC
PyInit_merge(void)
{
 
    return PyModule_Create(&merge_module);
}
