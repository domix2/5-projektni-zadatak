class Kategorija:
    def __init__(self, naziv, artikli):
        self.__naziv = naziv
        self.__artikli = artikli

    @property
    def naziv(self):
        return self.__naziv

    @naziv.setter
    def naziv(self, naziv):
        self.__naziv = naziv

    @property
    def artikli(self):
        return self.__artikli

    @artikli.setter
    def artikli(self, artikli):
        self.__artikli = artikli

    def ispis(self):
        print(f"{self.__naziv}:")
        for artikl in self.__artikli:
            artikl.ispis()