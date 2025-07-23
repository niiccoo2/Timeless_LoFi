# from make_music import *
# from play_music import *
# So there are less imports when testing ui ^^^

import customtkinter
from PIL import Image

class MainMenuFrame(customtkinter.CTkFrame):
    def __init__(self, master, switch_to_new_game, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        # Two columns: left for buttons, right for logo
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)  # left: buttons
        self.grid_columnconfigure(1, weight=1)  # right: logo

        # Left frame for buttons
        self.buttons_frame = customtkinter.CTkFrame(self)
        self.buttons_frame.grid(row=0, column=0, sticky="nsw", padx=20, pady=20)
        for i in range(5):
            self.buttons_frame.grid_rowconfigure(i, weight=1)
        self.buttons_frame.grid_columnconfigure(0, weight=1)

        self.resume = customtkinter.CTkButton(self.buttons_frame, text="Resume", command=lambda: print("Resume clicked"))
        self.resume.grid(row=0, column=0, sticky="ew", pady=5)

        self.new_game = customtkinter.CTkButton(self.buttons_frame, text="New Game", command=switch_to_new_game)
        self.new_game.grid(row=1, column=0, sticky="ew", pady=5)

        self.zen = customtkinter.CTkButton(self.buttons_frame, text="Zen Mode", command=lambda: print("Zen Mode clicked"))
        self.zen.grid(row=2, column=0, sticky="ew", pady=5)

        self.credits = customtkinter.CTkButton(self.buttons_frame, text="Credits", command=lambda: print("Credits clicked"))
        self.credits.grid(row=3, column=0, sticky="ew", pady=5)

        self.exit = customtkinter.CTkButton(self.buttons_frame, text="Exit", command=master.destroy)
        self.exit.grid(row=4, column=0, sticky="ew", pady=5)

        # Right frame for logo
        self.logo_frame = customtkinter.CTkFrame(self)
        self.logo_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.logo_frame.grid_rowconfigure(0, weight=1)
        self.logo_frame.grid_columnconfigure(0, weight=1)
        logo = customtkinter.CTkImage(light_image=Image.open("./logo.png"),
                                      dark_image=Image.open("./logo.png"),
                                      size=(400, 400))
        self.logo_label = customtkinter.CTkLabel(self.logo_frame, image=logo, text="")
        self.logo_label.image = logo
        self.logo_label.grid(row=0, column=0, sticky="")

class NewGameFrame(customtkinter.CTkFrame):
    def __init__(self, master, switch_to_main_menu, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.label = customtkinter.CTkLabel(self, text="New Game Screen")
        self.label.grid(row=0, column=0, sticky="nsew")
        self.back_button = customtkinter.CTkButton(self, text="Back to Menu", command=switch_to_main_menu)
        self.back_button.grid(row=1, column=0, pady=10)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1100x500")
        self.resizable(True, True)
        self.title('Timeless LoFi')

        self.logo = None
        self.logo_frame = None
        self.logo_label = None

        self.current_frame = None
        self.show_main_menu()

        self.bind("<Configure>", self.adjust_logo_size)

    def show_main_menu(self):
        # Set up 2-frame layout for main menu
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)

        # # Create and grid logo_frame if not already present
        # if self.logo_frame is None:
        #     self.logo = customtkinter.CTkImage(
        #         light_image=Image.open("./logo.png"),
        #         dark_image=Image.open("./logo.png"),
        #         size=(500, 500)
        #     )
        #     self.logo_frame = customtkinter.CTkFrame(self)
        #     self.logo_frame.grid(row=0, column=1, rowspan=5, sticky="nsew", padx=20, pady=20)
        #     self.logo_frame.grid_rowconfigure(0, weight=1)
        #     self.logo_frame.grid_columnconfigure(0, weight=1)
        #     self.logo_label = customtkinter.CTkLabel(self.logo_frame, image=self.logo, text="")
        #     self.logo_label.grid(row=0, column=0, sticky="")

        self._switch_frame(MainMenuFrame, switch_to_new_game=self.show_new_game)

    def show_new_game(self):
        # Remove logo_frame and use normal layout
        if self.logo_frame is not None:
            self.logo_frame.destroy()
            self.logo_frame = None
            self.logo_label = None
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
        self._switch_frame(NewGameFrame, switch_to_main_menu=self.show_main_menu)

    def _switch_frame(self, frame_class, **kwargs):
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = frame_class(self, **kwargs)
        # If logo_frame exists, use 2-frame layout, else normal
        if self.logo_frame is not None:
            self.current_frame.grid(row=0, column=0, rowspan=5, sticky="nsew", padx=20, pady=20)
        else:
            self.current_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    def adjust_logo_size(self, event=None):
        if self.logo_frame is None or self.logo_label is None:
            return
        logo_frame_width = self.logo_frame.winfo_width()
        logo_frame_height = self.logo_frame.winfo_height()
        new_size = min(logo_frame_width, logo_frame_height, 500)
        if new_size > 10:
            self.logo = customtkinter.CTkImage(
                light_image=Image.open("./logo.png"),
                dark_image=Image.open("./logo.png"),
                size=(new_size, new_size)
            )
            self.logo_label.configure(image=self.logo)

    def set_button_fonts(self, size):
        font_tuple = ("Helvetica", size)
        self.resume.configure(font=font_tuple)
        self.new_game.configure(font=font_tuple)
        self.zen.configure(font=font_tuple)
        self.credits.configure(font=font_tuple)
        self.exit.configure(font=font_tuple)

    def adjust_font_size(self, event=None):
        new_font_size = int((self.winfo_width() + self.winfo_height()) // 85)
        if new_font_size != self.current_font_size and new_font_size > 5:
            self.current_font_size = new_font_size
            self.set_button_fonts(new_font_size)


if __name__ == "__main__":
    app = App()
    app.mainloop()
