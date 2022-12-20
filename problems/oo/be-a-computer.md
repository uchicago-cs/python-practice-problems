# Be-a-Computer: Classes and Objects

In the following exercises, you will be shown a piece of code, and will have to figure out what it does (without running it yourself in the Python interpreter)

## Exercise #1

Given the following class definition:

    class Mystery:
        def __init__(self, v0, v1):
            self._v0 = v0
            self._v1 = v1

        def get_a(self):
            return self._v0+1

        def get_b(self):
            return self._v1*2

        def get_c(self):
            return self.get_a() + self.get_b()

        def do_d(self, val):
            self._v0, self._v1 = val

        def __str__(self):
            return str((self.get_a(), self.get_b(), self.get_c()))

What is the output of the following code?

    m0 = Mystery(1, 2)
    m0.do_d((m0.get_a(), m0.get_c()))
    print(m0)

    m1 = Mystery(3, 4)
    m1.do_d((m0.get_a(), m1.get_b()))
    print(m1)

## Exercise #2

This exercise uses the following constants and data:

    (DATE, TICKER, OPEN, CLOSE) = (0, 1, 2, 3)

    stocks = [['Date', 'Ticker Symbol', 'Open', 'Close'],
            ['2010-11-09', 'AMD', '8.22', '7.91'],
            ['2010-11-09', 'GOOG', '630.00', '624.82'],
            ['2010-11-09', 'QQQ', '53.95', '54.26'],
            ['2010-11-10', 'AMD', '8.22', '8.72'],
            ['2010-11-10', 'BSB', '620.00', '630.40'],
            ['2010-11-10', 'GOOG', '630.00', '630.40'],
            ['2010-11-10', 'QQQ', '53.95', '53.45'],
            ['2010-11-11', 'AMD', '8.22', '8.40'],
            ['2010-11-11', 'GOOG', '630.00', '634.82'],
            ['2010-11-11', 'QQQ', '53.95', '53.45']]

What is the output of the following code?

    class Stock_Info(object):
        def __init__(self, date, ticker, opening_price, closing_price):
            self.date = date
            self.ticker = ticker
            self.opening_price = opening_price
            self.__closing_price = closing_price

        def get_closing_price(self):
            return self.__closing_price

        def set_closing_price(self, correct_value):
            self.__closing_price = correct_value

        def __repr__(self):
            return "|".join([self.date, self.ticker, 
                            self.opening_price, self.__closing_price])


    def create_dict(data):
        rv = {}
        for row in data:
            tkr = row[TICKER]
            s = Stock_Info(row[DATE], tkr, row[OPEN], row[CLOSE])
            if tkr not in rv:
                rv[tkr] = []
            rv[tkr].append(s)

        return rv
            
    def mystery(d, list0):
        for (x, y, z) in list0:
            for a in d[x]:
                if a.date == y:
                    a.set_closing_price(z)
                    break


    d = create_dict(stocks)
    entries = [["GOOG", '2010-11-09', '625.00'], 
               ['GOOG', '2010-11-10', '634.82']]
    mystery(d, entries)
    for s in d["GOOG"]:
        print(s)