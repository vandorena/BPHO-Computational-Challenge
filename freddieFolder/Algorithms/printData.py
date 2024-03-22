def print_table(data: list, dataInColumns=False):
    """
    This procedure takes in a list of lists and prints it as a 2d table
    :param data: is the 2d list
    :param dataInColumns: this will rotate the data before printing, if needed
    :return: None
    """
    # rotates 2d list if dataInColumns is true
    if dataInColumns:
        tempData = []
        for row in range(len(data[0])):
            tempData.append([data[col][row] for col in range(len(data))])
        data = tempData
    # Calculate the maximum width for each column
    col_widths = [max(len(str(item)) for item in col) for col in zip(*data)]

    # Print the table row by row
    for row in data:
        formatted_row = ' | '.join(f"{item:{width}}" for item, width in zip(row, col_widths))
        print(formatted_row)

