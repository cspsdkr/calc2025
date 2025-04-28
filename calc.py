import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Калькулятор")
        self.root.resizable(False, False)
        
        # Установка иконки
        try:
            self.root.iconbitmap("calc.ico")  # Укажите путь к вашей иконке
        except:
            pass
        
        self.expression = ""
        self.result = ""
        
        # Создание элементов интерфейса
        self.create_widgets()
        
    def create_widgets(self):
        # Поле ввода
        self.input_field = tk.Entry(self.root, font=('Arial', 16), justify='right', bd=5)
        self.input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Поле вывода результата (неактивное)
        self.result_field = tk.Entry(self.root, font=('Arial', 16),
                                    state='readonly',
                                    readonlybackground='white',
                                    takefocus=0,  # Запрет получения фокуса
                                    highlightthickness=0,  # Убрать рамку фокуса
                                    cursor="arrow")  # Стандартный курсор мыши
        self.result_field.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
        
        # Кнопки
        buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('C', 5, 0), ('0', 5, 1), ('=', 5, 2), ('+', 5, 3)
        ]
        
        for (text, row, col) in buttons:
            btn = ttk.Button(self.root, text=text, 
                            command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
        
        # Настройка размеров колонок
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
            
    def on_button_click(self, value):
        if value == 'C':
            self.expression = ""
            self.result = ""
        elif value == '=':
            try:
                self.result = str(eval(self.expression))
            except:
                self.result = "Ошибка"
        else:
            self.expression += value
            
        self.update_fields()
            
    def update_fields(self):
        self.input_field.delete(0, tk.END)
        self.input_field.insert(0, self.expression)
        
        # Безопасное обновление поля результата
        self.result_field.config(state='normal')
        self.result_field.delete(0, tk.END)
        self.result_field.insert(0, self.result)
        self.result_field.config(state='readonly')

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()