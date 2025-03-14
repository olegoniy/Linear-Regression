# basically a separate class to validate users input (cause it is messy otherwise)
class Validator():
    
    def __init__(self):
        pass

    def is_pos_int(self, string:str)->bool:
        try:
            if int(string) <= 0:
                return False
            return True
        except:
            return False
    
    def is_pos_float(self, string:str)->bool:
        try:
            if float(string) <= 0:
                return False
            return True
        except:
            return False
        
    def is_float(self, string:str):
        try:
            float(string)
            return True
        except:
            return False
        
    