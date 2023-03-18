import datetime

class ATOM():    
    def __init__(self):
        pass
    
    def get_now(self):
        today = str(datetime.datetime.now())
        today = today.replace(" ", "_")
        today = today.replace(".", "_")
        today = today.replace(":", "_")
        return today
