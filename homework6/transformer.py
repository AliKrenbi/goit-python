def normalize(bad_string: str):
    good_string = bad_string.translate()
    return good_string


def normalize_filename(filename: str):
    ext = filename.split(".")[-1]
    new_filename = ".".join(filename.split(".")[-1])
    normalized_filename = normalize(new_filename)
    return normalized_filename + "." + ext