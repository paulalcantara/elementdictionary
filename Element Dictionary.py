from tkinter import *

class Element:
    def __init__(self, ElementName, ElementSymbol, AtomicNumber, AtomicWeight, Ayes):
        self.ElementName = ElementName
        self.ElementSymbol = ElementSymbol
        self.AtomicNumber = AtomicNumber
        self.AtomicWeight = AtomicWeight
        self.Ayes = Ayes
    def display(self):
        print("Element      : ", self.ElementName)
        print("Symbol       : ", self.ElementSymbol)
        print("Atomic Number: ", self.AtomicNumber)
        print("Atomic Weight: ", self.AtomicWeight)
        
TitleText = ("Arial", 24, "bold")
TitleCredits = ("MS Sans Serif", 12, "bold")
FontStyle1 = ("Arial", 18, "bold")
FontStyle2 = ("MS Sans Serif", 12, "bold")
FontStyle3 = ("Arial", 8, "bold")
FontStyle4 = ("Calibri", 16, "bold")
FontStyle5 = ("Calibri", 45, "bold")
FontYes = ("Calibri", 10)

class Window(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Element Finder")
        self.geometry("400x400")
        self.frames = {}
        hold = Frame(self)
        hold.pack(side = "top", fill = "both", expand = True)
        hold.grid_rowconfigure(0, weight = 1)
        hold.grid_columnconfigure(0, weight = 1)
        for i in (Title, Front, Element_Name, Element_Symbol, Atomic_Number, Atomic_Weight):
            page_name = i.__name__
            frame = i(parent=hold, controller = self)
            self.frames[page_name] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        self.show_frame("Title")
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class Title(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg = "#29B6F6", borderwidth = 10, relief = "solid")
        title = Label(self, text = "\nELEMENT FINDER", font = TitleText, bg = "#29B6F6")
        creds = Label(self, text = "\nCreated by: Paul Alcantara\n", font = TitleCredits, bg = "#29B6F6", fg = "#883000")
        title.pack(side = "top", pady = 10)
        creds.pack(side = "bottom", pady = 10)
        start = Button(self, text = "LAUNCH", borderwidth = 5, relief = "raise", command = lambda: controller.show_frame("Front"),font = FontStyle5, bg = "#D6B75A")
        start.config(width = 50, height = 4)
        start.pack(side = "bottom", anchor = E, fill = X, expand = YES, padx = 50, pady = 10)
class Front(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg = "#9B870C")
        text1 = Label(self, text = "ELEMENT FINDER", font = FontStyle1, bg = "#284646", fg = "white")
        text2 = Label(self, text = "Search by:", font = FontStyle4, fg = "#616166", bg = "#9B870C")
        creds = Label(self, text = "Created by: Paul Alcantara", font = FontStyle3, bg = "#284646", fg = "white")
        text1.pack(side = "top", fill = "x", pady = 10)
        text2.pack(padx = 5, pady = 10)
        creds.pack(side = "bottom", fill = "x", pady = 20)

        opt1 = Button(self, text = "Element Name",
                            command = lambda: controller.show_frame("Element_Name"),font = FontStyle2, bg = "#fed8b1", fg = "#10A5F5")
        opt1.config(width = 25, height = 2)
        opt2 = Button(self, text = "Element Symbol",
                            command = lambda: controller.show_frame("Element_Symbol"),font = FontStyle2, bg = "#89D5D2", fg = "#883000")
        opt2.config(width = 25, height = 2)
        opt3 = Button(self, text = "Atomic Number",
                            command = lambda: controller.show_frame("Atomic_Number"), font = FontStyle2, bg = "#fed8b1", fg = "#10A5F5")
        opt3.config(width = 25, height = 2)
        opt4 = Button(self, text = "Atomic Weight",
                            command = lambda: controller.show_frame("Atomic_Weight"), font = FontStyle2, bg = "#89D5D2", fg = "#883000")
        opt4.config(width = 25, height = 2)
        opt1.pack()
        opt2.pack()
        opt3.pack()
        opt4.pack()

class Element_Name(Frame):
    def __init__(self, parent, controller):
       self.count = 0
       Frame.__init__(self, parent)
       self.controller = controller
       self.configure(bg = "orange", borderwidth = 8, relief = "solid")
       space1 = Label(self, text = " ", bg = "orange")
       space1.pack()
       text1 = Label(self, text="                 Element Name:                 ", font = FontStyle1, fg = "white", bg = "#883000")
       text1.pack(pady=10)
       space2 = Label(self, text = " ", bg = "orange")
       space2.pack()
       self.atomic = Entry(self, width = 35, justify = "center", font = FontStyle2)
       self.atomic.pack()
       opt1 = Button(self, text = "Search", width = 15, command = self.Display, font = FontStyle2, fg = "blue")
       opt2 = Button(self, text = "Back",
                           command = lambda: controller.show_frame("Front"), font = FontStyle2)
       opt2.config(width=50, height = 2, bg = "#fed8b1")
       opt1.pack(side = 'top')
       opt2.pack(side = 'bottom')
       d = []
    def Display(self):
        r = []
        if self.count != 0:
            for i in (self.d):
                i.destroy()
        self.d = []
        r = SearchTable(self.atomic.get(),None, None, None, None)
        if len(r) != 0:
            for i in (r):
                self.d.append(Label(self, font = FontStyle4, bg = "orange", text = "\nElement Symbol: " + str(i.ElementSymbol)))
                self.d.append(Label(self, font = FontStyle4, bg = "orange", text = "Atomic Number: " + str(i.AtomicNumber)))
                self.d.append(Label(self, font = FontStyle4, bg = "orange", text = "Atomic Weight: " + str(i.AtomicWeight)))
                self.d.append(Label(self, font = FontYes, fg = "brown", bg = "orange", text = "\nTrivia: " +str(i.Ayes) + "\n"))
        else:
            self.d.append(Label(self, text = "\nThe Entered Element is Not Found\n\nReminder:\nCheck Your Spelling",
                                fg = "red", bg = "orange", font = FontStyle4))
        for i in (self.d):
            i.pack()
        self.count += 1

class Element_Symbol(Frame):
    def __init__(self, parent, controller):
       self.count = 0
       Frame.__init__(self, parent)
       self.controller = controller
       self.configure(bg = "#008080", borderwidth = 8, relief = "solid")
       text1 = Label(self, text = " ", bg = "#008080")
       text1.pack(side = "top", fill  ="x", pady=10)
       text2 = Label(self, text = "               Element Symbol:               ", font = FontStyle1, fg = "white", bg = "#284646")
       space = Label(self, text = " ", bg = "#008080")
       text2.pack()
       self.atomic = Entry(self, width = 35, justify = "center", font = FontStyle2)
       space.pack()
       self.atomic.pack()
       opt1=Button(self, text = "Search", width = 15, command = self.Display, font = FontStyle2, fg = "blue")
       opt2 = Button(self, text = "Back",
                           command=lambda: controller.show_frame("Front"), font = FontStyle2)
       opt2.config(width=50, height = 2, bg = "#89D5D2")
       opt1.pack(side = 'top')
       opt2.pack(side = 'bottom')
       d = []
    def Display(self):
        r = []
        if self.count != 0:
            for i in (self.d):
                i.destroy()
        self.d = []
        r = SearchTable(None, self.atomic.get(), None, None, None)
        if len(r) != 0:
            for i in (r):
                self.d.append(Label(self, font = FontStyle4, bg = "#008080", text = "\nElement Name: " + i.ElementName))
                self.d.append(Label(self, font = FontStyle4, bg = "#008080", text = "Atomic Number: " + str(i.AtomicNumber)))
                self.d.append(Label(self, font = FontStyle4, bg = "#008080", text = "Atomic Weight: " + str(i.AtomicWeight)))
                self.d.append(Label(self, font = FontYes, fg = "white", bg = "#008080", text = "\nTrivia: " +str(i.Ayes) + "\n"))
        else:
            self.d.append(Label(self, text = "\nThe Entered Element Symbol is Not Found\n\nReminder:\nCheck Your Spelling",
                                    fg = "red", bg = "#008080", font = FontStyle4))
        for i in (self.d):
            i.pack()
        self.count += 1
        
class Atomic_Number(Frame):
    def __init__(self, parent, controller):
        self.count = 0
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg = "orange", borderwidth = 8, relief = "solid")
        space = Label(self, text = " ", bg = "orange")
        space.pack()
        text1 = Label(self, text = "               Atomic Number:               ", font = FontStyle1, fg = "white", bg = "#883000")
        text1.pack(side = "top", fill = "x", pady = 10)
        text2 = Label(self, text = "Integer Only", font = FontStyle2, bg = "orange")
        text2.pack()
        self.atomic = Entry(self, width = 35, justify = "center", font = FontStyle2)
        self.atomic.pack()
        opt1 = Button(self, text = "Search", width = 15, command = self.Display, font = FontStyle2, fg = "blue")
        opt2 = Button(self, text = "Back",
                           command = lambda: controller.show_frame("Front"), font = FontStyle2, bg = "#fed8b1")
        opt2.config(width = 50, height = 2)
        opt1.pack(side = 'top')
        opt2.pack(side = 'bottom')
        d = []
    def Display(self):
        r = []
        if self.count != 0:
            for i in (self.d):
                i.destroy()
        self.d = []
        r = SearchTable(None, None, self.atomic.get(), None, None)
        if len(r) != 0:
            for i in (r):
                self.d.append(Label(self, font = FontStyle4, bg = "orange", text = "\nElement Name: " + i.ElementName))
                self.d.append(Label(self, font = FontStyle4, bg = "orange", text = "Element Symbol: " + i.ElementSymbol))
                self.d.append(Label(self, font = FontStyle4, bg = "orange", text = "Atomic Weight: " + str(i.AtomicWeight)))
                self.d.append(Label(self, font = FontYes, fg = "brown", bg = "orange", text = "\nTrivia: " +str(i.Ayes) + "\n"))
        else:
            self.d.append(Label(self, text = "\nThe Entered Value Points to None in List\n\nReminder:\nUse Integers Only",
                                    font = FontStyle4, fg = "red", bg = "orange"))
        for i in (self.d):
            i.pack()
        self.count += 1
        
