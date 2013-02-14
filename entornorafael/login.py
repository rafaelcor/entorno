import gtk
import os
import time
import sys
root_window = gtk.gdk.get_default_root_window()
screenwidth, screenheight = root_window.get_size()
class Base:
	def aboutinfo(self,widget):
		dialog = gtk.MessageDialog(None,
					gtk.DIALOG_MODAL,
                    type=gtk.MESSAGE_INFO,
                    buttons=gtk.BUTTONS_OK)
		dialog.set_markup("")
		dialog.run()
		dialog.destroy()
	
	
	
	
	def getlogin(self, widget, entry1, entry2):
		self.user = self.entry1.get_text()
		#print "user: %s"%self.user	
		self.password = self.entry2.get_text()
		#print "password: %s"%self.password
		for root, dirs, files in os.walk("./usuarios"):
			if self.user in dirs:
				for root, dirs, files in os.walk("./usuarios/%s"%self.user+"/"+"password") :
					if self.password in files:
						os.system("python entorno.py")
						sys.exit()
					
					
			else:
				dialog = gtk.MessageDialog(None,
                               gtk.DIALOG_MODAL,
                               type=gtk.MESSAGE_ERROR,
                               buttons=gtk.BUTTONS_OK)
				dialog.set_markup("This user or password or both aren't exits")
				dialog.run()
				dialog.destroy()
				
	
	def rebootf(self,widget):
		print "en construccion"
	
	
	def __init__(self):
		self.window = gtk.Window()
		self.window.set_resizable(False)
		self.window.set_size_request(gtk.gdk.screen_width(), gtk.gdk.screen_height())
		self.table = gtk.Table(2, 3, True)
		self.window.add(self.table)
		self.label1 = gtk.Label("User")
		self.label2 = gtk.Label("Password")
		self.entry1 = gtk.Entry()
		self.entry2 = gtk.Entry()
		self.entry2.set_visibility(False)
		self.button = gtk.Button(label="OK")
		self.button.connect("clicked",self.getlogin,self.entry1,self.entry2)
		self.box = gtk.VBox()
		#self.button.add(self.box)
		self.table.attach(self.label1, 0,1,0,1)
		self.table.attach(self.label2, 0,1,0,2)
		self.table.attach(self.entry1, 1,2,0,1)		
		self.table.attach(self.entry2, 1,2,0,2)
		self.table.attach(self.box, 1,2,1,3)
		self.box.pack_start(self.button,True,False)
		self.window.show_all()
		self.window2 = gtk.Window(gtk.WINDOW_POPUP)
		self.window2.set_size_request(gtk.gdk.screen_width(),25)
		self.window2.move(0, screenheight-25)
		self.bar = gtk.MenuBar()
		self.menu = gtk.Menu()
		self.options = gtk.MenuItem("Options")
		self.shutdown = gtk.MenuItem("Shutdown")
		self.shutdown.connect("activate",gtk.main_quit)
		self.reboot = gtk.MenuItem("Reboot")
		self.reboot.connect("activate",self.rebootf)
		self.about = gtk.MenuItem("About")
		self.about.connect("activate",self.aboutinfo)
		self.bar.append(self.options)
		self.options.set_submenu(self.menu)
		self.menu.append(self.shutdown)
		self.menu.append(self.reboot)
		self.menu.append(self.about)
		self.window2.add(self.bar)
		self.window2.show_all()
def main():
	gtk.main()
	
if __name__ == "__main__":
	Base()
	main()
