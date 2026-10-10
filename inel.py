class Nod:
    def __init__(self, nume):
        self.nume = nume
        self.urmatorul = None

    def transmite(self, mesaj, numar_noduri):
        nod_curent = self
        print(f"{self.nume} trimite mesajul: {mesaj}")

        for _ in range(numar_noduri):
            nod_curent = nod_curent.urmatorul
            print(f"{nod_curent.nume} primeste mesajul: {mesaj}")


def construieste_inel(numar_noduri):
    noduri = [Nod(f"Nodul {index + 1}") for index in range(numar_noduri)]

    for index, nod in enumerate(noduri):
        nod.urmatorul = noduri[(index + 1) % numar_noduri]

    return noduri


def main():
    numar_noduri = 3
    noduri = construieste_inel(numar_noduri)
    mesaj = input("Introdu mesajul: ").strip() or "Salut din inel!"

    print("\nTransmitere circulara:")
    noduri[0].transmite(mesaj, numar_noduri)


if __name__ == "__main__":
    main()
