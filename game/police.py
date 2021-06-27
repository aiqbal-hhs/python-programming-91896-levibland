class Police:
    def __init__(self, _members, _director):
        self.members = _members
        self.director = _director
    
    def addMember(self, _uuid, _name):
        print(f'{_name} has joined the popo.\n')
        self.members.append(_uuid)
    
    def removeMember(self, _uuid):
        self.members.remove(_uuid)
    
    def changeDirector(self, _uuid):
        self.director = _uuid
