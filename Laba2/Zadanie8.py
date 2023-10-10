class Stude:
    name = 'Voterman'
    surname = 'Jerk'

    def initials(self):
        return self.case_up(self.name[0], self.surname[0])

    def case_up(self, stri1, stri2):
        return stri1.upper() + ' ' + stri2.upper()


stude = Stude()

print(stude.initials())