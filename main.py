
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class CalculatorApp(App):
    def build(self):
        root_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.solution = TextInput(
            multiline=False, 
            readonly=True, 
            halign="right", 
            font_size=40,
            size_hint_y=0.25
        )
        root_layout.add_widget(self.solution)
        
        buttons = [
            ['C', '⌫', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['00', '0', '.', '=']
        ]
        
        grid = GridLayout(cols=4, spacing=10)
        
        for row in buttons:
            for label in row:
                button = Button(
                    text=label,
                    font_size=28,
                    pos_hint={"center_x": 0.5, "center_y": 0.5}
                )
                button.bind(on_press=self.on_button_press)
                grid.add_widget(button)
                
        root_layout.add_widget(grid)
        return root_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            self.solution.text = ""
        elif button_text == "⌫":
            self.solution.text = current[:-1]
        elif button_text == "=":
            try:
                expression = current.replace('%', '/100')
                self.solution.text = str(eval(expression))
            except Exception:
                self.solution.text = "Error"
        else:
            if current == "Error":
                current = ""
            self.solution.text = current + button_text

if __name__ == "__main__":
    CalculatorApp().run()
