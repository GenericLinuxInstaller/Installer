import npyscreen
import includes
import networking
import userman

class Installer(npyscreen.NPSAppManaged):
    def onStart(self):
        # Welcome message
        npyscreen.notify_wait(includes.welcome_message, title="Welcome", form_color='STANDOUT', wrap=True, wide=True)

        # Networking 
        self.addForm('MAIN', networking.connInfo, name='Linux Generic Installer - Networking')
        
        # User management 
        self.addForm('userman', userman.userInfo, name='Linux Generic Installer - User Management')
        
        # Image detection/selection
        
        # Partitioning  
        
        # Bootloader installation 



Installer().run()
