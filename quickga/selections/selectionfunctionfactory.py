class SelectionFunctionFactory:
    def __new__(cls, *args, **kargs):
        obj = object.__new__(cls)
        obj.__init__(*args, **kargs)

        return obj.selection_function

    def selection_function(self, parent_pool, num_offspring):
        raise Exception("Must implement 'selection_function' method")