import pyfpgrowth


def fpGrowth(transactions):
    patterns = pyfpgrowth.find_frequent_patterns(transactions, 1)
    rules = pyfpgrowth.generate_association_rules(patterns, 0.2)
    print(patterns)
    print(rules)
    salida = "\nFrecuencias" + "\n" + str(patterns) + "\n" + "Reglas" + "\n" + str(rules)
    return salida
