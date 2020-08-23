from os import path

store_data = "store.txt"
order_data = "order.txt"

if path.exists(store_data) and path.exists(order_data):
    print("File Found!")
    store_file = open(store_data, "r")
    order_file = open(order_data, "r")
    store_split = store_file.read().splitlines()
    order_split = order_file.read().splitlines()

    def store(n, q):
        for line in store_split:
            store_list = line.split(" | ")
            if n == store_list[0]:
                price = int(store_list[1])
                summ = q * price

                return f"{n:20}|{q:^4}|{store_list[1]:^5}|{summ:4} "
    summ = []
    count = 0
    for line in order_split:
        order_list = line.split(" | ")
        name = order_list[0]
        qtty = int(order_list[1])
        s = store(name, qtty)
        s1 = s.split("|")
        s2 = int(s1[3])
        summ.append(s2)
        sumar = sum(summ)
        print(s)
        count += 1
        if count == len(order_split):
            print(f"TOTAL: {sumar}")

else:
    print("File NOT Found")

