class ATMError(Exception):
    def __init__(self, name, message, detail=None):
        super().__init__(message)
        self.name = name
        self.detail = detail
        
    def __repr__(self):
        line = f"{self.name}"
        if self.detail:
            line += f" - {self.detail}"
        return line