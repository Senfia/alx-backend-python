def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''This function retrieves the initial element from a sequence,
       provided that it exists.
    '''
    if lst:
        return lst[0]
    else:
        return None
