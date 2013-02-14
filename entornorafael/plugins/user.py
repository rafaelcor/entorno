import getpass
import gtk
#print getpass.getuser()


class Base:
	def __init__(self, menu):
		if type(menu) != gtk.MenuBar:
			raise TypeError, "a gtk.MenuBar is required"
		#self.windowu = gtk.Window()
		#self.windowu.set_decorated(False)
		#self.menubar = gtk.MenuBar()
		#self.windowu.add(self.menubar)
		self.labelu = gtk.Label(getpass.getuser())
		#self.menu = gtk.Menu()
		self.d = gtk.MenuItem(getpass.getuser())
		menu.append(self.d)
		self.d.show()
		self.labelu.show()
		#self.menubar.add(self.labelu)
		#self.windowu.show_all()
def main():
	gtk.main()
	
if __name__ == "__main__":
	Base()
	main()
