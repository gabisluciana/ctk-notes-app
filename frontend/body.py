import customtkinter as ctk


class MainWindow(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.title = ctk.CTkEntry(self, fg_color="transparent", border_width=0, font=self.winfo_toplevel().title_font)
        self.title.grid(column=0, row=0, padx=(0, 5), pady=5, sticky="ew")

        self.body = ctk.CTkTextbox(
            self, fg_color="transparent", font=self.winfo_toplevel().body_font, wrap="word", activate_scrollbars=False
        )
        self.body.grid(column=0, row=1, sticky="nsew", columnspan=2)
