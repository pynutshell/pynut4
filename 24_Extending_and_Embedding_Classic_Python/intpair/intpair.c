#include "Python.h"
#include "structmember.h"
/* per-instance data structure */
typedef struct {
    PyObject_HEAD
    int first, second;
} intpair;
static int
intpair_init(PyObject *self, PyObject *args, PyObject *kwds)
{
    static char* nams[] = {"first","second",NULL};
    float first_arg, second_arg;
    if(!PyArg_ParseTupleAndKeywords(args, kwds, "ff", nams, &first_arg, &second_arg))
        return -1;
    ((intpair*)self)->first = (int)first_arg;
    ((intpair*)self)->second = (int)second_arg;
    return 0;
}
static void
intpair_dealloc(PyObject *self)
{
    self->ob_type->tp_free(self);
}
static PyObject*
intpair_str(PyObject* self)
{
    return PyUnicode_FromFormat("intpair(%d,%d)",
        ((intpair*)self)->first, ((intpair*)self)->second);
}
static PyMemberDef intpair_members[] = {
    {"first", T_INT, offsetof(intpair, first), 0, "first item" },
    {"second", T_INT, offsetof(intpair, second), 0, "second item" },
    {NULL}
};
static PyTypeObject t_intpair = {
    PyObject_HEAD_INIT(0)                /* tp_head */
    "intpair.intpair",                   /* tp_name */
    sizeof(intpair),                     /* tp_basicsize */
    0,                                   /* tp_itemsize */
    intpair_dealloc,                     /* tp_dealloc */
    0,                                   /* tp_print */
    0,                                   /* tp_getattr */
    0,                                   /* tp_setattr */
    0,                                   /* tp_compare */
    intpair_str,                         /* tp_repr */
    0,                                   /* tp_as_number */
    0,                                   /* tp_as_sequence */
    0,                                   /* tp_as_mapping */
    0,                                   /* tp_hash */
    0,                                   /* tp_call */
    0,                                   /* tp_str */
    PyObject_GenericGetAttr,             /* tp_getattro */
    PyObject_GenericSetAttr,             /* tp_setattro */
    0,                                   /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT,
    "two ints (first,second)",
    0,                                   /* tp_traverse */
    0,                                   /* tp_clear */
    0,                                   /* tp_richcompare */
    0,                                   /* tp_weaklistoffset */
    0,                                   /* tp_iter */
    0,                                   /* tp_iternext */
    0,                                   /* tp_methods */
    intpair_members,                     /* tp_members */
    0,                                   /* tp_getset */
    0,                                   /* tp_base */
    0,                                   /* tp_dict */
    0,                                   /* tp_descr_get */
    0,                                   /* tp_descr_set */
    0,                                   /* tp_dictoffset */
    intpair_init,                        /* tp_init */
    PyType_GenericAlloc,                 /* tp_alloc */
    PyType_GenericNew,                   /* tp_new */
    PyObject_Del,                        /* tp_free */
};
static PyMethodDef no_methods[] = { {NULL} };
static char intpair_docs[] =
    "intpair: data type with int members .first, .second\n";
static struct PyModuleDef intpair_module = {
   PyModuleDef_HEAD_INIT,
   "intpair",
   intpair_docs,
   -1,
   no_methods
};
 
PyMODINIT_FUNC
PyInit_intpair(void)
{
    PyObject* this_module = PyModule_Create(&intpair_module);
    PyType_Ready(&t_intpair);
    PyObject_SetAttrString(this_module, "intpair", (PyObject*)&t_intpair);
    return this_module;
}
