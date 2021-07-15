from tkinter import *


def icalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="powder blue")
    storeObj.pack(side=side, expand=YES, fill=BOTH)

    return storeObj


def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)

    return storeObj


class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add("*Front", "arial 20 bold")
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Calculator")


        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display, justify="right", bd=30, bg="green").pack(side=TOP, expand=NO, fill=BOTH)

        for clearButton in (["C"]):
            erase = icalc(self, TOP)
            for ichar in clearButton:
                button(erase, LEFT, ichar, lambda storeObj=display, q=ichar: storeObj.set(''))

        for numButton in ("789/", "456*", "123-", "0.+"):
            FunctionNum = icalc(self, TOP)
            for iEquals in numButton:
                button(FunctionNum, LEFT, iEquals, lambda storeOgj=display, q= iEquals: storeOgj.set(storeOgj.get() + q))


        EqualButton = icalc(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                btniEquals = button(EqualButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>', lambda e, s=self, storeObj=display: s.calc(storeObj), '+')

            else:
                btniEquals = button(EqualButton, LEFT, iEquals, lambda storeObj=display, s=' %s ' % iEquals: storeObj.set(storeObj.get() + s))


    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")


if __name__=='__main__':
    app().mainloop()