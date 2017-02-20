class Busket(object):
    volume = 10

    def __init__(self):
        self.products = []

    def put_product(self, product):
        try:
            if not product.due_date:
                print('Product is rotten')
                return

        except AttributeError:
            print('Product does not have due_date')

            if product.fragile and self.volume - product.volume < 0:
                print('No space left')
                return

        self.products.append(product)
        print('Added to cart')


class Cart(Busket):
    volume = 20


class CashDesk(object):
    def __init__(self, number):
        self.number = number

    def how_much(self, busket):
        total = 0
        for product in busket.products:
            total += product.price
        return total


class AbstractProduct(object):
    def __init__(self, price, volume):
        self.price = price
        self.volume = volume


class Drink(AbstractProduct):
    fragile = True


class Food(AbstractProduct):
    def __init__(self, price, volume, due_date):
        self.price = price
        self.volume = volume
        self.due_date = due_date


b = Busket()
c = Cart()

cd = CashDesk(1)

for i in range(100):
    f = Food(10, 1, True)
    f1 = Food(10, 2, False)

    drink = Drink(100, 2)

    b.put_product(f)
    b.put_product(drink)

    c.put_product(f1)
    c.put_product(drink)

print('busket is', cd.how_much(b))
print('cart is', cd.how_much(c))
