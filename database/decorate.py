def deco_maker_with_arguments(deco_arg1, deco_arg2, deco_arg3):
    def decorator(func):
        def wrapper(func_arg1, func_arg2, func_arg3) :
            "This is the wrapper function"
            print("The wrapper can access all the variables\n"
                  "\t- from the decorator maker: {0} {1} {2}\n"
                  "\t- from the function call: {3} {4} {5}\n"
                  "\tand pass them to the decorated function."
                  .format(deco_arg1, deco_arg2,deco_arg3,
                          func_arg1, func_arg2,func_arg3))
            func_arg4 = 'func_arg4'
            return func(func_arg1, func_arg2,func_arg3, func_arg4)

        return wrapper

    return decorator

pandas = "Pandas"

@deco_maker_with_arguments(pandas, "Numpy","Scikit-learn")
def decorated_func_with_arguments(func_arg1, func_arg2,func_arg3,
                                  func_arg4):
    print("\tThis is the decorated function and it only knows about\n"
          "\tits arguments: {0}" " {1}" " {2}".format(func_arg1,
                                                      func_arg2,
                                                      func_arg3))

decorated_func_with_arguments(pandas, "Science", "Tools")
