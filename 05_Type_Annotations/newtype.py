import typing

# ambiguous types for key and value
# employee_department_map: dict[str, str] = {}

EmpId = typing.NewType('EmpId', str)
DeptId = typing.NewType('DeptId', str)
employee_department_map: dict[EmpId, DeptId] = {}


def transfer_employee(empid: EmpId, to_dept: DeptId):
    # update department for employee
    employee_department_map[to_dept] = empid

"""
error: Invalid index type "DeptId" for "Dict[EmpId, DeptId]"; expected type "EmpId"
error: Incompatible types in assignment (expression has type "EmpId", target has type "DeptId")
"""


ZipCode = typing.NewType("ZipCode", str)

