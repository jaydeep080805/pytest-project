def make_snippet(str):
    string_as_list = list(str.split(" "))
    length_of_string = len(string_as_list)

    if length_of_string > 5:
        return f'{" ".join(string_as_list[:5])}...'
    
    return str