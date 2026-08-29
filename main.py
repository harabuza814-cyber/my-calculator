import math
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class ScientificCalculatorApp(App):
    def build(self):
        root_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Display Screen
        self.solution = TextInput(
            multiline=False, 
            readonly=True, 
            halign="right", 
            font_size=32,
            size_hint_y=0.2
        )
        root_layout.add_widget(self.solution)
        
        # Scientific & Basic Buttons Layout
        buttons = [
            ['sin', 'cos', 'tan', 'C', '⌫'],
            ['log', 'ln', '√', '(', ')'],
            ['x²', 'π', 'e', '^', '/'],
            ['7', '8', '9', '*', '%'],
            ['4', '5', '6', '-', '+'],
            ['1', '2', '3', '0', '.'],
            ['00', '=', '', '', '']
        ]
        
        grid = GridLayout(cols=5, spacing=6)
        
        for row in buttons:
            for label in row:
                if label == '':
                    grid.add_widget(BoxLayout()) # Empty space filler
                    continue
                button = Button(
                    text=label,
                    font_size=20,
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
                # Replace scientific symbols with Python math library functions
                expr = current
                expr = expr.replace('π', str(math.pi))
                expr = expr.replace('e', str(math.e))
                expr = expr.replace('^', '**')
                expr = expr.replace('%', '/100')
                expr = expr.replace('√', 'math.sqrt')
                expr = expr.replace('sin', 'math.sin')
                expr = expr.replace('cos', 'math.cos')
                expr = expr.replace('tan', 'math.tan')
                expr = expr.replace('log', 'math.log10')
                expr = expr.replace('ln', 'math.log')
                
                # Simple handling for x²
                if '²' in expr:
                    expr = expr.replace('²', '**2')

                result = str(eval(expr))
                self.solution.text = result
            except Exception:
                self.solution.text = "Error"
        elif button_text == "x²":
            self.solution.text = current + "**2"
        elif button_text in ['sin', 'cos', 'tan', 'log', 'ln', '√']:
            self.solution.text = current + button_text + "("
        else:
            if current == "Error":
                current = ""
            self.solution.text = current + button_text

if __name__ == "__main__":
    ScientificCalculatorApp().run()
