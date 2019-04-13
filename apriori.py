def read_transactions():
    with open(input("Enter filename: "), 'r') as input_file:
        baskets = []
        for line in input_file:
            baskets.append(line.rstrip().split(','))
    return baskets


def calculate_support(transactions, catalog, threshold):
    supports = {}
    total = len(transactions)
    times_bought = 0
    for item in catalog:
        for transaction in transactions:
            if item in transaction:
                times_bought += 1
        support = times_bought / total
        if support > threshold:
            supports[item] = support
        times_bought = 0
    return supports

def calclate_confidence(threshold):
    confidence = {}

    return confidence  # dictionary


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
    # calclate_confidence(confidence_threshold)
    calculate_support(transactions,catalog, .5)


main()
