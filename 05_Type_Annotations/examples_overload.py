import typing

@typing.overload
def fn(*, key: str, value: int):
    ...


@typing.overload
def fn(*, strict: bool):
    ...


def fn(**kwargs):
    # implementation goes here, including handling of differing
    # named arguments
    pass


# valid calls
fn(key='abc', value=100)
fn(strict=True)

# invalid calls
fn(1)
fn('abc')
fn('abc', 100)
fn(key='abc')
fn(True)
fn(strict=True, value=100)
