def print_store_matrix(matrix):
    column_widths = [
        max(len(str(item)) for item in column) + 2 for column in zip(*matrix)
    ]
    print("\n")
    total_width = sum(column_widths) + len(column_widths) - 1
    border_width = (total_width - len(" STORE ")) // 2
    print("+" + "-" * border_width + " STORE " + "-" * border_width + "+")

    header = "|".join(
        "{:^{width}}".format(column, width=width)
        for column, width in zip(matrix[0], column_widths)
    )
    print(header)

    separator = "+".join("-" * width for width in column_widths)
    print(separator)

    for row in matrix[1:]:
        row_str = "|".join(
            "{:^{width}}".format(str(item), width=width)
            for item, width in zip(row, column_widths)
        )
        print(row_str)

    print("+" + "-" * total_width + "+")
    print("\n")


def create_items_matrix(store):
    matrix = [["Item", "Stock", "Price", "Category", "Id"]]

    for item in store.items.values():
        matrix.append(
            [item.name, item.stock, item.price, item.product_category, item.id]
        )
    return matrix
