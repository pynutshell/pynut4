# ||--3.10|| prior to 3.10, specifying alternative types requires
# use of the Union type
from typing import Callable, Union
str_predicate_function: Callable[Union[str, bytes], bool]

# ||--3.9|| prior to 3.9, builtins such as list, tuple, dict, set,
# etc. required types imported from the typing module
from typing import Dict, Tuple, Callable, Union
employee_data: Dict[str, Tuple[int, int, str]]
str_predicate_function: Callable[Union[str, bytes], bool]