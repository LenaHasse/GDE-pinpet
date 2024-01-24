from tkinter import *
import customtkinter
from customtkinter import *
import tkintermapview

root = CTk()


root.geometry('2160x1620') #wymiary aplikacji
my_label=LabelFrame(root)
my_label.pack(side=RIGHT,pady=20)

map_widget = tkintermapview.TkinterMapView(my_label, width=1750, height=1620) #wymiary mapy


#pinezki schronisk woj pomorskie
marker_1 = map_widget.set_marker(54.453360, 18.540189, text="Schronisko Sopotkowo", marker_color_circle='dark blue', marker_color_outside='blue')

marker_2 = map_widget.set_marker(54.375374, 18.449175, text="Schronisko Promyk", marker_color_circle='dark blue', marker_color_outside='blue')

marker_3 = map_widget.set_marker(53.721950, 17.574248, text="Schronisko Przytulisko", marker_color_circle='dark blue', marker_color_outside='blue')

marker_4= map_widget.set_marker(54.562768, 18.175170, text="Schronisko OTOZ Animals w Dąbrówce", marker_color_circle='dark blue', marker_color_outside='blue')

marker_5 = map_widget.set_marker(54.184247, 19.447635, text="Schronisko Animals", marker_color_circle='dark blue', marker_color_outside='blue')

marker_6= map_widget.set_marker(54.492701, 18.528024, text="Schronisko Ciapkowo", marker_color_circle='dark blue', marker_color_outside='blue')

marker_7= map_widget.set_marker(54.502217, 17.729414, text="Schronisko w Małoszycach", marker_color_circle='dark blue', marker_color_outside='blue')

marker_8=map_widget.set_marker(54.489319, 17.034188, text="Schronisko w Słupsku", marker_color_circle='dark blue', marker_color_outside='blue')

marker_9=map_widget.set_marker(53.948367, 18.540194, text="Schronisko OTOZ Animals w Starogardzie Gdańskim", marker_color_circle='dark blue', marker_color_outside='blue')

marker_10=map_widget.set_marker(54.109158, 18.781509, text="Schronisko OTOZ Animals w Tczewie", marker_color_circle='dark blue', marker_color_outside='blue')





#funkcja dodawania pinezek
def add_marker_event(coords):
    zgl = customtkinter.CTkLabel(master=root, text='DODAWANIE ZGLOSZENIA', font=('Broadway', 25), text_color='#FFFFFF', )
    zgl.place(relx=0.093, rely=0.09, anchor='n')
    prob = customtkinter.CTkEntry(master=root, placeholder_text='Jaka pomoc jest potrzebna?..', width=300, text_color='#FFFFFF')
    prob.place(relx=0.095, rely=0.15, anchor='n')
    new_marker = map_widget.set_marker(coords[0], coords[1], text="nowa pinezka".center(10))
    zwierz = customtkinter.CTkEntry(master=root, placeholder_text='Jakie zwierzę?..', width=300, text_color='#FFFFFF')
    zwierz.place(relx=0.095, rely=0.2, anchor='n')
    #new_marker.set_text(final)


btnpin=CTkButton(master=root, text="Dodaj pinezke", corner_radius=32, fg_color='#E80D15', hover_color='#730509', command=add_marker_event) #przycisk do uruchomienia dodawania pinezki o zgloszeniu
#btnpin.place(relx=0.09, rely=0.5, anchor='n')

map_widget.add_right_click_menu_command(label="Dodaj pinezkę",
                                        command=add_marker_event,
                                        pass_coords=True)





map_widget.set_position(54.372158, 18.638306) #pozycja "startowa" aplikacji na mapie
map_widget.set_zoom(12)


map_widget.pack()

root.mainloop()