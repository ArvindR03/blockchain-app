from transaction import Transaction
import datetime

class Vote(Transaction):
    def __init__(self, voter, candidate):
        super().__init__(sender=voter, recipient=candidate, amount='VOTE', timestamp=datetime.datetime.now())

    def check_valid_vote(self, voter_list: list, candidate_list: list, election_start: datetime.datetime, election_end: datetime.datetime):
        if super().sender not in voter_list:
            return False
        if super().recipient not in candidate_list:
            return False
        if not (election_start <= datetime.datetime.strptime(super().timestamp) <= election_end):
            return False
        return True