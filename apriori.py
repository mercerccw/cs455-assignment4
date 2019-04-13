def read_transactions():
    with open(input("Enter filename: "), 'r') as input_file:
        baskets = []
        for line in input_file:
            baskets.append(line.rstrip().split(','))
    return baskets


def calculate_support(transactions, catalog, threshold):
    supports = {}
    supports_with_threshold = {}
    total = len(transactions)
    times_bought = 0
    for item in catalog:
        for transaction in transactions:
            if item in transaction:
                times_bought += 1
        support = times_bought / total
        if support > threshold:
            supports_with_threshold[item] = support
        supports[item] = support
        times_bought = 0
    return supports, supports_with_threshold


def get_occurrences(transactions, catalog, threshold):
    edited_catalog = catalog[1:]
    times_bought = 0
    times_bought_together = 0
    one_products_occurrences = {}
    two_products_occurrences = {}

    for i in range(len(catalog)):
        for transaction in transactions:
            if catalog[i] in transaction:
                times_bought += 1
                for j in range(len(edited_catalog)):
                    if len(edited_catalog) != 0:
                        for subtransaction in transactions:
                            if catalog[i] in subtransaction:
                                if edited_catalog[j] in subtransaction:
                                    times_bought_together += 1
                                    two_products_occurrences[
                                        catalog[i] + '-and-' + edited_catalog[j]] = times_bought_together
                        times_bought_together = 0
        edited_catalog = edited_catalog[1:]
        one_products_occurrences[catalog[i]] = times_bought
        times_bought = 0

    confidences, confidences_with_threshold = calculate_confidence(one_products_occurrences, two_products_occurrences,
                                                                   threshold)
    return confidences, confidences_with_threshold


def calculate_confidence(one_products_occurrences, two_products_occurrences, threshold):
    confidences = {}
    confidences_with_threshold = {}

    for item in one_products_occurrences:
        for two_items in two_products_occurrences:
            if item in two_items:
                confidence = two_products_occurrences.get(two_items) / one_products_occurrences.get(item)
                if confidence > threshold:
                    print(str(two_items) + " : " + "If " + str(item) + " is purchased first " + " = " + str(
                        confidence * 100) + "%")

    return confidences, confidences_with_threshold


def get_all_items(transactions):
    catalog = []
    for transaction in transactions:
        for item in transaction:
            item = item.strip()
            if item not in catalog:
                catalog.append(item)
    return catalog


def main():
    transactions = read_transactions()
    catalog = get_all_items(transactions)
    support_threshold = float(input("Enter support threshold: "))
    confidence_threshold = float(input("Enter confidence threshold: "))
    print('-' * 20 + "\n Rules Discovered: \n")
    calculate_support(transactions, catalog, support_threshold)
    get_occurrences(transactions, catalog, confidence_threshold)
    print('-' * 20)


main()
