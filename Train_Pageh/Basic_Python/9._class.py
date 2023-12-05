import runpy


class BangunRuangClass:
    def luasPersegiPanjang():
        panjang = 20
        lebar = 10
        luas = panjang * lebar
        return luas
    def check():
        pageh_ganteng = False
        if pageh_ganteng is not True:
            print("Pageh Ganteng")
        else:
            print("Pageh tidak ganteng")


runpy(BangunRuangClass.check())
