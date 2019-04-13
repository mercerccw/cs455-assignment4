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


def calculate_confidence(transactions, catalog, threshold):
    confidences = []
    confidences_with_threshold = []
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
                                        catalog[i] + '-to-' + edited_catalog[j]] = times_bought_together
                        times_bought_together = 0
        edited_catalog = edited_catalog[1:]
        one_products_occurrences[catalog[i]] = times_bought
        times_bought = 0

    return one_products_occurrences, two_products_occurrences


def calculate_lift():
    pass


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
    # support_threshold = float(input("Enter support threshold: "))
    # confidence_threshold = float(input("Enter confidence threshold: "))
    # calculate_support(support_threshold)
    # calculate_confidence(confidence_threshold)
    support, supports_with_threshold = calculate_support(transactions, catalog, .5)
    print(support)
    print(supports_with_threshold)
    one, two = calculate_confidence(transactions, catalog, .5)

    print(one)
    print(two)


main()