class Atomic_Weight(Frame):
    def __init__(self, parent, controller):
       self.count = 0
       Frame.__init__(self, parent)
       self.controller = controller
       self.configure(bg = "#008080", borderwidth = 8, relief = "solid")
       space = Label(self, text = " ", bg = "#008080")
       space.pack()
       text1 = Label(self, text = "Atomic Weight:", font = FontStyle1, fg = "white", bg = "#284646")
       text1.pack(side = "top", fill = "x", pady = 10)
       text2 = Label(self, text="Value Should Have 3 Decimal Places ", font = FontStyle2, bg = "#008080", fg = "white")
       text2.pack()
       self.atomic = Entry(self, width = 35, justify = "center", font = FontStyle2)
       self.atomic.pack()
       opt1=Button(self, text = "Search", width = 15, command = self.Display, font = FontStyle2, fg = "blue")
       opt2 = Button(self, text = "Back",
                           command = lambda: controller.show_frame("Front"), font = FontStyle2)
       opt2.config(width=50, height = 2, bg = "#89D5D2")
       opt1.pack(side = 'top')
       opt2.pack(side = 'bottom')
       d = []
    def Display(self):
        r = []
        if self.count != 0:
            for i in (self.d):
                i.destroy()
        self.d = []
        r = SearchTable(None, None, None, float(self.atomic.get()), None)
        if len(r) != 0:
            for i in (r):
                self.d.append(Label(self, font = FontStyle4, bg = "#008080", text = "\nElement Name: " + i.ElementName))
                self.d.append(Label(self, font = FontStyle4, bg = "#008080", text = "Element Symbol: " + i.ElementSymbol))
                self.d.append(Label(self, font = FontStyle4, bg = "#008080", text = "Atomic Number: " + str(i.AtomicNumber)))
                self.d.append(Label(self, font = FontYes, bg = "#008080", text = "\nTrivia: " +str(i.Ayes) + "\n"))
        else:
            self.d.append(Label(self, text = "\nThe Entered Value Points to None in List\n\nReminder:\nNumber Should Have 3 Decimal Places\n\n",
                                    font = FontStyle4, fg = "red", bg = "#008080"))
        for i in (self.d):
            i.pack()
        self.count += 1

