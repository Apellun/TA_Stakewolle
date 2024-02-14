from fastapi import HTTPException
        
        
class CodeDoesntExistException(HTTPException):
    def __init__(self):
        self.status_code = 400
        self.detail = "Код не найден"
        super().__init__(self.status_code, self.detail)
        

class UserDoesntExistException(HTTPException):
    def __init__(self):
        self.status_code = 400
        self.detail = "Пользователь не найден"
        super().__init__(self.status_code, self.detail)
        

class CodeExistsException(HTTPException):
    def __init__(self):
        self.status_code = 400
        self.detail = "У вас уже есть код"
        super().__init__(self.status_code, self.detail)
        
               
class CodeExpiredException(HTTPException):
    def __init__(self):
        self.status_code = 200
        self.detail = "Срок годности кода истек"
        super().__init__(self.status_code, self.detail)
        
