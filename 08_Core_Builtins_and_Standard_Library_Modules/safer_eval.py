def safer_eval(s):
    code = compile(s, '<user-entered string>', 'eval')
    if code.co_names:
        raise ValueError(f'Names {code.co_names!r} not allowed in expression {s!r}')
    return eval(code)

x = safer_eval("10+35")
y = safer_eval("min(1,2,3)")
