import random


def main():
    card = int(input("enter the numebr of cards: "))
    pick_list = deal_cards(card)
    print(pick_list)


def deal_cards(card):
    count = 0
    list_num = []
    while count < card:
        i = random.randrange(0, 52)
        list_num.append(i)
        count += 1
    # print(list_num, count)
    return list_num


main()