from tkinter import *
import customtkinter
from customtkinter import *
import tkintermapview
from PIL import ImageTk, Image
import os

root = CTk()

customtkinter.set_appearance_mode('light')
root.geometry('1080x1920')
root.resizable(width=False, height=False)
my_label=LabelFrame(root)
my_label.pack(side=RIGHT,pady=20)


map_widget = tkintermapview.TkinterMapView(my_label, width=1080, height=1080) #wymiary mapy




#pinezki schronisk woj pomorskie
marker_1 = map_widget.set_marker(54.453360, 18.540189,
                                 text="Schronisko Sopotkowo",
                                 marker_color_circle='#8f1318',
                                 marker_color_outside='#EA0B15')

marker_2 = map_widget.set_marker(54.375374, 18.449175,
                                 text="Schronisko Promyk",
                                 marker_color_circle='#8f1318',
                                 marker_color_outside='#EA0B15')

marker_3 = map_widget.set_marker(53.721950, 17.574248,
                                 text="Schronisko Przytulisko",
                                 marker_color_circle='#8f1318',
                                 marker_color_outside='#EA0B15')

marker_4= map_widget.set_marker(54.562768, 18.175170,
                                text="Schronisko OTOZ Animals w Dąbrówce",
                                marker_color_circle='#8f1318',
                                marker_color_outside='#EA0B15')

marker_5 = map_widget.set_marker(54.184247, 19.447635,
                                 text="Schronisko Animals",
                                 marker_color_circle='#8f1318',
                                 marker_color_outside='#EA0B15')

marker_6= map_widget.set_marker(54.492701, 18.528024,
                                text="Schronisko Ciapkowo",
                                marker_color_circle='#8f1318',
                                marker_color_outside='#EA0B15')

marker_7= map_widget.set_marker(54.502217, 17.729414,
                                text="Schronisko w Małoszycach",
                                marker_color_circle='#8f1318',
                                marker_color_outside='#EA0B15')

marker_8=map_widget.set_marker(54.489319, 17.034188,
                               text="Schronisko w Słupsku",
                               marker_color_circle='#8f1318',
                               marker_color_outside='#EA0B15')

marker_9=map_widget.set_marker(53.948367, 18.540194,
                               text="Schronisko OTOZ Animals w Starogardzie Gdańskim",
                               marker_color_circle='#8f1318',
                               marker_color_outside='#EA0B15')

marker_10=map_widget.set_marker(54.109158, 18.781509,
                                text="Schronisko OTOZ Animals w Tczewie",
                                marker_color_circle='#8f1318',
                                marker_color_outside='#EA0B15')
def submit():
    # get text from "prob" CTkEntry object
    prob_text = prob.get()
    # set nice display text for the new marker by joining "Problem: " with prob_text
    marker_text = "Problem: " + prob_text
    # set marker_text as a display text for the new_marker marker
    # we can reference new_marker variable here, because new_marker variable was declaerd as global in add_marker_event() function
    new_marker.set_text(marker_text)
#funkcja dodawania pinezek
def add_marker_event(coords):
    global new_marker
    zgl.place(relx=0.5, rely=0.099, anchor='n')
    prob.place(relx=0.5, rely=0.14, anchor='n')
    my_button.place(relx=0.5, rely=0.2, anchor='n')

    new_marker = map_widget.set_marker(coords[0],
                                       coords[1],
                                       text=''.center(10))

    zwierz.place(relx=0.5, rely=0.17, anchor='n')


map_widget.add_right_click_menu_command(label="Dodaj pinezkę",
                                        command=add_marker_event,
                                        pass_coords=True)
def submit():
    # get text from "prob" CTkEntry object
    prob_text = prob.get()
    zwierz_text=zwierz.get()
    # set nice display text for the new marker by joining "Problem: " with prob_text
    marker_text = "Problem: " + prob_text + '\n Zwierzę: ' + zwierz_text
    # set marker_text as a display text for the new_marker marker
    # we can reference new_marker variable here, because new_marker variable was declaerd as global in add_marker_event() function
    new_marker.set_text(marker_text)


#entry frame help info
prob = customtkinter.CTkEntry(master=root,
                              placeholder_text='Jaka pomoc jest potrzebna?..',
                              width=300,
                              text_color='black')

#submit button
my_button = customtkinter.CTkButton(master=root,
                                    text="Submit",
                                    command=submit,
                                    fg_color='#EA0B15',
                                    hover_color='#8f1318')

#title of report
zgl = customtkinter.CTkLabel(master=root,
                             text='DODAWANIE ZGLOSZENIA',
                             font=('Broadway', 40),
                             text_color='black', )

#entry frame pet info
zwierz = customtkinter.CTkEntry(master=root,
                                placeholder_text='Jakie zwierzę?..',
                                width=300,
                                text_color='black')

#heading
heading_image= os.path.join(os.path.dirname(__file__),
                            'pinpetheading.png')
h_image=customtkinter.CTkImage(light_image=Image.open(heading_image),
                               size=(1080, 150))
img_label=customtkinter.CTkLabel(root,
                                 image=h_image)
img_label.place(x=0.15,
                y=0.1)





map_widget.set_position(54.372158, 18.638306) #pozycja "startowa" aplikacji na mapie
map_widget.set_zoom(12)


map_widget.pack(side= BOTTOM)


root.mainloop()