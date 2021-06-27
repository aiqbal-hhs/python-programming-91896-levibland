class Bank:
    def __init__(self, _player_balances, _org_balances):
        self.player_balances = _player_balances
        self.org_balances = _org_balances

    def player_deposit(self, _uuid, _amount):
        self.player_balances[_uuid] += _amount
    
    def player_withdraw(self, _uuid, _amount):
        self.player_balances[_uuid] -= _amount

    def org_deposit(self, _org_id, _amount):
        self.org_balances[_org_id] += _amount
    
    def org_withdraw(self, _org_id, _amount):
        self.org_balances[_org_id] -= _amount

    def transfer_balance_player(self, _uuid, _uuid2, _amount):
        if self.player_balances[_uuid] < _amount:
            pass
        else:
            self.player_balances[_uuid] -= _amount
            self.player_balances[_uuid2] += _amount

    def transfer_balance_player_org(self, _uuid, _org_id, _amount):
        if self.player_balances[_uuid] < _amount:
            pass
        else:
            self.player_balances[_uuid] -= _amount
            self.org_balances[_org_id] += _amount
    
    def transfer_balance_org_player(self, _uuid, _org_id, _amount):
        if self.org_balances[_org_id] < _amount:
            pass
        else:
            self.player_balances[_uuid] -= _amount
            self.org_balances[_org_id] += _amount
    
    def transfer_balance_org(self, _org_id, _org_id2, _amount):
        if self.org_balances[_org_id] < _amount:
            pass
        else:
            self.org_balances[_org_id] -= _amount
            self.org_balances[_org_id2] += _amount
