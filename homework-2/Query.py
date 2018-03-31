keys = []
def select(*field_name: str):
    """ This function accepts field names
    and puts them in the list
    of global variable 'keys'.

    :param field_name: Names to put in the list.
    :type field_name: Str.
    :returns: None.
    """
    global keys
    keys = [*field_name]

dict_filter = {}
def field_filter(field_name : str, collection: list):
    """ This function accepts field name
    and a list of values from this field
    and puts them in dictionary of
    global variable 'dict_filter'.

    :param field_name: Name of the required field.
    :type field_name: Str.
    :param collection: Required values of the field_name.
    :type collection: List.
    :returns: None.
    """
    global dict_filter
    dict_filter = {field_name: collection}

def query(collection: list, select, *field_filter):
    """ This function chooses the selected fields,
    filters them and returns only selected fields
    of the elements which fit filter's criteria.

    :param collection: Data to sort and filter.
    :type collection: List.
    :param select: Functions that selects fields.
    :type select: Function.
    :param field_filter: Function that filters data.
    :type: field_filter: Function.
    :returns: List of selected and filtered elements of the data.
    """
    # Copying the data, but with
    # selected field names only.
    selected_list = []
    for i in collection:
        selected = {}
        for key in keys:
            selected[key] = i[key]
        selected_list.append(selected)
    # Filtering copied list
    filtered_list = []
    for j in selected_list:
        for value in list(dict_filter.values())[0]:
            filtered = {}
            if j[list(dict_filter.keys())[0]] == value:
                filtered_list.append(i)
    return filtered_list
