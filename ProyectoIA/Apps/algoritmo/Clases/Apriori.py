from efficient_apriori import apriori
import json


def Apriori(transactions):
    itemsets, rules = apriori(transactions, min_support=0.1, min_confidence=0.2)
    # print(itemsets)
    # print(rules)

    # Print out every rule with 2 items on the left hand side,
    # 1 item on the right hand side, sorted by lift
    salida = "\n"
    rules_rhs = filter(lambda rule: len(rule.lhs) == 1 and len(rule.rhs) == 1, rules)
    for rule in sorted(rules_rhs, key=lambda rule: rule.lift):
        salida = salida + str(rule) + "\n"
        # print(rule)  # Prints the rule and its confidence, support, lift, ...
    return salida


def leerDatos(ruta):
    with open(ruta) as file:
        datosInput = json.load(file)
    return datosInput


transactions = [['hd', 'b', 'k'],
                ['hd', 'b'],
                ['hd', 'b', 'ch'],
                ['ch', 'ck'],
                ['ch', 'k'],
                ['hd', 'b', 'ch']]
Apriori(transactions)
print(Apriori(transactions))
