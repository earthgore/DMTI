from tkinter import *
from N import COM_NN_D
from N import natural

constN = 0;
class Window:
    global str_var, opened
    def __init__(self, wight, height, title="ffr", resizable=(True, True), icon=None):

        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{wight}x{height}+900+100")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)

        self.entry = Entry(self.root)
        self.entry1 = Entry(self.root)
        self.buttonN = Button(self.root, text="Натуральные числа с нулем", width=50, height=5, bg="#F0E68C",  command=self.get_algN, font="Arial 10")
        self.button2 = Button(self.root, text="Целые числа", width=50, height=5, bg="#F0E68C", font="Arial 10")
        self.button3 = Button(self.root, text="Рациональная числа", width=50, height=5, bg="#F0E68C", font="Arial 10")
        self.button4 = Button(self.root, text="Многочлен с рациональными коэффициентами", width=50, height=5, bg="#F0E68C", font="Arial 10")
        self.buttonN_1 = Button(self.root, text="Сравнение натуральных чисел", width=50, height=5, bg="#F0E68C", font="Arial 10")
        self.buttonN_2 = Button(self.root, text="Проверка на ноль", width=50, height=5, bg="#F0E68C", font="Arial 10")
        self.buttonN_3 = Button(self.root, text="Добавление 1 к натуральному числу", width=50, height=5, bg="#F0E68C", font="Arial 10")
        self.buttonN_4 = Button(self.root, text="Сложение натуральных чисел", width=50, height=5, bg="#F0E68C", font="Arial 10")
        self.buttonN_5 = Button(self.root, text="Вычитание из первого большего натурального числа второго меньшего или равного", width=50, height=5, bg="#F0E68C", font="Arial 10")




    def run(self):
        self.draw_widgets()
        self.root.mainloop()



    def draw_widgets(self):
        self.buttonN.pack()
        self.button2.pack()
        self.button3.pack()
        self.button4.pack()



    def get_algN(self):

        self.buttonN.forget()
        self.button2.forget()
        self.button3.forget()
        self.button4.forget()
        self.buttonN_1.pack()
        self.buttonN_2.pack()
        self.buttonN_3.pack()
        self.buttonN_4.pack()
        self.buttonN_5.pack()



a = natural(input("Введите первое число:"))
b = natural(input("Введите второе число:"))

print(COM_NN_D(a,b))
"""if __name__ == "__main__":
    window = Window(400, 600, "Кодер")
    window.run()"""