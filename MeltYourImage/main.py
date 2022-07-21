from tkinter import *
from tkinter import filedialog, messagebox

import PIL.JpegImagePlugin
from PIL import ImageTk, Image, ImageOps
import customtkinter
import os
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

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
        self.frame_left.grid_rowconfigure(7, weight=1)

        # ================== RIGHT layout (2x2) ==================
        self.frame_right.columnconfigure(0, weight=1)
        self.frame_right.rowconfigure(0, weight=1)

        # ------------------ RIGHT-image layout (1x2) ------------------
        self.frame_image = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_image.grid(row=0, column=0, pady=5, padx=5, sticky="nsew")
        self.frame_image.columnconfigure(0, weight=1)
        self.frame_image.rowconfigure(0, weight=1)

        # ------------------ RIGHT-process layout (1x2) ------------------
        self.frame_process = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_process.grid(row=0, column=1, pady=5, padx=5, sticky="nsew")
        self.frame_image.columnconfigure(0, weight=1)
        self.frame_process.rowconfigure(8, weight=1)

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
                                                command=self.open_image)
        self.button_open.grid(row=2, pady=10, padx=20)

        self.button_save = customtkinter.CTkButton(master=self.frame_left,
                                                text="Save Image",
                                                command=self.save_image)
        self.button_save.grid(row=3, pady=10, padx=20)

        self.button_save_as = customtkinter.CTkButton(master=self.frame_left,
                                                   text="Save As Image",
                                                   command=self.save_as_image)
        self.button_save_as.grid(row=4, pady=10, padx=20)

        self.button_guide = customtkinter.CTkButton(master=self.frame_left,
                                                text="Guide",
                                                command=self.button_event)
        self.button_guide.grid(row=5, pady=10, padx=20)

        self.button_info = customtkinter.CTkButton(master=self.frame_left,
                                                text="Info",
                                                command=self.button_event)
        self.button_info.grid(row=6, pady=10, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=7, pady=0, padx=20, sticky="s")

        self.optionmenu_appearance_mode = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_appearance_mode.grid(row=8, pady=10, padx=20, sticky="s")


        # ================== FRAME_RIGHT ==================

        # ------------------ frame_image ------------------
        self.default_image = ImageTk.PhotoImage(Image.open("images\default.jpg"))
        self.label_image = customtkinter.CTkLabel(self.frame_image, image=self.default_image)
        self.label_image.grid(row=0, sticky="nsew", padx=5, pady=5)

        self.label_error = customtkinter.CTkLabel(master=self.frame_image,
                                                 text="")
        self.label_error.grid(row=1, sticky="nsew", pady=5, padx=5)

        # ------------------ frame_process ------------------
        self.label_process = customtkinter.CTkLabel(master=self.frame_process,
                                                        text="Image Compression",
                                                        text_font=("Roboto Medium", 12))
        self.label_process.grid(row=0, pady=10, padx=10, sticky="n")

        self.radio_var = IntVar(value=0)
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_process,
                                                           variable=self.radio_var,
                                                           text="Gray Image",
                                                           value=0)
        self.radio_button_1.grid(row=1, pady=10, padx=10, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_process,
                                                           variable=self.radio_var,
                                                           text="Color Image",
                                                           value=1)
        self.radio_button_2.grid(row=2, pady=10, padx=10, sticky="n")

        self.button_process = customtkinter.CTkButton(master=self.frame_process_1,
                                                      text="Process Image",
                                                      command=self.process_image,
                                                      )
        self.button_process.grid(row=0, pady=10, padx=20)

        self.label_max_rank = customtkinter.CTkLabel(master=self.frame_process_1,
                                                        text="Max Rank: ")
        self.label_max_rank.grid(row=1, pady=5, padx=15, sticky='w')

        self.label_rank = customtkinter.CTkLabel(master=self.frame_process_2,
                                                 text="Approximate Matrix' s Rank")
        self.label_rank.grid(row=0, pady=5, padx=5)

        self.entry_rank = customtkinter.CTkEntry(master=self.frame_process_2,
                                            width=100)
        self.entry_rank.grid(row=1, pady=5, padx=5)


        self.button_compress = customtkinter.CTkButton(master=self.frame_process_2,
                                                      text="Compress Image",
                                                      command=self.compress_image)
        self.button_compress.grid(row=2, pady=10, padx=20)

        self.button_exit = customtkinter.CTkButton(master=self.frame_process,
                                                   text="Exit",
                                                   border_width=2,
                                                   fg_color=None,
                                                   command=self.quit)
        self.button_exit.grid(row=9, pady=10, padx=10, sticky="we")


        # ------------------------------------------------------------------------------------------
        # ----------------------------------- SET DEFAULT VALUES -----------------------------------
        # ------------------------------------------------------------------------------------------
        self.optionmenu_appearance_mode.set("Dark")
        self.radio_button_1.select()
        self.button_save.configure(state="disabled")
        self.button_save_as.configure(state="disabled")
        self.button_process.configure(state="disabled")
        self.button_compress.configure(state="disabled")

    # ==========================================================================================
    # ======================================= FUNCTIONS ========================================
    # ==========================================================================================

    # ================== OPEN-SAVE FILE ==================
    def open_image(self):
        '''
            Get image path from user
            Arguments:
                None
            Returns:
                None
        '''
        try:
            self.image_path = filedialog.askopenfilename(initialdir="\\", title="Open", filetypes=(
            ("Image files", "*.jpg"), ("Image files", "*.png"), ("Image files", "*.jpeg"), ("All files", "*.*")))
            if self.image_path:
                self.image = Image.open(self.image_path)
                self.display_image = ImageTk.PhotoImage(self.image)
                self.label_image = customtkinter.CTkLabel(self.frame_image, image=self.display_image)
                self.label_image.grid(row=0, sticky="nsew", padx=5, pady=5)
        except Exception as e:
            Label(self, text=messagebox.showerror("Cannot open the file", "Please select image file!"))
        #Update status bar
        list_name = self.image_path.split("/")
        self.title(self.NAME + " - " + list_name[-1])
        self.button_save.configure(state="enabled")
        self.button_save_as.configure(state="enabled")
        self.button_process.configure(state="enabled")

        self.edited_image = self.image
        self.label_max_rank.configure(text="Max Rank: ")
        self.entry_rank.delete(0, 'end')
        self.label_error.configure(text="")


    def save_image(self):
        '''
            Save image file
            Arguments:
                None
            Returns:
                None
        '''
        try:
            self.edited_image.save(self.image_path)
            Label(self, text=messagebox.showinfo("Saved", "Save successfully!"))
        except Exception as e:
            Label(self, text=messagebox.showerror("Cannot save the file", "Please try again!"))

    def save_as_image(self):
        '''
            Save image file
            Arguments:
                None
            Returns:
                None
        '''
        try:
            output_path = filedialog.asksaveasfilename(defaultextension=".jpg", initialdir="\\", title="Save As", filetypes=(
            ("JPG files", "*.jpg"), ("PNG files", "*.png"), ("JPEG files", "*.jpeg"), ("All files", "*.*")))
            if output_path:
                self.edited_image.save(output_path)
                Label(self, text=messagebox.showinfo("Saved", "Save successfully!"))
                #Update status bar
                list_name = output_path.split("/")
                self.title(self.NAME + " - " + list_name[-1])
        except Exception as e:
            Label(self, text=messagebox.showerror("Cannot save the file", "Please try again!"))
        self.image_path = output_path

    # ================== PROCESS IMAGE ==================
    def process_image(self):
        #Check mode to process
        self.mode_process = self.radio_var.get()
        if self.mode_process == 0:
            self.process_gray_image()
        else:
            self.process_color_image()
        self.button_compress.configure(state="enabled")

    def process_gray_image(self):
        self.gray_image = self.edited_image.convert('L')
        self.gray_image = np.array(self.gray_image)
        self.gray_image = self.gray_image / 255.
        U, sigma, V_T = self.calculate_svd(self.gray_image)
        self.max_rank = la.matrix_rank(sigma)
        self.label_max_rank.configure(text="Max Rank: " + str(self.max_rank))


    def process_color_image(self):
        self.color_image = self.edited_image.convert('RGB')
        self.color_image = np.array(self.color_image)
        self.red_channel = self.color_image[:, :, 0] / 255.
        self.green_channel = self.color_image[:, :, 1] / 255.
        self.blue_channel = self.color_image[:, :, 2] / 255.
        self.max_rank = la.matrix_rank(self.blue_channel)
        self.label_max_rank.configure(text="Max Rank: " + str(self.max_rank))


    # ================== COMPRESS IMAGE ==================

    def compress_image(self):
        # Check mode to compress
        self.mode_compress = self.radio_var.get()
        if self.mode_compress != self.mode_process:
            Label(self, text=messagebox.showerror("Cannot compress the image", "The image you processed has a different mode than the one you want to compress.\nPlease try again!"))
        elif self.mode_compress == 0:
            self.compress_gray_image()
        else:
            self.compress_color_image()
        self.entry_rank.delete(0, 'end')

    def compress_gray_image(self):
        rank = self.entry_rank.get()
        if rank:
            rank = int(rank)
            if rank < 0:
                Label(self, text=messagebox.showerror("Cannot compress the image",
                                                      "Approximate Matrix' s Rank must be positive.\nPlease try again!"))
            elif rank > self.max_rank:
                Label(self, text=messagebox.showerror("Cannot compress the image",
                                                      "Approximate Matrix' s Rank must be equal or less than Max Rank.\nPlease try again!"))
            else:
                A_approx, error = self.find_A_approx(self.gray_image, rank)
                self.edited_image = Image.fromarray(A_approx * 255.)
                self.display_image = ImageTk.PhotoImage(self.edited_image)
                self.label_image.configure(image=self.display_image)
                self.label_error.configure(text='Error: ' + str(error))
                self.edited_image = self.edited_image.convert("L")
        else:
            Label(self, text=messagebox.showerror("Cannot compress the image",
                                                  "You've not entered Approximate Matrix' s Rank.\nPlease try again!"))


    def compress_color_image(self):
        rank = self.entry_rank.get()
        if rank:
            rank = int(rank)
            if rank < 0:
                Label(self, text=messagebox.showerror("Cannot compress the image",
                                                      "Approximate Matrix' s Rank must be positive.\nPlease try again!"))
            elif rank > self.max_rank:
                Label(self, text=messagebox.showerror("Cannot compress the image",
                                                      "Approximate Matrix' s Rank must be equal or less than Max Rank.\nPlease try again!"))
            else:
                self.red_compressed, er = self.find_A_approx(self.red_channel, rank)
                self.green_compressed, er = self.find_A_approx(self.green_channel, rank)
                self.blue_compressed, er = self.find_A_approx(self.blue_channel, rank)
                new_color_image = np.stack((self.red_compressed * 255., self.green_compressed * 255., self.blue_compressed * 255.), axis=2)
                self.edited_image = Image.fromarray(new_color_image.astype(np.uint8))
                self.display_image = ImageTk.PhotoImage(self.edited_image)
                self.label_image.configure(image=self.display_image)
                self.edited_image = self.edited_image.convert("RGB")
        else:
            Label(self, text=messagebox.showerror("Cannot compress the image",
                                                  "You've not entered Approximate Matrix' s Rank.\nPlease try again!"))

    def button_event(self):
        print()

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()

    ############################ SVD ALGORITHMS FUNCTIONS ############################
    def calculate_eigh_ATA(self, A):
        '''
            Calculate the eigenvalues and eigenvectors of matrix A^T.A
            Arguments:
                A: numpy array - the image
            Returns:
                eigenvalues: numpy array
                eigenvectors: numpy array
        '''
        ATA = np.dot(A.T, A)
        eigenvalues, eigenvectors = la.eigh(ATA)
        eigenvalues = np.maximum(eigenvalues, 0.)

        # Sort descending
        sorted_index = eigenvalues.argsort()[::-1]
        eigenvalues = eigenvalues[sorted_index]
        eigenvectors = eigenvectors[:, sorted_index]

        return eigenvalues, eigenvectors

    def calculate_svd(self, A):
        '''
            Using SVD to calculate U, sigma and V^T matrices of matrix A
            Arguments:
                A: numpy array - the image
            Returns:
                U: numpy array
                sigma: numpy array
                V_T: numpy array
        '''
        m = A.shape[0]
        n = A.shape[1]

        # Check to know calculate U or V^T first
        if m >= n:
            eigenvalues, eigenvectors = self.calculate_eigh_ATA(A.T)

            sigma = np.zeros([m, n])
            for i in range(min(m, n)):
                sigma[i][i] = max(eigenvalues[i], 0.)
            sigma = np.maximum(np.sqrt(sigma), 0)

            U = eigenvectors

            V = np.zeros([n, n])
            for i in range(n):
                V[:, i] = np.dot(A.T, U[:, i]) / sigma[i][i]
            V_T = V.T
        else:
            eigenvalues, eigenvectors = self.calculate_eigh_ATA(A)

            sigma = np.zeros([m, n])
            for i in range(min(m, n)):
                sigma[i][i] = max(eigenvalues[i], 0.)
            sigma = np.maximum(np.sqrt(sigma), 0)

            V = eigenvectors
            V_T = V.T

            U = np.zeros([m, m])
            for i in range(m):
                U[:, i] = np.dot(A, V[:, i]) / sigma[i][i]

        return U, sigma, V_T

    def find_A_approx(self, A, rank):
        '''
            Calculate the matrix A_approximately of A with rank using SVD
            Arguments:
                A: numpy array - the image
                rank: int - the rank of the approximate matrix,
                    the greater the rank is the more accuracy the approximate image is
            Returns:
                result: numpy array - the approximately image
                error: float - the error of the approximate image
        '''
        U, sigma, V_T = self.calculate_svd(A)
        # Approximate matrix with rank
        new_A = U[:, :rank] @ sigma[:rank, :rank] @ V_T[:rank, :]
        # Calculate error
        if rank < min(A.shape[0], A.shape[1]):
            error = np.sum(sigma[rank:, :]) / np.sum(sigma)
        else:
            error = 0.
        return new_A, error

############################ MAIN ############################
if __name__ == "__main__":
    app = App()
    app.mainloop()


