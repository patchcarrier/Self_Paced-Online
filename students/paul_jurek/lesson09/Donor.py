"""donor class controlling donor behavior"""

from collections import namedtuple
import datetime

Donation = namedtuple('Donation', ['amount', 'date', 'id'])


class Donor:
    """donor giving to organization"""

    def __init__(self, id, firstname=None, lastname=None):
        """args:
            id (int): identification for donor.  Will try to force to int when
                initiated or raise error.
            firstname (str, optional): string representing given name
            lastnamt (str, optional): string representing surname

            _donations (list): contains Donation objects from donor
            _donation_id (int): tracks indentification for donations"""
        try:
            self.id = int(id)
        except ValueError:
            raise ValueError('id input should be interpreted as integer')
        self.firstname = firstname
        self.lastname = lastname
        self._donations = []
        self._donation_id = 1

    def donation_total(self):
        """returns the total amount the donor has donated"""
        return sum([i.amount for i in self._donations])

    def add_donation(self, amount, date=datetime.datetime.utcnow()):
        """adds donation for user"""
        self._donations.append(Donation(amount=amount, date=date, id=self._donation_id))
        self._donation_id += 1

    def donation_count(self):
        """returns count of donations"""
        return len(self._donations)

    @property
    def donations(self):
        """returns donations"""
        return self._donations

    @property
    def fullname(self):
        """returns combine first and last name"""
        return " ".join([self.firstname, self.lastname])

    def summarize_donor(self):
        """provides summary tuple of donor"""
        return (self.id, self.fullname, self.donation_total(), self.donation_count(), self.donation_total()/self.donation_count())