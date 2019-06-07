def slices(series, length):
    if length < 1 or length > len(series):
        raise ValueError(f'Value for length: {length}  is not valid')
    return [series[i:i+length] for i in range(0, len(series)-length+1, 1)]
