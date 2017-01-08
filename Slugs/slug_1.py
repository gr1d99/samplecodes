class KwargsRequired(Exception):
    pass


class StringRequired(Exception):
    pass

BAD_CHARS = "`~!@#$%^&*()_+={}[]:;'<>,./?\\|"


def _clean(value):
    for c in BAD_CHARS:
        if c in value:
            value = value.replace(c, "")
    return value


def slugify(value):
    joiner = "-"
    temp = _clean(value)

    # strip white spaces using strip()
    s_temp = temp.strip()

    # check for spaces in between
    s_1_temp = s_temp.split(" ")

    clean_str = ""
    if len(s_1_temp) > 1:
        for i in range(len(s_1_temp)):
            if i == len(s_1_temp)-1:
                clean_str += s_1_temp[i]
            else:
                clean_str += s_1_temp[i] + joiner
    else:
        return value

    return clean_str


def sample_1(**kwargs):
    result = {}
    if not kwargs:
        raise KwargsRequired(
            """
            You must pass a keyword argument!!
            """)
    for i in range(len(kwargs)):
        for k, v in kwargs.items():
            if not isinstance(v, str):
                raise StringRequired("""
                keyword argument '%s' value is of type %s, expected value of type %s
                """
                                     % (k, type(v), str))
            else:
                result[k] = slugify(v)
        return result
