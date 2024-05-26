class Frame:
    def __init__(self, frame_name : str, parent_frame: 'Frame' = None):
        self.frame_name = frame_name
        self.slots = {}
        self.parent_frame = parent_frame

    def __slot_name_not_found(self, slot_name):
        return f'Slot {slot_name} not found'
    
    def set_slot(self, slot_name : str, slot_value):
        # Если есть родитель, то надо проверить сначала в нём
        if self.parent_frame:
            # Сначала проверяем, может уже есть такой слот в родителе
            parent_slot = self.parent_frame.get_slot(slot_name)
            if parent_slot != self.__slot_name_not_found(slot_name):
                # Если есть такой слот - пишем в родителя.
                self.parent_frame.set_slot(slot_name, slot_value)
                return
        # Если нету такого слота в родителе - пишем в себя
        self.slots[slot_name] = slot_value

    def get_slot(self, slot_name : str):
        if slot_name in self.slots:
            return self.slots[slot_name]
        elif self.parent_frame:
            return self.parent_frame.get_slot(slot_name)
        else:
            return self.__slot_name_not_found(slot_name)

    def __str__(self):
        result = f'{self.frame_name} :\n'

        if self.parent_frame:
            for key, value in self.parent_frame.slots.items():
                result += f'\t{key} : {value}\n'
        for key, value in self.slots.items():
            result += f'\t{key} : {value}\n'
        return result