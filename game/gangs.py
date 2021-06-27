class Gang:
    def __init__(self, _name, _leader, _members, _address):
        self.name = _name
        self.leader = _leader
        self.members = _members
        self.address = _address
    
    def changeName(self, _name):
        print(f'{self.name} has been renamed to {_name}.\n')
        self.name = _name
    
    def changeLeader(self, _leader, _name):
        print(f'{self.name} has elected a new leader, {_name}.\n')
        self.leader = _leader
    
    def addMember(self, _uuid, _name):
        print(f'{_name} has joined {self.name}.\n')
        self.members.append(_uuid)
    
    def removeMember(self, _uuid):
        self.members.remove(_uuid)
                
    def changeAddress(self, _address):
        print(f'{self.name} has changed their safehouse address to {_address}.\n')
        self.address = _address
