from pmma.src.registry import Registry
from pmma.src.constants import Constants

def swizzle(in_format, data, out_format):
    if in_format == out_format:
        return data
    if len(data) != len(in_format):
        raise AttributeError("Data length is not compatible")
    if "".join(sorted(in_format)) in "".join(sorted(out_format)):
        out_data = []
        for character in out_format:
            if not character in in_format:
                out_data.append(0)
            else:
                out_data.append(data[in_format.index(character)])
        return out_data

    else:
        raise AttributeError("Formats are not compatible")