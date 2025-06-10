class Kitob:
    def __init__(self, sarlavha, muallif):
        self.sarlavha = sarlavha
        self.muallif = muallif

    def __repr__(self):
        return f"{self.sarlavha} - {self.muallif}"


class Kutubxona:
    def __init__(self):
        self._kitoblar = []

    def __getitem__(self, index):
        return self._kitoblar[index]

    def __setitem__(self, index, kitob):
        if isinstance(kitob, Kitob):
            self._kitoblar[index] = kitob
        else:
            raise ValueError("Faqat Kitob obyektlarini qo'shish mumkin.")

    def __delitem__(self, index):
        del self._kitoblar[index]

    def __len__(self):
        return len(self._kitoblar)

    def __contains__(self, sarlavha):
        return any(k.sarlavha == sarlavha for k in self._kitoblar)

    def __iter__(self):
        return iter(self._kitoblar)

    def qoshish(self, kitob):
        if isinstance(kitob, Kitob):
            self._kitoblar.append(kitob)
        else:
            raise ValueError("Faqat Kitob obyektlarini qo'shish mumkin.")
