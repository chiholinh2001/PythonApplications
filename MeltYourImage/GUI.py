from tkinter import *
from PIL import ImageTk, Image
import customtkinter
import os

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    WIDTH = 1200
    HEIGHT = 600
    PATH = os.path.dirname(os.path.realpath(__file__))
    NAME = "Melt Your Image"
    # ==========================================================================================
    # ========================================= SETUP ==========================================
    # ==========================================================================================
    def __init__(self):
        super().__init__()

        # ------------------------------------------------------------------------------------------
        # -------------------------------------- MAIN WINDOW ---------------------------------------
        # ------------------------------------------------------------------------------------------


        self.title(App.NAME)
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.minsize(App.WIDTH, App.HEIGHT)
        self.maxsize(App.WIDTH, App.HEIGHT)
        self.resizable(False, False)
        self.iconbitmap(self.PATH + "\icons\iconWindow.ico")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed


        # ------------------------------------------------------------------------------------------
        # ------------------------------------- SEPERATE FRAME -------------------------------------
        # ------------------------------------------------------------------------------------------

        #================== MAIN layout (2x1) ==================
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe")


        # ================== LEFT layout (1x8) ==================
        self.frame_left.grid_columnconfigure(0, weight=1)
        self.frame_left.grid_rowconfigure(6, weight=1)

        # ================== RIGHT layout (2x2) ==================
        self.frame_right.columnconfigure(0, weight=1)
        self.frame_right.rowconfigure(0, weight=1)

        # ------------------ RIGHT-image layout (1x2) ------------------
        self.frame_image = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_image.grid(row=0, column=0, pady=5, padx=5, sticky="nsew")
        self.frame_image.columnconfigure(0, weight=1)
        self.frame_image.rowconfigure(0, weight=1)

        # ------------------ RIGHT-tool layout (1x1) ------------------
        self.frame_tool = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_tool.grid(row=1, column=0, pady=5, padx=5, sticky="nsew")
        self.frame_tool.columnconfigure(0, weight=1)
        self.frame_tool.rowconfigure(0, weight=1)

        # ------------------ RIGHT-process layout (1x2) ------------------
        self.frame_process = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_process.grid(row=0, column=1, rowspan=2, pady=5, padx=5, sticky="nsew")
        self.frame_image.columnconfigure(0, weight=1)
        self.frame_process.rowconfigure(7, weight=1)

        self.frame_process_1 = customtkinter.CTkFrame(master=self.frame_process)
        self.frame_process_1.grid(row=3, column=0, columnspan=2, rowspan=2, pady=5, padx=5, sticky="nsew")

        self.frame_process_2 = customtkinter.CTkFrame(master=self.frame_process)
        self.frame_process_2.grid(row=5, column=0, columnspan=2, rowspan=2, pady=5, padx=5, sticky="nsew")

        # ------------------------------------------------------------------------------------------
        # -------------------------------------- DESIGN FRAME --------------------------------------
        # ------------------------------------------------------------------------------------------


        # ================== FRAME_LEFT ==================

        self.logo_image = ImageTk.PhotoImage(Image.open("icons\iconWindow.ico"))
        self.label_logo_image = customtkinter.CTkLabel(self.frame_left, image=self.logo_image)
        self.label_logo_image.grid(row=0, pady=20, padx=10, sticky="nsew")

        self.nameProgram = customtkinter.CTkLabel(master=self.frame_left,
                                                  text=App.NAME,
                                                  text_font=("Roboto Medium", 15))  # font name and size in px
        self.nameProgram.grid(row=1, pady=10, padx=10, sticky="n")

        self.button_open = customtkinter.CTkButton(master=self.frame_left,
                                                text="Open Image",
                                                command=self.button_event)
        self.button_open.grid(row=2, pady=10, padx=20)

        self.button_save = customtkinter.CTkButton(master=self.frame_left,
                                                text="Save Image",
                                                command=self.button_event)
        self.button_save.grid(row=3, pady=10, padx=20)

        self.button_guide = customtkinter.CTkButton(master=self.frame_left,
                                                text="Guide",
                                                command=self.button_event)
        self.button_guide.grid(row=4, pady=10, padx=20)

        self.button_info = customtkinter.CTkButton(master=self.frame_left,
                                                text="Info",
                                                command=self.button_event)
        self.button_info.grid(row=5, pady=10, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=7, pady=0, padx=20, sticky="s")

        self.optionmenu_appearance_mode = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_appearance_mode.grid(row=8, pady=10, padx=20, sticky="s")


        # ================== FRAME_RIGHT ==================

        # ------------------ frame_image ------------------
        self.display_image = ImageTk.PhotoImage(Image.open("images\image2.jpg"))
        self.label_image = customtkinter.CTkLabel(self.frame_image, image=self.display_image)
        self.label_image.grid(row=0, sticky="nsew", padx=5, pady=5)

        self.slider_1 = customtkinter.CTkSlider(master=self.frame_image,
                                                from_=0,
                                                to=1,
                                                number_of_steps=10)
        self.slider_1.grid(row=1, pady=5, padx=5, sticky="we")

        # ------------------ frame_tool ------------------
        Label(self.frame_tool, text="heloo").grid(row=0, column=0)

        # ------------------ frame_process ------------------
        self.label_process = customtkinter.CTkLabel(master=self.frame_process,
                                                        text="Image Compression",
                                                        text_font=("Roboto Medium", 12))
        self.label_process.grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky="n")

        self.radio_var = IntVar(value=0)
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_process,
                                                           variable=self.radio_var,
                                                           text="Gray Image",
                                                           value=0)
        self.radio_button_1.grid(row=1, column=0, columnspan=2, pady=10, padx=10, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_process,
                                                           variable=self.radio_var,
                                                           text="Color Image",
                                                           value=1)
        self.radio_button_2.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="n")

        self.button_process = customtkinter.CTkButton(master=self.frame_process_1,
                                                      text="Process Image",
                                                      command=self.button_event,
                                                      )
        self.button_process.grid(row=0, column=0, columnspan=2, pady=10, padx=20)

        self.label_maxrank = customtkinter.CTkLabel(master=self.frame_process_1,
                                                        text="Max Rank: ")
        self.label_maxrank.grid(row=1, column=0, columnspan=2, pady=5, padx=15, sticky='w')


        self.entry = customtkinter.CTkEntry(master=self.frame_process_2,
                                            width=80)
        self.entry.grid(row=0, column=0, columnspan=1, pady=10, padx=5, sticky="w")

        self.combobox_1 = customtkinter.CTkComboBox(master=self.frame_process_2,
                                                    width=80,
                                                    values=["Rank", "%"])
        self.combobox_1.grid(row=0, column=1, columnspan=1, pady=10, padx=5, sticky="e")

        self.button_compress = customtkinter.CTkButton(master=self.frame_process_2,
                                                      text="Compress Image",
                                                      command=self.button_event)
        self.button_compress.grid(row=1, column=0, columnspan=2, pady=10, padx=20)



        # self.switch_1 = customtkinter.CTkSwitch(master=self.frame_right,
        #                                         text="CTkSwitch")
        # self.switch_1.grid(row=4, column=2, columnspan=1, pady=10, padx=20, sticky="we")
        #
        # self.switch_2 = customtkinter.CTkSwitch(master=self.frame_right,
        #                                         text="CTkSwitch")
        # self.switch_2.grid(row=5, column=2, columnspan=1, pady=10, padx=20, sticky="we")



        # self.check_box_1 = customtkinter.CTkCheckBox(master=self.frame_right,
        #                                              text="CTkCheckBox")
        # self.check_box_1.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        #
        # self.check_box_2 = customtkinter.CTkCheckBox(master=self.frame_right,
        #                                              text="CTkCheckBox")
        # self.check_box_2.grid(row=6, column=1, pady=10, padx=20, sticky="w")



        self.button_exit = customtkinter.CTkButton(master=self.frame_process,
                                                   text="Exit",
                                                   border_width=2,  # <- custom border_width
                                                   fg_color=None,  # <- no fg_color
                                                   command=self.button_event)
        self.button_exit.grid(row=8, column=0, columnspan=2, pady=10, padx=10, sticky="we")


        # ------------------------------------------------------------------------------------------
        # ----------------------------------- SET DEFAULT VALUES -----------------------------------
        # ------------------------------------------------------------------------------------------
        self.optionmenu_appearance_mode.set("Dark")
        # self.button_3.configure(state="disabled", text="Disabled CTkButton")
        # self.combobox_1.set("CTkCombobox")
        # self.radio_button_1.select()
        # self.slider_1.set(0.2)
        # self.slider_2.set(0.7)
        # self.progressbar.set(0.5)
        # self.switch_2.select()
        # self.radio_button_3.configure(state=DISABLED)
        # self.check_box_1.configure(state=DISABLED, text="CheckBox disabled")
        # self.check_box_2.select()

    # ==========================================================================================
    # ======================================== FUNCTIONS =======================================
    # ==========================================================================================

    def button_event(self):
        print("Button pressed")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()

############## MAIN ##############
if __name__ == "__main__":
    app = App()
    app.mainloop()
