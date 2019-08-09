import apriori
transactions = [('elma', 'muz', 'dondurma', 'simit'),
                ('elma', 'muz', 'simit'),
                ('yumurta', 'simit'),
                ('yumurta', 'erik'),
                ('elma', 'muz'),
                ('elma', 'muz', 'yumurta')]
print(apriori.apriori(transactions))