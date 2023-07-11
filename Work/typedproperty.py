# typedproperty.py

def typedproperty(name, expected_type):
    private_name = '_' + name
    @property
    def prop(self):
        return getattr(self, private_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise ValueError(f'Expected {expected_type} for attr: {name}')
        setattr(self, private_name, value)

    return prop

String = lambda x: typedproperty(x, str)
Integer = lambda x: typedproperty(x, int)
Float = lambda x: typedproperty(x, float)
