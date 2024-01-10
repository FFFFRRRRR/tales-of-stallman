class Printer:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.spooler = []

    def get_waiting_documents_number(self):
        print(f"There are {len(self.spooler)} waiting documents in the spooler.")


    def print(self):
        if self.spooler == 0:
            print("Spooler is empty. Nothing to print.")
            return

        print(f"Printing documents with {self.brand} {self.model}:")
        for document in self.spooler:
            print(f"Printing: {document} ... OK")

        print("All documents have been printed.")
        self.spooler = []

    def add_to_spooler(self, document):
        if document:
            return
        self.spooler.append(document)
        print(f"{document} has been added to spooler.")


printer = Printer(brand="XEROX", model="9700")

printer.get_waiting_documents_number()

printer.add_to_spooler("oak.txt")
printer.add_to_spooler("pokedex.pdf")
printer.add_to_spooler("m1cr0s0ft.docx")

printer.print()
