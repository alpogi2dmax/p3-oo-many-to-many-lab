class Author:

    all = []

    def __init__(self, name):
        self.name = name
        self._contracts = []
        type(self).all.append(self)

    def contracts(self):
        return self._contracts.copy()
    
    def books(self):
        return list({contract.book for contract in self._contracts})
    
    def total_royalties(self):
        return sum(list({contract.royalties for contract in self._contracts}))
    

    def sign_contract(self, book, date, royalties):
        if isinstance(book, Book):
            contract = Contract(self, book, date, royalties)
            self._contracts.append(contract)
            book.add_contract(contract)
            return contract
        else:
            raise TypeError('book must be an instance of Book')

class Book:

    all = []

    def __init__(self, title):
        self.title = title
        self._contracts = []
        type(self).all.append(self)

    def contracts(self):
        return self._contracts.copy()
    
    def authors(self):
        return list({contract.author for contract in self._contracts})

    def add_contract(self, contract):
        if isinstance(contract, Contract):
            self._contracts.append(contract)
        else:
            raise TypeError('contract must be an instance of Contract')
      
class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if isinstance(book, Book) and isinstance(author, Author) and isinstance(date, str) and isinstance(royalties, int):
            self.author = author
            self.book = book
            self.date = date
            self.royalties = royalties
            type(self).all.append(self)
            author._contracts.append(self)
            book.add_contract(self)
        else:
            raise TypeError('Invalid types for author and/or book')
    
    @classmethod
    def contracts_by_date(cls, date):
        return list({contract for contract in cls.all if contract.date == date})