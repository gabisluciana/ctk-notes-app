import customtkinter as ctk


class ConfirmDelete(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.geometry("250x150")
        self.label = ctk.CTkLabel(self, text="Confirm Delete")
        self.label.grid(padx=20, pady=20, column=0, row=0, columnspan=2)

        self.delete_note_btn = ctk.CTkButton(
            self,
            text="Delete Note",
            width=100,
            fg_color="#C73E1D",
            hover_color="#8C2D15",
            font=self.master.button_font,
            command=self.master.delete_note,
        )
        self.delete_note_btn.grid(padx=10, pady=5, column=1, row=1)

        self.cancel_btn = ctk.CTkButton(
            self,
            text="Cancel",
            width=100,
            fg_color="#307C39",
            hover_color="#245E2B",
            font=self.master.button_font,
            command=self.destroy,
        )
        self.cancel_btn.grid(padx=10, pady=5, column=0, row=1)
