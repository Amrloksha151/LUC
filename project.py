import tkinter as tk
import ttkbootstrap as ttk
import time


def main():
    global root
    root = ttk.Window(
        title="LUConverto", themename="cyborg", iconphoto="convert.png"
    )
    root.geometry("800x600")
    root.resizable(False, False)

    # Title
    global title
    title = ttk.Label(master=root, text="LUConverto", font="Impact 32 bold")
    title.pack()

    # Menu(s)
    global inputVar, outputVar, menusFrame
    menusFrame = ttk.Frame(root)
    inputMenu = tk.Menu(font="Courier 12", title="Input-Unit")
    outputMenu = tk.Menu(font="Courier 12", title="Output-Unit")
    options = ["KiloMeter", "CentiMeter", "Meter", "Yard", "Mile"]
    inputVar = tk.StringVar()
    outputVar = tk.StringVar()
    for option in options:
        inputMenu.add_radiobutton(label=option, value=option, variable=inputVar)
        outputMenu.add_radiobutton(label=option, value=option, variable=outputVar)
    inputMenuButton = ttk.Menubutton(master=menusFrame, text="Input", menu=inputMenu)
    inputLabel = ttk.Label(master=menusFrame, font="Courier 16", text="Input: ")
    outputMenuButton = ttk.Menubutton(master=menusFrame, text="Output", menu=outputMenu)
    outputLabel = ttk.Label(master=menusFrame, font="Courier 16", text="Output: ")
    inputLabel.pack(side="left")
    inputMenuButton.pack(side="left")
    outputLabel.pack(side="left")
    outputMenuButton.pack(side="left")
    menusFrame.pack(pady=60)
    # Entry
    global entryVar, entryFrame
    entryFrame = ttk.Frame(master=root)  # Frame
    entryVar = tk.StringVar()  # Var
    entryLabel = ttk.Label(master=entryFrame, text="Amount: ", font="Courier 20")
    entry = ttk.Entry(master=entryFrame, textvariable=entryVar, width=40)
    entryLabel.pack(side="left")
    entry.pack(side="left")
    entryFrame.pack(pady=60)

    # Submit Button
    global submitButton
    submitButton = ttk.Button(
        master=root, text="Submit", width=20, padding=10, command=convert
    )
    submitButton.pack(pady=60)
    # Loop
    root.mainloop()


def hide(*args):
    args = list(args)
    for arg in args:
        arg.pack_forget()


def appear(*args):
    args = list(args)
    for arg in args:
        arg.pack(pady=60)


def convert():
    try:
        amount = float(entryVar.get())
    except ValueError:
        pass
    else:
        cm = 1
        m = 100
        km = 1000 * m
        mil = 1.609344 * km
        yr = mil / 1760

        # Simplified input
        if inputVar.get() == "CentiMeter":
            origin = amount * cm
        elif inputVar.get() == "KiloMeter":
            origin = amount * km
        elif inputVar.get() == "Meter":
            origin = amount * m
        elif inputVar.get() == "Yard":
            origin = amount * yr
        elif inputVar.get() == "Mile":
            origin = amount * mil

        # Output
        if outputVar.get() == "CentiMeter" and origin:
            out = origin / cm
            output = f"{round(out, 3)} CentiMeter(s)"
        elif outputVar.get() == "KiloMeter" and origin:
            out = origin / km
            output = f"{round(out, 3)} KiloMeter(s)"
        elif outputVar.get() == "Meter" and origin:
            out = origin / m
            output = f"{round(out, 3)} Meter(s)"
        elif outputVar.get() == "Yard" and origin:
            out = origin / yr
            output = f"{round(out, 3)} Yard(s)"
        elif outputVar.get() == "Mile" and origin:
            out = origin / mil
            output = f"{round(out, 3)} Mile(s)"
        else:
            output = "Invalid input"

        hide(entryFrame, menusFrame, submitButton)
        root.update()
        title.configure(text="Output")
        outputGUI = ttk.Label(master=root, text=output, font="Courier 20")
        outputGUI.pack(pady=200)
        root.update()
        # Delay
        time.sleep(5)
        # Reset
        title.configure(text="LUConverto")
        outputGUI.pack_forget()
        appear(menusFrame, entryFrame, submitButton)
        root.update()


if __name__ == "__main__":
    main()
