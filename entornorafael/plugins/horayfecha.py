#!/usr/bin/env python
#coding=utf-8
import gtk
import gobject
import time


class Base:
	def actualizar(self,widget):
		try:
			self.date.get_child().set_text(time.ctime(time.time()))
			return True
		except:
			return False
	
	
	def __init__(self, menu):
	
		if type(menu) != gtk.MenuBar:
			raise TypeError, "a gtk.MenuBar is required"
		#self.windowd = gtk.Window()
		#self.windowd.set_decorated(False)
		#self.menubard = gtk.MenuBar()
		#self.windowd.add(self.menubard)
		#self.window.set_title("Date and hour")
		#self.windowd.connect("destroy", gtk.main_quit)
		self.date = gtk.MenuItem(time.ctime(time.time()))
		menu.append(self.date)
		self.date.show()
		menu.show()
		#self.windowd.add(self.date)
		#self.windowd.show_all()
		gobject.idle_add(self.actualizar,self.date)
def main():
	gtk.main()
if __name__ == "__main__":
	Base()
	main()
