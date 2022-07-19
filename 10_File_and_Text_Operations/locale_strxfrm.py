import locale

def locale_sort_inplace(list_of_strings):
    list_of_strings.sort(key=locale.strxfrm)
