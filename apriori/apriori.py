def _get_all_items(transactions):
    lookup = {}
    for itemler in transactions:
        for i in itemler:
            if (i in lookup):
                lookup[i] += 1
            else:
                lookup[i] = 1
    return lookup


def _eliminate_by_support_value(lookup, size_of_transactions, min_support):
    eliminated_dictionary = {}
    for k, v in lookup.items():
        lookup[k] = v / size_of_transactions
        if lookup[k] > min_support:
            eliminated_dictionary[k] = lookup[k]
    return eliminated_dictionary


def _compare_tuple_lists(transactions, tuple_list):
    new_lookup = {}
    for item in tuple_list:
        for t in transactions:
            count = 0
            for element in item:
                if element in t:
                    count += 1
            if count == len(item):
                if item not in new_lookup:
                    new_lookup[item] = 0
                new_lookup[item] += 1
    return new_lookup


def _generate_tuples(itemset):
    tuples = []
    liste = list(itemset.keys())
    for i, eleman in enumerate(liste):
        esas_tuple = tuple([eleman])
        for j in range(i + 1, len(liste)):
            gecici_tuple = tuple([list(itemset.keys())[j]])
            son_tuple = tuple(set(esas_tuple + gecici_tuple))
            if type(son_tuple[0]) == type("string"):
                tuples.append(son_tuple)
            else:
                tuples.append(tuple(set(list(son_tuple[0] + son_tuple[1]))))
    return list(set(tuples))


def apriori(transactions, min_support=0.3):
    lookup = _get_all_items(transactions)
    freq_itemsets = []
    freq_itemsets.append(_eliminate_by_support_value(lookup, len(transactions), min_support))

    two_element_tuples = _generate_tuples(freq_itemsets[0])
    new_lookup = _compare_tuple_lists(transactions, two_element_tuples)
    leveltwo = _eliminate_by_support_value(new_lookup, len(transactions), min_support)
    freq_itemsets.append(leveltwo)

    three_element_tuples = _generate_tuples(freq_itemsets[1])
    last_lookup = {}
    last_lookup = _compare_tuple_lists(transactions, three_element_tuples)
    levelthree = _eliminate_by_support_value(last_lookup, len(transactions), min_support)
    freq_itemsets.append(levelthree)

    return (freq_itemsets)