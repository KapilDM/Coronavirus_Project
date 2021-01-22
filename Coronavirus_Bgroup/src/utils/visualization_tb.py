def cm_to_inch(value):
    """Changing the size of the graphs from cm to ich"""
    return value/2.54


def funcion_para_añadir_una_barra(string):
    """Adding the double bar to the path"""
    result = string.replace("\\", r"\\")
    print(result)
    return result