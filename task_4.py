from abc import ABC, abstractmethod


class Phone(ABC):
    price = 1
    weight = 2
    length = 3
    width = 4
    lang = "ru"

    @abstractmethod
    def get_price_with_disc(self):
        pass

    @abstractmethod
    def get_diagonal(self):
        print(pow(((self.weight**2)+(self.length**2)), 0.5))

    @abstractmethod
    def get_lang(self):
        print(self.lang)


class Iphone(Phone):
    price = 1000
    weight = 200
    length = 140
    width = 45


class Android(Phone):
    price = 800
    weight = 210
    length = 145
    width = 40


class Iphone_15(Iphone):
    colour = 'black'

    def __init__(self,serial):
        self.__serial_number = serial

    def get_diagonal(self):
        super().get_diagonal()

    def get_price_with_disc(self):
        sell = self.price * 1.5
        return int(sell)

    def get_lang(self):
        super().get_lang()

    @property
    def serial(self):
        return self.__serial_number

    @serial.setter
    def serial(self, serial):
        self.__serial_number = serial


class Iphone_4(Iphone):
    def get_diagonal(self):
        super().get_diagonal()

    def get_price_with_disc(self):
        sell = self.price * 0.5
        return int(sell)

    def get_lang(self):
        super().get_lang()


a = Iphone_15('123abc')
b = Iphone_4()
print(f'Серийный номер: {a.serial}')
a.serial = 'qweqwe'
print(f'Новый серийный номер: {a.serial}')
print(f'цена iphone 15: {a.get_price_with_disc()}')
print(f'цена iphone 4: {b.get_price_with_disc()}')




