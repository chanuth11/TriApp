from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.label import Label
import kivy

Config.set('graphics', 'resizable', True)
kivy.require('1.9.0')


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    def input(self):
        height = self.height_input.text
        age = self.age_input.text
        weight = self.weight_input.text
        sex = self.sex.text
        activity = self.activity.text
        # error checking
        if height != "" and weight != "" and age != "" and activity != "Physical Activity" and sex != "Sex":
            if height.isnumeric() == True and weight.isnumeric() == True and age.isnumeric() == True:
                if int(height) > 0 and int(weight) > 0 and int(age) > 0:
                    # calorie needed to maintain weight
                    if sex == "Male":
                        bmrm = 66 + (6.3 * int(weight)) + (12.9 * int(height)) - (6.8 * int(age))
                        if activity == "No exercise":
                            calorie = bmrm * 1.2
                        elif activity == "1-3 days/week":
                            calorie = bmrm * 1.375
                        elif activity == "3-5 days/week":
                            calorie = bmrm * 1.55
                        elif activity == "6-7 days/week":
                            calorie = bmrm * 1.725
                        elif activity == "7 days/week":
                            calorie = bmrm * 1.9
                    elif sex == "Female":
                        bmrf = 655 + (4.3 * int(weight)) + (int(height) * 4.7) - (4.7 * int(age))
                        if activity == "No exercise":
                            calorie = bmrf * 1.2
                        elif activity == "1-3 days/week":
                            calorie = bmrf * 1.375
                        elif activity == "3-5 days/week":
                            calorie = bmrf * 1.55
                        elif activity == "6-7 days/week":
                            calorie = bmrf * 1.725
                        elif activity == "7 days/week":
                            calorie = bmrf * 1.9
                    label = Label(
                        text="total amount of calories you need to maintain your current weight: " + str(calorie),
                        font_size='20sp', pos=(0, -45))
                    # make error check so that when you calculate again text does not overlap
                    self.add_widget(label)
                    self.label_created_in_python = label

                else:
                    self.height_input.text = ""
                    self.age_input.text = ""
                    self.weight_input.text = ""
            else:
                self.height_input.text = ""
                self.age_input.text = ""
                self.weight_input.text = ""
        else:
            self.height_input.text = ""
            self.age_input.text = ""
            self.weight_input.text = ""

    def change(self):
        # go to calender window
        self.parent.current = 'third'


class Calculator(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("main.kv")


class MyMainApp(App):
    def build(self):
        Window.clearcolor = (0.6, 0.3, 0.9, 0.5)
        return kv


if __name__ == "__main__":
    MyMainApp().run()