def AllElements():
    x = []
    x.append(Element("Hydrogen", "H", 1, 1.008, "Hydrogen is the only element that can exist\nwithout neutrons."))
    x.append(Element("Helium", "He", 2, 4.003, "Helium is the second-lightest element."))
    x.append(Element("Lithium", "Li", 3, 6.941, "Used extensively in rechargeable batteries."))
    x.append(Element("Beryllium", "Be", 4, 9.012, "It is a hard metal, but is brittle at\nroom temperature."))
    x.append(Element("Boron", "B", 5, 10.811, "Has the highest melting point of the metalloids." ))
    x.append(Element("Carbon", "C", 6, 12.011, "It's one of the most abundant element in\nthe universe."))
    x.append(Element("Nitrogen", "N", 7, 14.007, "Has no odor, is tasteless, and colorless."))
    x.append(Element("Oxygen", "O", 8, 15.999, "Supports combustion."))
    x.append(Element("Fluorine", "F", 9, 18.998, "Most reactive and the most electronegative\nof all the elements."))
    x.append(Element("Neon", "Ne", 10, 20.180, "One of the rarest elements on Earth."))
    x.append(Element("Sodium", "Na", 11, 22.990, "Highly reactive."))
    x.append(Element("Magnesium", "Mg", 12, 24.305, "It's the eighth-most abundant element in\nthe universe."))
    x.append(Element("Aluminum", "Al", 13, 26.982, "It Doesn't Rust."))
    x.append(Element("Silicon", "Si", 14, 28.086, "Like water, silicon has a higher density as\na liquid than as a solid."))
    x.append(Element("Phosphorus", "P", 15, 30.974, "Found in bones."))
    x.append(Element("Sulfur", "S", 16, 32.066, "Sulfur compounds are why onions make you cry."))
    x.append(Element("Chlorine", "Cl", 17, 35.453, "The third most abundant element in the\nEarth's oceans."))
    x.append(Element("Argon", "Ar", 18, 39.948, "Produced industrially by cryogenically\ndistilling air."))
    x.append(Element("Potassium", "K", 19, 39.098, "Potassium has a low density for a metal."))
    x.append(Element("Calcium", "Ca", 20, 40.078, "The body needs calcium to maintain strong bones."))
    x.append(Element("Scandium", "Sc", 21, 44.956, "Used in alloys much like aluminum."))
    x.append(Element("Titanium", "Ti", 22, 47.867, "Can be Found in almost every living thing."))
    x.append(Element("Vanadium", "V", 23, 50.942, "It can be found in more than 60 minerals."))
    x.append(Element("Chromium", "Cr", 24, 51.996, "In its pure form, chromium is a silvery, lustrous,\nhard metal that has a high polish, ideal for electroplating."))
    x.append(Element("Manganese", "Mn", 25, 54.938, "Twelfth most abundant element in the\nEarth's crust"))
    x.append(Element("Iron", "Fe", 26, 55.845, "One of the main component of meteorites."))
    x.append(Element("Cobalt", "Co", 27, 58.933, "Pure Cobalt Cannot be Found in Nature."))
    x.append(Element("Nickel", "Ni", 28, 58.693, "The fifth most abundant element on Earth."))
    x.append(Element("Copper", "Cu", 29, 63.546, "An essential element for human nutrition."))
    x.append(Element("Zinc", "Zn", 30, 65.38, "Has a self-healing mechanism in it."))
    x.append(Element("Gallium", "Ga", 31, 69.723, "It is considered to be non-toxic."))
    x.append(Element("Germanium", "Ge", 32, 72.631, "Stable in air and water, and is unaffected\nby alkalis and acids, except nitric acid."))
    x.append(Element("Arsenic", "As", 33, 74.922, "It has poor conductivity to electricity."))
    x.append(Element("Selenium", "Se", 34, 78.972, "Found in metal sulfide ores, where it\npartially replaces the sulfur."))
    x.append(Element("Bromine", "Br", 35, 79.904, "Bromine is the tenth most abundant element\nin sea water."))
    x.append(Element("Krypton", "Kr", 36, 84.798, "Named from the Greek word kryptos\nmeaning hidden."))
    x.append(Element("Rubidium", "Rb", 37, 85.468, "Rubidium melts just a little above\nbody temperature."))
    x.append(Element("Strontium", "Sr", 38, 87.62, "A soft, silvery metal that burns in\nair and reacts with water."))
    x.append(Element("Yttrium", "Y", 39, 88.906,"Rare-earth element ignites easily in air, and\nhas been found in rocks retrieved from the moon."))
    x.append(Element("Zirconium", "Zr", 40, 91.224, "Used in ultra-strong ceramics."))
    x.append(Element("Niobium", "Nb", 41, 92.906, "Used in alloys including stainless steel.\nIt improves the strength of the alloys."))
    x.append(Element("Molybdenum", "Mo", 42, 95.95, "silvery-white metal that is ductile and\nhighly resistant to corrosion."))
    x.append(Element("Technetium", "Tc", 43, 98.907, "If you spent all day wearing it as a hat\nor breathed it in as dust it could definitely kill you."))
    x.append(Element("Ruthenium", "Ru", 44, 101.07, "Ruthenium compounds are similar to those\nformed by the element cadmium."))
    x.append(Element("Rhodium", "Rh", 45, 102.906, "Silver-white metallic element that is\nhighly reflective and resistant to corrosion."))
    x.append(Element("Palladium", "Pd", 46, 106.42, "The largest use of palladium today is in catalytic converters."))
    x.append(Element("Silver", "Ag", 47, 107.868, "Silver was used a lot in currency."))
    x.append(Element("Cadmium", "Cd", 48, 112.411, "The bluish-white metal that is known as cadmium\nis malleable, ductile and can easily be cut with a knife."))
    x.append(Element("Indium", "In", 49, 114.818, "Indium metal remains unusually soft and malleable\nat very low temperatures"))
    x.append(Element("Tin", "Sn", 50, 118.711, "Bronze typically consists of 88% copper and 12% tin."))
    x.append(Element("Antimony", "Sb", 51, 121.760, "Used in ancient Egypt as a form of eyeliner"))
    x.append(Element("Tellurium", "Te", 52, 127.6, "Is a metalloid, meaning it possesses the properties\nof both metals and nonmetals."))
    x.append(Element("Iodine", "I", 53, 126.904, "We get most of our iodine from milk."))
    x.append(Element("Xenon", "Xe", 54, 131.294, "Pronounced as ZEE-non this element is a gas primarily\nused in light manufacturing"))
    x.append(Element("Cesium", "Cs", 55, 132.905, "use for caesium compounds is as a drilling fluid."))
    x.append(Element("Barium", "Ba", 56, 137.328, "Its name comes from the Greek word meaning heavy."))
    x.append(Element("Lanthanum", "La", 57, 138.905, "Lanthanum is a metal so soft it can be cut with a butter knife."))
    x.append(Element("Cerium", "Ce", 58, 140.116, "Component of mischmetal, used in the manufacture\nof alloys for cigarette lighters"))
    x.append(Element("Praseodymium", "Pr", 59, 140.908, "Used in a variety of alloys."))
    x.append(Element("Neodymium", "Nd", 60, 144.242, "Used with iron and boron to create powerful permanent magnets"))
    x.append(Element("Promethium", "Pm", 61, 144.913, "Most promethium is used for research purpose."))
    x.append(Element("Samarium", "Sm", 62, 150.36, "It is the hardest and the most brittle of the rare earth elements."))
    x.append(Element("Europium", "Eu", 63, 151.964, "It is the most reactive of the rare earth metals\nand ignites in air at temperatures in excess of 150 oC to 180 oC. "))
    x.append(Element("Gadolinium", "Gd", 64, 157.25, "Possesses unusual metallurgic properties."))
    x.append(Element("Terbium", "Tb", 65, 158.925, "Used to dope calcium fluoride, calcium tungstate\nand strontium molybdate, all used in solid-state devices."))
    x.append(Element("Dysprosium", "Dy", 66, 162.500, "Its compounds have been used for making laser materials\nand phosphor activators, and in metal halide lamps."))
    x.append(Element("Holmium", "Ho", 67, 164.930, "It does not react in dry air at normal temperatures"))
    x.append(Element("Erbium", "Er", 68, 167.259, "Erbium metal is fairly stable in air and\ndoes not oxidize as rapidly as some of the other rare-earth metals"))
    x.append(Element("Thulium", "Tm", 69, 168.934, "Has been used to create lasers."))
    x.append(Element("Ytterbium", "Yb", 70, 173.055, "Uses of ytterbium include use as a radiation source for x-ray machines."))
    x.append(Element("Lutetium", "Lu", 71, 174.967, "Lutetium is the hardest lanthanide element."))
    x.append(Element("Hafnium", "Hf", 72, 178.49, "Is a good absorber of neutrons and is used to make control rods"))
    x.append(Element("Tantalum", "Ta", 73, 180.948, "Very resistant to corrosion attack."))
    x.append(Element("Tungsten", "W", 74, 183.84, "Known as one of the toughest things found in nature."))
    x.append(Element("Rhenium", "Re", 75, 186.207, "Used for oven filaments and x-ray machines"))
    x.append(Element("Osmium", "Os", 76, 190.23, "Is the rarest of all stable elements."))
    x.append(Element("Iridium", "Ir", 77, 192.217, "It has a very high density and melting point."))
    x.append(Element("Platinum", "Pt", 78, 195.085, "Used in catalytic converters"))
    x.append(Element("Gold", "Au", 79, 196.967, "is extremely ductile."))
    x.append(Element("Mercury", "Hg", 80, 200.592, "It can be extremely poisonous to humans."))
    x.append(Element("Thallium", "TI", 81, 204.383, "It has a low melting point and will tarnish in air to a bluish-gray oxide."))
    x.append(Element("Lead", "Pb", 82, 207.2, "Lead is a considered a basic metal or post-transition metal."))
    x.append(Element("Bismuth", "Bi", 83, 208.980, "Bismuth metal is brittle and so it is usually mixed\nwith other metals to make it useful."))
    x.append(Element("Polonium", "Po", 84, 208.982, "Very rare and highly volatile radioactive metal."))
    x.append(Element("Astatine", "At", 85, 209.987, "Radioactive, unstable."))
    x.append(Element("Radon", "Rn", 86, 222.018, "Causes cancer. Breathing radon can increase your\nrisk of developing lung cancer." ))
    x.append(Element("Francium", "Fr", 87, 223.020, "A heavy, unstable, radioactive metal with\na maximum half-life of only 22 minutes."))
    x.append(Element("Radium", "Ra", 88, 226.025, "The heaviest alkaline earth metal"))
    x.append(Element("Actinium", "Ac", 89, 227.028, "It is about 150 times as radioactive as radium."))
    x.append(Element("Thorium", "Th", 90, 232.038, "Thorium is radioactive. It collects in living animal bones,\nincluding human bone, where it can remain for a long period of time."))
    x.append(Element("Protactinium", "Pa", 91, 231.036, "The existence of protactinium was predicted in 1871 by Dmitri Mendeleev."))
    x.append(Element("Uranium", "U", 92, 238.029, "Pure uranium is a silvery-white metal."))
    x.append(Element("Neptunium", "Np", 93, 237.048, "It has no stable isotopes."))
    x.append(Element("Plutonium", "Pu", 94, 244.064, "Plutonium is not a good conductor of electricity\nor heat, unlike some metals."))
    x.append(Element("Americium", "Am", 95, 243.061, "It is used in smoke detectors and can be\nused as a portable source of gamma rays."))
    x.append(Element("Curium", "Cm", 96, 247.070, "It tarnishes slowly in dry air at room temperature."))
    x.append(Element("Berkelium", "Bk", 97, 247.070, "It was used for the atmospheric nuclear\nweapons tests between 1945 and 1980."))
    x.append(Element("Californium", "Cf", 98, 251.080, "Californium is a very strong neutron emitter."))
    x.append(Element("Einsteinium", "Es", 99, 254, "The main use of einsteinium is to create heavier elements,\nincluding mendelevium."))
    x.append(Element("Fermium", "Fm", 100, 257.095, "Fermium has no known biological role.\nIt is toxic due to its radioactivity."))
    x.append(Element("Mendelevium", "Md", 101, 258.1, " Mendelevium is used only for research.\nMendelevium has no known biological role."))
    x.append(Element("Nobelium", "No", 102, 259.101, "Nobelium is made by bombarding curium with\ncarbon in a device called a cyclotron."))
    x.append(Element("Lawrencium", "Lr", 103, 262, "Its only use is for research within a laboratory.\nMost actinides are used for their radioactive properties."))
    x.append(Element("Rutherfordium", "Rf", 104, 261, "The first transactinide or super-heavy element to be discovered."))
    x.append(Element("Dubnium", "Db", 105, 262, "A highly radioactive metal, of which only a few atoms\nhave ever been made."))
    x.append(Element("Seaborgium", "Sg", 106, 266, "It decays into rutherfordium-267 through alpha decay\nor decays through spontaneous fission."))
    x.append(Element("Bohrium", "Bh", 107, 264, "There are currently no uses for bohrium outside\nof basic scientific research."))
    x.append(Element("Hassium", "Hs", 108, 269, "At present it is only used in research.\nHassium has no known biological role."))
    x.append(Element("Meitnerium", "Mt", 109, 268, "There are no real uses for meitnerium, except in research."))
    x.append(Element("Darmstadtium", "Ds", 110, 269, "Darmstadtium has no known biological role."))
    x.append(Element("Roentgenium", "Rg", 111, 272, "The only uses of roentgenium are for scientific study."))
    x.append(Element("Copernicium", "Cn", 112, 277, "Tt is only used in research. It has no known biological role."))
    x.append(Element("Ununtrium", "Uut", 113, "unknown", "Ununtrium is classified as a metal and is expected\nto be solid at room temperature."))
    x.append(Element("Flerovium", "FI", 114, 289, "Is a superheavy artificial chemical element with the\nsymbol Fl and atomic number 114"))
    x.append(Element("Ununpentium", "Uup", 115, "unknown", "They are only used for the purpose of scientific\nstudy and research."))
    x.append(Element("Livermorium", "Lv", 116, 298, "it is only used in research. It has no known\nbiological role."))
    x.append(Element("Ununseptium", "Uus", 117, 277, "Is a synthetic radioactive metal and has only been\nproduced in minute amounts."))
    x.append(Element("Ununoctium", "Uuo", 118, "unknown", "They are only used for the purpose of\nscientific study and research."))
    return x

def SearchTable(name, symbol, number, weight, yes):
    r = []
    x = AllElements()
    if (name != None):
        name = name.capitalize()
        for i in (x):
            if i.ElementName == name:
                r.append(i)
    elif (symbol != None):
        symbol = symbol.capitalize()
        for i in (x):
            if i.ElementSymbol == symbol:
                r.append(i)
    elif (number != None):
        if (number.isdigit()):
            number = int(number)
            for i in (x):
                if i.AtomicNumber == number:
                    r.append(i)
    elif (weight != None):
        for i in (x):
            if i.AtomicWeight == weight:
                r.append(i)
    elif (yes != None):
        for i in (x):
            if Ayes == yes:
                r.append(i)
    return r

if __name__ == "__main__":
    GroupTen = Window()
    GroupTen.mainloop()
