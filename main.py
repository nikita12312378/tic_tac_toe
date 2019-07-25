from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Canvas, Color, Rectangle, Line
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from random import random

class tic_tac_toeApp(App):
    def restart(self,instance):
        tic_tac_toeApp.get_running_app().stop()
        tic_tac_toeApp().run()
    def game_over(self, instance, res):
        self.bl.add_widget(Button(text=(res+". Restart"), size_hint=(1,.1),background_color=(random(),random(),random(),random()),on_press = self.restart))
    def tictac(self,instance,but):
        if self.check %2 == 0 and but not in self.checker and but not in self.checker1:
            exec("self.but"+str(but)+".text = 'X'")
            self.check += 1
            self.checker[but]=['X']
            for i in self.write:
                if i[0] in self.checker and i[1] in self.checker and i[2] in self.checker:
                    if self.checker123 == 0:
                        self.game_over(1,'The 1st player won')
                        self.check-=2
                        self.checker123 = 1
                        color = (random(),random(),random(),random())
                        for j in range(3):
                            exec('self.but'+str(i[j])+'.background_color=(color)')
        elif but not in self.checker and but not in self.checker1:
            self.check +=1
            exec("self.but"+str(but)+".text = 'O'")
            self.checker1[but]=['O']
            for i in self.write:
                if i[0] in self.checker1 and i[1] in self.checker1 and i[2] in self.checker1:
                    if self.checker123 == 0:
                        self.game_over(1,'The 2nd player won')
                        self.check-=2
                        color = (random(),random(),random(),random())
                        for j in range(3):
                            exec('self.but'+str(i[j])+'.background_color=(color)')
                        self.checker123 = 1
        if self.check == 9:
            self.game_over(1,'Draw')
    def build(self):
        self.checker123 = 0
        self.write = [[0,1,2],[0,3,6],[3,4,5],[6,7,8],[2,5,8],[1,4,7],[0,4,8],[2,4,6]]
        self.bl = BoxLayout(orientation='vertical')
        self.checker = {}
        self.checker1 = {}
        self.check = 0
        self.gl = GridLayout(cols=3)
        self.bl.add_widget(self.gl)
        for i in range(9):
            exec("self.but"+str(i)+"= Button(font_size = 50,on_press = lambda a, self=self: self.tictac(1,"+str(i)+"))")
            eval('self.gl.add_widget(self.but'+str(i)+')')
        return self.bl

class start(Widget):
    def __init__(self, **kwargs):
        super(start, self).__init__(**kwargs)
        with self.canvas:
            Rectangle(source = "tic_tac.png", size = (Window.width, Window.height))

class start1(Widget):
    def __init__(self, **kwargs):
        super(start1, self).__init__(**kwargs)
        with self.canvas:
            Color(0,1,0)
            self.size = [(Window.width-40)/2,(Window.height-40)/2]
            Line(points=[self.size[0],self.size[1],self.size[0], self.size[1]+40, self.size[0]+40,self.size[1]+20], close = True, cap = 'round', joint = 'round', width = 5)

    def on_touch_down(self,touch):
        if touch.x > self.size[0] and touch.y > self.size[1] and touch.x < self.size[0]+40 and touch.y < self.size[1]+40:
            with self.canvas:
                Color(1,1,1)

                Rectangle(size = (Window.width,Window.height))
            tic_tac_toeApp().run()
class PlayApp(App):
    def build(self):
        name = Label(text = 'Крестики нолики', color = (1,1,0,1), font_size = '30',pos = (Window.width/2-50,Window.height-100))
        parent = Widget()
        parent.add_widget(name)
        parent.add_widget(start())
        parent.add_widget(start1())
        return parent

if __name__ == '__main__':
    PlayApp().run()
