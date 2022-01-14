from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel

Builder.load_file('main.kv')

class MyLayout(TabbedPanel):
	def switch_click(self, switchObject, switchValue):
		if (switchValue):
			self.ids.my_label.text = 'Ustawienia odblokowane'
			self.ids.my_boxlayout.disabled = False
		else:
			self.ids.my_label.text = 'Ustawienia zablokowane'
			self.ids.my_boxlayout.disabled = True

class MyApp(App):
	def build(self):
		return MyLayout()

if __name__ == '__main__':
	MyApp().run()