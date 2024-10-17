# This looks better https://stackoverflow.com/questions/19232373/exceptions-for-the-whole-class
import functools
def err_handler( e,outer,out):
    print("err_handlerException", type(e).__name__, "in", str(e))
    print (str(e))
    out=100
    outer=200
    return out,outer
def no_err_handler(out,outer):
    print ("no_err_handler:",out)
    outer=300
    return out,outer

def handle_err(handler, *exceptions):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_output=None
            try:
                e = None
                func_output= func(*args, **kwargs)
                print("inpargs--->",args[2])
                o1,o2= no_err_handler(func_output,args[2])
                return o1,o2
            except BaseException as e:
                o1,o2= err_handler( e,args[2],func_output)
                return o1, o2
            finally:
             pass
        return wrapper
    return decorator

def outer_div(x1,y1):
    outerinp=None
    z=None
    @handle_err((no_err_handler,err_handler), TypeError, ValueError)
    def div(x, y,outerinp):
        print("start inner_div function inside div()")
        z=x/y
        print("end inner_div function inside div()")
        print("outerinp after running handle_with:", outerinp)
        return z
    div_out,outerinp=div(x1,y1,outerinp)
    print("********outerinp***",outerinp)
    print("********add_out ( z) ***", div_out)
    return div_out,outerinp
#======================================================================================================
# Testing it
zout,outer_output=outer_div(3,2)
print("End calling the test zout_inner=", zout , "outer_output=", outer_output)
#=========================================================================================================
#  https://www.datacamp.com/tutorial/decorators-python try this one
# from functools import wraps
# def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
#     def decorator(func):
#         def wrapper(function_arg1, function_arg2, function_arg3) :
#             "This is the wrapper function"
#             print("The wrapper can access all the variables\n"
#                   "\t- from the decorator maker: {0} {1} {2}\n"
#                   "\t- from the function call: {3} {4} {5}\n"
#                   "and pass them to the decorated function"
#                   .format(decorator_arg1, decorator_arg2,decorator_arg3,
#                           function_arg1, function_arg2,function_arg3))
#             return func(function_arg1, function_arg2,function_arg3)
#
#         return wrapper
#
#     return decorator
#
# pandas = "Pandas"
# @decorator_maker_with_arguments(pandas, "Numpy","Scikit-learn")
# def decorated_function_with_arguments(function_arg1, function_arg2,function_arg3):
#     print("This is the decorated function and it only knows about its arguments: {0}"
#            " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))
#
# @decorator_maker_with_arguments("d1", "d2","d3")
# def decorated_function_with_arguments2(function_arg1, function_arg2,function_arg3):
#     print("This is the decorated function and it only knows about its arguments: {0}"
#            " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))
#
# decorated_function_with_arguments(pandas, "Science", "Tools")
# print("callinmg #2")
# decorated_function_with_arguments2("f1","f2","f3")
# new https://stackoverflow.com/questions/129144/generic-exception-handling-in-python-the-right-way