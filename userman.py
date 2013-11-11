import npyscreen

class userInfo(npyscreen.Form):
    def afterEditing(self):
        self.parentApp.NEXT_ACTIVE_FORM = None

    def create(self):
        self.root_pass = self.add(npyscreen.TitlePassword, name='Root password')
        self.root_pass_again = self.add(npyscreen.TitlePassword, name='Root password')


