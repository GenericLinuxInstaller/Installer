import npyscreen

class connInfo(npyscreen.Form):

    def afterEditing(self):
        self.parentApp.NEXT_ACTIVE_FORM = 'userman'

    def create(self):
        self.ip        = self.add(npyscreen.TitleText, name='Ip address ')
        self.mask  = self.add(npyscreen.TitleText, name=    'Netmask    ')
        self.gw  = self.add(npyscreen.TitleText, name=      'Gateway    ')


