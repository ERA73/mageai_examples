import sys
import math

# decorators
def output_memory(function):
    """Calculate the memory size of the incomming fuction output
    
    args:
        function: incomming function
    Return: overwrited function
    """

    def overwrited(*args, **kwargs):
        result = function(*args, **kwargs)
        size_bytes = __get_total_size(result)
        scale_name, scale_value = __get_size_scale(size_bytes)
        scaled_size = size_bytes / scale_value
        print(f"Output memory size: '{scaled_size:.2f} {scale_name}")
        return result
    return overwrited

# private functions
def __get_total_size(obj):
    if isinstance(obj, dict):
        if obj:
            total_size = sum(sys.getsizeof(k) for k in obj.keys())
            total_size += sum(__get_total_size(v) for v in obj.values())
        else:
            return sys.getsizeof(obj)
    elif isinstance(obj, (list, tuple, set, frozenset)):
        if obj:
            total_size = sum(__get_total_size(i) for i in obj)
        else:
            return sys.getsizeof(obj)
    else:
        total_size = sys.getsizeof(obj)
    return total_size

def __get_size_scale(value:int):
    """get_size_scale
    
    Args:
        value: (int) number for calculate the scale of itself
    Return: 
        scale_name, scale_value
    """

    exponent = math.floor(math.log10(abs(value)))
    index_scale = exponent // 3
    scales = [["Bytes",1], ["KB",1024], ["MB",1024**2], ["GB",1024**3], ["TB",1024**4]]
    if index_scale < len(scales):
        return scales[index_scale]
    else:
        return scales[-1]
    