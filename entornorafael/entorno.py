#!/usr/bin/env python coding=utf-8
import gtk
#root_window = gtk.gdk.get_default_root_window()
#screenwidth, screenheight = root_window.get_size()
#1024x600
import os
from plugins import horayfecha
from plugins import user
gtk.rc_parse("/usr/share/themes/Clearlooks/gtk-2.0/gtkrc")



class Base:
	def logoutf(self,widget):
		import os
		import sys
		#os.system("python login.py")
		#os.system("sudo killall Xorg")
		
		os.system("killall openbox")
		sys.exit()
		
	
	
	
	def opc(self,widget):
		self.windoc = gtk.Window()
		self.windoc.set_decorated(1)
		self.windoc.set_style(gtk.Style())
		self.calendardoc = gtk.Calendar()
		self.windoc.add(self.calendardoc)
		self.windoc.set_focus(self.calendardoc)
		self.windoc.show()
		self.calendardoc.show()
		

	
    
	def exitbuttondesk(self, widget, event):
		if event.type == gtk.gdk._2BUTTON_PRESS:
			#import commands
			f = os.system('gnome-terminal &')
			#if "orden" in f:
			#	commands.getoutput('cmd')
	
	
	def nw(self,widget):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.button = gtk.Button(label="this is a test")
		self.window.add(self.button)
		self.window.show()
		self.button.show()
		
	def opent(self,widget):
		#import commands
		f = os.system('gnome-terminal &')
		#if "orden" in f:
		#	commands.getoutput('cmd')

	def __init__(self):
		self.win = gtk.Window(gtk.WINDOW_POPUP)
		#self.win.set_gravity(False)
		self.win2 = gtk.Window(gtk.WINDOW_POPUP)
		self.win3 = gtk.Window()
		#os.system("openbox")
		#self.win3.set_size_request(gtk.gdk.screen_width(), gtk.gdk.screen_height())
		self.win3.set_decorated(0)
		self.win3.fullscreen()
		self.win3.add_events(gtk.gdk.BUTTON_PRESS_MASK)
		self.menurc = gtk.Menu()#right click menu
		self.menurcitem = gtk.MenuItem("Apagar")
		self.menurcitem1 = gtk.MenuItem("Cambiar fondo de escritorio")
		self.fl = lambda shutdown:os.system("exec shutdown -h now")
		self.menurc.append(self.menurcitem)
		self.menurcitem.connect("activate", self.fl)
		self.menurcitem.show()
		self.menurcitem = gtk.MenuItem("Apagar")
		self.menurcitem1 = gtk.MenuItem("Cambiar fondo de escritorio")
		self.menurc.append(self.menurcitem1)
		self.menurcitem1.show()
		self.menurcitem1.connect("activate",self.changebackground)
		self.win3.connect_object("event", self.button_press, self.menurc)
		#self.image = gtk.Image()
		#self.image.set_from_file("fondo.jpg")
		self.pixbuf = gtk.gdk.pixbuf_new_from_file('/home/rafael/Escritorio/entornorafael/chaos.jpg')
		self.pixbuf = self.pixbuf.scale_simple(gtk.gdk.screen_width(), gtk.gdk.screen_height()-50, gtk.gdk.INTERP_BILINEAR)
		self.image = gtk.image_new_from_pixbuf(self.pixbuf)
		#self.box = gtk.VBox()
		self.fixed = gtk.Fixed()
		#self.box = gtk.VBox()
		#self.buttoninf = gtk.ToggleButton()
		#self.buttoninf.set_size_request(95,86)
		self.win3.add(self.fixed)
		#self.imageforb = gtk.Image()
		#self.imageforb.set_from_file("/home/rafael/Escritorio/entornorafael/terminal.png")
		#self.buttoninf.add(self.box)
		#self.buttoninf.connect('clicked', self.opent)
		#self.buttoninf.add(self.imageforb)
		#self.imageforb.show()
		self.table = gtk.Table(7, 15, True)
		x = 0
		y = 0
		for algo in os.listdir("/home/rafael/Escritorio/"):
			self.algo = algo
			self.buttont = gtk.ToggleButton(label=algo)
			self.buttont.connect("button_press_event",self.abrir,self.algo)
			self.buttont.set_size_request(95,86)
			self.table.attach(self.buttont, x, x+1, y, y+1)
			x += 1
			if x >= 15:
				x = 0
				y += 1
            
			self.buttont.show()
		
		self.fixed.put(self.image, 0, 25)
		self.fixed.put(self.table, 0, 25)
		self.table.show()
		##self.fixed.put(self.buttoninf, 120, 400)
		
		#self.box.pack_start(self.buttoninf, True,True,-1)
		##self.buttoninf.show()
		#self.label = gtk.Label("Terminal")
		#self.box.pack_start(self.imageforb,True,True,1)
		#self.box.pack_start(self.label,True,True,1)
		#self.buttoninf.connect("button_press_event", self.exitbuttondesk)
		#self.box.show()
		self.fixed.show()
		#self.label.show()
		
		
		#self.tg = gtk.ToggleButton(label="hello")
		#self.box.pack_start(self.tg,False,False,2)
		#self.box.pack_start(self.image,True,True,1)
		self.win.set_resizable(False)
		self.win2.set_resizable(False)
		self.win3.set_resizable(False)
		self.win.set_size_request(gtk.gdk.screen_width(), 25)
		self.win2.set_size_request(gtk.gdk.screen_width(), 25)
		self.win.move(0, gtk.gdk.screen_height()-25)
		self.win2.move(0, 0)
		self.bar = gtk.MenuBar()
		self.bar2 = gtk.MenuBar()
		
		self.win.add(self.bar)
		self.win2.add(self.bar2)
		#self.win.add(self.box)
		#self.bar.add(self.box)
		self.button1 = gtk.Button()
		#self.bar.add(self.button1)
		self.tad = gtk.MenuItem("Aplicaciones")
		self.tad2 = gtk.MenuItem("Aplicaciones")
		self.sistema = gtk.MenuItem("Sistema")
		self.logout = gtk.MenuItem("Log out")
		self.sb = gtk.Menu()
		self.sb2 = gtk.Menu()
		self.menu3 = gtk.Menu()
		self.exit = gtk.MenuItem("Exit")
		self.exit.connect("activate", gtk.main_quit)
		self.wm = gtk.MenuItem("Abrir ventana")
		self.oc = gtk.MenuItem("Abrir calendario")
		
		self.wm.connect("activate", self.nw)
			
		self.sb.append(self.exit)
		
		#self.win.set_opacity(0.9)
		self.tad.set_submenu(self.sb)
		
		
		
		self.bar.append(self.tad)
		
		###making a basic menu
		self.bar.append(self.sistema)
		horayfecha.Base(self.bar)
		self.sistema.set_submenu(self.menu3)
		self.menu3.append(self.logout)
		self.menu3.show()
		self.sistema.show()
		self.logout.show()
		###
		self.logout.connect("activate",self.logoutf)
		self.poweritem = gtk.MenuItem()
		self.powericon = gtk.image_new_from_icon_name("system-shutdown", gtk.ICON_SIZE_LARGE_TOOLBAR)
		self.poweritem.add(self.powericon)
		#self.poweritem.selected-shadow-type(gtk.SHADOW_OUT)
		#self.poweritem.connect("button_press_event",self.logoutf)
		self.bar2.append(self.tad2)
		self.bar2.append(self.poweritem)
		user.Base(self.bar2)
		self.sb.append(self.wm)
		self.sb.append(self.oc)
		self.oc.connect("activate",self.opc)
		self.oc.show()
		#self.box.pack_start(self.bar)
		self.ap = gtk.MenuItem("Abrir")
		self.sb.append(self.ap)
		#self.ap.connect("activate", self.nw)
		self.sbb = gtk.Menu()
		self.ap.set_submenu(self.sbb)
		self.apmi = gtk.MenuItem("Terminal")
		self.apmi.connect("activate", self.opent)
		self.sbb.append(self.apmi)
		#self.win3.fullscreen()
		self.win3.show()
		self.win.show()
		self.bar.show()
		self.tad.show()
		self.sb.show()
		self.exit.show()
		self.wm.show()
		self.ap.show()
		self.sbb.show()
		self.apmi.show()
		#self.box.show()
		self.win2.show()
		self.bar2.show()
		self.tad2.show()
		self.sb2.show()
		self.poweritem.show()
		self.powericon.show()
		self.image.show()
		#os.system("openbox --replace")
		#self.box.show()
		#self.tg.show()

	def gettextd(self,filename):
		
			#self.textd = self.entryd.get_text()
		self.pixbuf = gtk.gdk.pixbuf_new_from_file(filename)
		self.pixbuf = self.pixbuf.scale_simple(gtk.gdk.screen_width(), gtk.gdk.screen_height(), gtk.gdk.INTERP_BILINEAR)
		self.image = gtk.image_new_from_pixbuf(self.pixbuf)
		self.image.show()
		self.fixed.put(self.image, 0, 0)
		self.dialog.hide()
		self.refreshdesktop()
		

		#glib.GError

	def button_press(self, widget, event):
		if event.type == gtk.gdk.BUTTON_PRESS and event.button == 3:
			#make widget popup
			widget.popup(None, None, None, event.button, event.time)

	def windhide(self,widget):
		self.wind.hide()

	def refreshdesktop(self):
		self.fixed.put(self.table, 0, 25)
		#self.imageforb.realize()
		#self.buttoninf.realize()
		#self.box.realize()
		self.fixed.realize()
		#self.label.realize()


	#self.pixbuf = gtk.gdk.pixbuf_new_from_file('fondo.jpg')

	def changebackground(self, widget):
		
		#self.wind.set_decorated(False)
		#self.wind.set_skip_taskbar_hint(True)
		#self.wind.set_size_request(500, 100)
		#self.dialog.set_position(gtk.WIN_POS_CENTER)
		self.dialog = gtk.FileChooserDialog("Open..",
                               None,
                               gtk.FILE_CHOOSER_ACTION_OPEN,
                               (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                gtk.STOCK_OPEN, gtk.RESPONSE_OK))
		self.dialog.set_default_response(gtk.RESPONSE_OK)
		#self.filename = self.dialog.get_filename()
		self.dialog.set_position(gtk.WIN_POS_CENTER)
		self.filter = gtk.FileFilter()
		self.filter.set_name("Images")
		self.filter.add_mime_type("image/jpg")
		self.filter.add_pattern("*.jpg")
		self.dialog.add_filter(self.filter)

		self.response = self.dialog.run()
		if self.response == gtk.RESPONSE_OK:
			print self.dialog.get_filename(), 'selected'
			self.gettextd(self.dialog.get_filename())
		elif self.response == gtk.RESPONSE_CANCEL:
			print 'Closed, no files selected'
		self.dialog.destroy()
		
		
	def abrir(self, widget, event, archivo):
		if event.type == gtk.gdk._2BUTTON_PRESS:
			try:
				if os.path.isdir(archivo):
					os.system("nautilus %s" % archivo )
					print archivo
					
				elif os.path.islink(archivo):
					print archivo
					print 'enlace'
				elif os.path.isfile(archivo):
					print "Es un archivo"
					print archivo
					self.archivosp = archivo
					self.archivospp = archivo.split(".")
					print self.archivospp[-1]
					if self.archivospp[-1] == "deskfile":
						print "en construccion"
					elif len(self.archivospp) <= 1:
						import commands
						self.mimef = commands.getoutput("file " + "%s"%self.archivosp).split(": ")[1].split(",")[0]
						print self.mimef
						if self.mimef == "POSIX shell script text executable" or "very short file (no magic)" or "ASCII English text":
							os.system("nano %s"%self.archivosp)
			except:
				print "una excepcion"
		
		
	
def main():
	gtk.main()
	
if __name__ == "__main__":
	Base()
	main()
