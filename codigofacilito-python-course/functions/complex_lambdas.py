whitout_parameters = lambda : True
with_values = lambda val1, val2=10, val3=10 : val1 + val2 + val3
with_asterisk = lambda *args : args[0]
with_double_asteriks = lambda **kwargs : kwargs[0]
with_asterisks = lambda *args, **kwargs : kwargs.get('key', False)