import Frame

class KnowledgeFrames:
    def __init__(self):
        self.data = {}
    
    def __key_not_found(self, key):
        raise KeyError(key)

    def add_entry(self, key, value : Frame):
        self.data[key] = value

    def get_entry(self,key):
        return self.data.get(key, self.__key_not_found)
    
    def delete_entry(self, key):
        if key in self.data:
            del self.data[key]
        else:
            self.__key_not_found()
        
    def list_entries(self):
        return self.data.keys()
    
    def search_entries(self, search_term):
        results = {key: value for key, value in self.data.items() if search_term.lower() in key.lower()}
        return results
    