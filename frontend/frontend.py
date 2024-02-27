import backend.database as db
import backend.notes as nt
import customtkinter as ctk

from frontend.sidebar import Sidebar
from frontend.body import MainWindow
from frontend.confirm_delete import ConfirmDelete


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        db.create_tables()

        ctk.set_appearance_mode("dark")
        self.title("Notes")
        self.geometry("1000x600")
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.title_font = ctk.CTkFont(family="Arial", size=40, weight="bold")
        self.body_font = ctk.CTkFont(family="Helvetica", size=16)
        self.button_font = ctk.CTkFont(family="Helvetica", size=13)

        # Sidebar
        self.sidebar = Sidebar(self, fg_color="transparent")
        self.sidebar.grid(column=0, row=0, padx=(10, 5), pady=10, sticky="ns")

        # Main Window
        self.main_window = MainWindow(self, fg_color="transparent")
        self.main_window.grid(column=1, row=0, padx=(5, 10), pady=10, sticky="nsew")

        # Start a New Note
        self.new_note()

        # Load buttons for any existing notes into the sidebar
        self.load_notes()

    def new_note(self):
        self.current_note_id = None
        self.main_window.title.delete(0, ctk.END)
        self.main_window.body.delete("1.0", ctk.END)
        self.main_window.title.insert(0, "New Note")
        self.main_window.body.focus_set()
        self.sidebar.delete_note_btn.configure(state="disabled")
        # Autosave note
        # self.after(120000, self.save_note)

    def save_note(self):
        title = self.main_window.title.get()
        body = self.main_window.body.get("1.0", ctk.END)

        if self.current_note_id is None:
            nt.create_note(title, body)
        else:
            nt.update_note(self.current_note_id, title, body)

        note_id = nt.get_last_note_id()
        self.current_note_id = note_id

        self.load_notes()
        self.sidebar.delete_note_btn.configure(state="normal")
        # Autosave note
        self.after(120000, self.save_note)

    def delete_note(self):
        if self.current_note_id is not None:
            nt.delete_note(self.current_note_id)
            self.load_notes()
            self.new_note()

    def load_note_content(self, note_id):
        note = nt.get_note(note_id)
        if note:
            note_title = note[1]
            note_body = note[2]
            self.current_note_id = note_id
            self.main_window.title.delete(0, ctk.END)
            self.main_window.body.delete("1.0", ctk.END)
            self.main_window.title.insert(0, note_title)
            self.main_window.body.insert("1.0", note_body)
            self.sidebar.delete_note_btn.configure(state="normal")

    def load_notes(self):
        for child in self.sidebar.notes_list.winfo_children():
            child.destroy()

        notes = nt.get_all_notes()

        for i, note in enumerate(notes):
            note_id = note[0]
            note_title = note[1]
            note_updated = note[3]
            button = ctk.CTkButton(
                self.sidebar.notes_list,
                text=note_title + " \n" + note_updated,
                width=250,
                fg_color="purple",
                font=self.button_font,
                command=lambda id=note_id: self.load_note_content(id),
            )
            button.grid(column=0, row=i, padx=10, pady=5)
