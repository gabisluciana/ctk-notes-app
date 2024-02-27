import customtkinter as ctk


class Sidebar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.rowconfigure(3, weight=1)
        self.new_note_btn = ctk.CTkButton(
            self,
            text="New Note",
            width=250,
            font=self.winfo_toplevel().button_font,
            command=self.winfo_toplevel().new_note,
        )
        self.new_note_btn.grid(column=0, row=0, padx=10, pady=5)

        self.save_note_btn = ctk.CTkButton(
            self,
            text="Save Note",
            width=250,
            fg_color="#307C39",
            hover_color="#245E2B",
            font=self.winfo_toplevel().button_font,
            command=self.winfo_toplevel().save_note,
        )
        self.save_note_btn.grid(column=0, row=1, padx=10, pady=5)

        self.delete_note_btn = ctk.CTkButton(
            self,
            text="Delete Note",
            width=250,
            fg_color="#C73E1D",
            hover_color="#8C2D15",
            font=self.winfo_toplevel().button_font,
            command=self.winfo_toplevel().delete_note,
            state="disabled",
        )
        self.delete_note_btn.grid(column=0, row=2, padx=10, pady=5)
        self.notes_list = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.notes_list.grid(column=0, row=3, sticky="nsew")
