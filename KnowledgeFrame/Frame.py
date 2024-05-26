class Frame:
    
    def __init__(self, frame_name : str):
        self.frame_name = frame_name
        self.slots = {}

    def __slot_name_not_found(self, slot_name):
        raise KeyError(slot_name)
    
    def set_slot(self, slot_name : str, slot_value):
        self.slots[slot_name] = slot_value

    def get_slot(self, slot_name : str):
        return self.slots.get(slot_name, self.__slot_name_not_found)

    def __str__(self):
        return f'{self.frame_name} : {self.slots}'