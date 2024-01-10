class Printer:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.spooler = []

    def get_waiting_documents_number(self):
        print(f"There are {len(self.spooler)} waiting documents in the spooler.")


printer = Printer(brand="XEROX", model="9700")

printer.get_waiting_documents_number()
