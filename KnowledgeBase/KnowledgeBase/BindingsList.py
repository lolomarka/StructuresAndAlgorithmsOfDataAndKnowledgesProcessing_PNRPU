class BindingsList(object):
    def __init__(self):
        super(BindingsList, self).__init__()
        self.bindings_list = []

    def __repr__(self):
        return 'BindingsList({!r})'.format(self.bindings_list)
    
    def __str__(self):
        string = ''
        for binding, associated_fact_rules in self.bindings_list:
            string += f'Bindings for Facts and Rules: {str(binding)}\n'
            string += f'Associated Facts and Rules: [{str.join(', ', (str(f) for f in associated_fact_rules))}]'
        return string

    def __len__(self):
        return len(self.bindings_list)

    def __getitem__(self, key):
        return self.bindings_list[key][0]

    def add_bindings(self, bindings, facts_rules=[]):
        self.bindings_list.append((bindings, facts_rules)) 