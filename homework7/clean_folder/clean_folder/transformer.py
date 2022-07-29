CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

TRANS = {}
def normalize(bad_string: str):
    good_string = bad_string.translate(TRANS)
    return good_string


def normalize_filename(filename: str):
    ext = filename.split(".")[-1]
    new_filename = ".".join(filename.split(".")[:-1])
    normalized_filename = normalize(new_filename)
    return normalized_filename + "." + ext