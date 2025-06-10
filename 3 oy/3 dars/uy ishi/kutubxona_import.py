from kutubxonaa import Kutubxona,Kitob


kutubxona = Kutubxona()

kitob1 = Kitob("Alkimyogar", "Paulo Coelho")
kitob2 = Kitob("O'tkan kunlar", "Abdulla Qodiriy")
kitob3 = Kitob("Mehrobdan chayon", "Pirimqul Qodirov")

kutubxona.qoshish(kitob1)
kutubxona.qoshish(kitob2)
kutubxona.qoshish(kitob3)


print("Kitoblar soni:", len(kutubxona))


print("2-chi indeksdagi kitob:", kutubxona[2])


kutubxona[1] = Kitob("Yangi nom", "Abdulla Qodiriy")
print("Yangilangan kitob:", kutubxona[1])
