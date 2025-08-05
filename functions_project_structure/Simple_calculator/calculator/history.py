class History:
    def __init__(self):
        self._records = []

    def add_record(self, operation_str):
        self._records.append(operation_str)

    def show(self):
        if not self._records:
            print("No history yet.")
        else:
            print("\n--- Calculation History ---")
            for record in self._records:
                print(f"- {record}")