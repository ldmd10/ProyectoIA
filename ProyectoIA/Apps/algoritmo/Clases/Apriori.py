from efficient_apriori import apriori
import json


def Apriori(transactions, lhs, rhs, soporte, confianza):
    itemsets, rules = apriori(transactions, soporte, confianza)
    # print(itemsets)
    # print(rules)

    # Print out every rule with 2 items on the left hand side,
    # 1 item on the right hand side, sorted by lift
    salida = "\n"
    rules_rhs = filter(lambda rule: len(rule.lhs) == lhs and len(rule.rhs) == rhs, rules)
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
