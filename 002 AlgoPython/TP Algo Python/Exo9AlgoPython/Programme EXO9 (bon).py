import os.path

def get_operator(number):
    prefixes = ['77', '78', '76', '70', '75']
    for prefix in prefixes:
        if number.startswith(prefix) and len(number) == 9:
            return True
    return False

def load_data(filename):
    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            data = file.readlines()
        operators = data[0].strip().split(',')
        matrix = {}
        for operator in operators:
            matrix[operator] = []
        for line in data[1:]:
            customer = line.strip().split(',')
            operator = get_operator(customer[2])
            if operator:
                matrix[operator].append(customer)
        return operators, matrix
    return [], {}

def save_data(filename, operators, matrix):
    with open(filename, 'w') as file:
        file.write(','.join(operators) + '\n')
        for operator in operators:
            for customer in matrix[operator]:
                file.write(','.join(customer) + '\n')

def display_customers(matrix, operator=None):
    if operator:
        customers = matrix[operator]
        for customer in customers:
            print('Nom:', customer[0], '\t', 'Téléphone:', customer[2])
    else:
        for operator in matrix:
            customers = matrix[operator]
            print('Opérateur:', operator)
            for customer in customers:
                print('\tNom:', customer[0], '\t', 'Téléphone:', customer[2])

def display_phone_number(matrix, name):
    for operator in matrix:
        customers = matrix[operator]
        for customer in customers:
            if customer[0] == name:
                print('Téléphone:', customer[2])
                return
    print('Client non trouvé.')

def add_or_update_phone(matrix, name, number):
    operator = get_operator(number)
    if operator:
        for i, customer in enumerate(matrix[operator]):
            if customer[0] == name:
                matrix[operator][i][2] = number
                return
        matrix[operator].append([name, '', number])
    else:
        print('Numéro invalide.')

operators, matrix = load_data('phone_book.txt')
if not operators:
    operators = input('Entrez une liste d\'opérateurs séparés par une virgule: ').strip().split(',')
    matrix = {operator: [] for operator in operators}

while True:
    print('1. Afficher les clients par opérateur')
    print('2. Afficher le numéro de téléphone')
    print('3. Ajouter ou modifier le numéro d\'un client')
    print('4. Quitter')
    choice = input('Faites votre choix: ')
    if choice == '1':
        display_customers(matrix)
    elif choice == '2':
        name = input('Entrez le nom d\'un client: ')
        display_phone_number(matrix, name)
    elif choice == '3':
        name = input('Entrez le nom d\'un client: ')
        number = input('Entrez un numéro de téléphone: ')
        add_or_update_phone(matrix, name, number)
    elif choice == '4':
        save_data('phone_book.txt', operators, matrix)
        break
    else:
        print('Choix invalide.')




