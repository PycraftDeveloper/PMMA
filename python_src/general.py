from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

def swizzle(in_format, data, out_format, handle_alpha=False):
    if in_format == out_format:
        return data
    elif len(data) != len(in_format):
        raise AttributeError("Data length is not compatible")
    else:
        out_data = []
        for character in out_format:
            if not character in in_format:
                if handle_alpha and character.lower() == "a":
                    out_data.append(Constants.ALPHA)
                else:
                    out_data.append(0)
            else:
                out_data.append(data[in_format.index(character)])
        return out_data

def can_swizzle(in_format, data, out_format):
    if in_format == out_format:
        return True
    elif len(data) != len(in_format):
        return False
    return True