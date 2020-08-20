class Label():
    def __init__(self, text):
        self.text = text

    def __str__(self):
        self.length = 58
        return f"\n#{self.text:^{self.length}}#\n"

class Emphasedlabel(Label):
    def __str__(self):
        super().__str__()
        contur = "#" * (self.length + 2)
        return "\n" + contur + super().__str__() + contur + "\n"


main_label = Label("Hello OOP!")
emp_label = Emphasedlabel("Another label!!!")

print(main_label)
print(emp_label)