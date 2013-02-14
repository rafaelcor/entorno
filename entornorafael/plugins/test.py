import horayfecha
import gtk
class Base:
	def __init__(self):
		self.window = gtk.Window()
		self.window.set_decorated(False)
		self.menubar = gtk.MenuBar()
		self.window.add(self.menubar)
		
		
		horayfecha.Base(self.menubar)
		self.window.show_all()
def main():
	gtk.main()
	
if __name__ == "__main__":
	Base()
	main()

