def generate_key_sequence(keyword):
    sorted_chars = sorted([(char, i) for i, char in enumerate(keyword)], key=lambda x: (x[0], x[1]))
    key_sequence = [rank + 1 for _, rank in sorted_chars]
    return key_sequence

def fill_table(text, num_columns):
    num_rows = (len(text) + num_columns - 1) // num_columns
    table = [[''] * num_columns for _ in range(num_rows)]
    for index, char in enumerate(text):
        row, col = divmod(index, num_columns)
        table[row][col] = char
    return table

def print_table(table, keyword, key_sequence):
    header = " ".join(f"{keyword[i]}({key_sequence[i]})" for i in range(len(keyword)))
    print(header)
    print("-" * len(header))
    for row in table:
        print("  ".join(char if char else ' ' for char in row))

def encrypt_transposition_with_table(text, keyword):
    key_sequence = generate_key_sequence(keyword)
    num_columns = len(keyword)
    table = fill_table(text, num_columns)

    print("Таблица до перестановки:")
    print_table(table, keyword, key_sequence)

    sorted_columns = sorted(range(num_columns), key=lambda x: key_sequence[x])
    sorted_table = [[row[col_index] for col_index in sorted_columns] for row in table]

    print("\nТаблица после перестановки:")
    print_table(sorted_table, keyword, [key_sequence[i] for i in sorted_columns])

    encrypted_text = ''.join([''.join(row) for row in zip(*sorted_table) if any(row)])
    
    return encrypted_text

keyword = "ЛУНАТИК"
text = "ТЗКИМАКСБАЛЛ"

encrypted_text = encrypt_transposition_with_table(text, keyword)
print("\nЗашифрованный текст:", encrypted_text)
