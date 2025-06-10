class Product:
    def __init__(self, nomi, narxi):
        self.nomi = nomi
        self.narxi = narxi

    def __repr__(self):
        return f"{self.nomi} - {self.narxi} so'm"

    def __eq__(self, other):
        return isinstance(other, Product) and self.nomi == other.nomi and self.narxi == other.narxi


class Savat:
    def __init__(self):
        self._mahsulotlar = []

    def __getitem__(self, index):
        return self._mahsulotlar[index]

    def __setitem__(self, index, value):
        if isinstance(value, Product):
            self._mahsulotlar[index] = value
        else:
            raise ValueError("Faqat Product obyektlarini qo'shish mumkin.")

    def __delitem__(self, index):
        del self._mahsulotlar[index]

    def __len__(self):
        return len(self._mahsulotlar)

    def __contains__(self, product):
        return product in self._mahsulotlar

    def __iter__(self):
        return iter(self._mahsulotlar)

    def __str__(self):
        if not self._mahsulotlar:
            return "Savat bo'sh."
        return "\n".join(str(p) for p in self._mahsulotlar)

    def __bool__(self):
        return bool(self._mahsulotlar)

    def __add__(self, product):
        if isinstance(product, Product):
            self._mahsulotlar.append(product)
            return self
        else:
            raise ValueError("Faqat Product obyektini qo‘shish mumkin.")

    def __call__(self):
        return sum(p.narxi for p in self._mahsulotlar)

    def __eq__(self, other):
        if not isinstance(other, Savat):
            return False
        return sorted(self._mahsulotlar, key=lambda x: x.nomi) == sorted(other._mahsulotlar, key=lambda x: x.nomi)



p1 = Product("Non", 3000)
p2 = Product("Sut", 7000)
p3 = Product("Non", 3000)

print(p1 == p3)
print(repr(p2))


savat = Savat()
savat += p1
savat += p2
print(savat)
print("Umumiy mahsulotlar:", len(savat))
print(p3 in savat)
for mahsulot in savat:
    print("->", mahsulot.nom)

print("1-mahsulot:", savat[0])
savat[1] = Product("Yog'", 15000)
del savat[0]
print("Yangi savat:\n", savat)


if savat:
    print("Savat bo‘sh emas")
print("Jami narx:", savat())

savat2 = Savat()
savat2 += Product("Yog'", 15000)
print("Savatlar tengmi:", savat == savat2)

savat3 = Savat()
print(savat3)

try:
    savat + "oddiy matn"
except ValueError as e:
    print("Xatolik:", e)


