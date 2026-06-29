import dearpygui.dearpygui as dpg

from src.ollama_client import OllamaClient
from src.config import OLLAMA_MODEL


class ChatApp:
    def __init__(self):
        self.client = OllamaClient()
        self.chat_history = ""
        self.messages = [
            {
                "role": "system",
                "content": "You are a helpful local AI assistant. Answer clearly and briefly."
            }
        ]

    def _append_message(self, sender, text):
        self.chat_history += f"{sender}:\n{text}\n\n"
        dpg.set_value("chat_output", self.chat_history)

    def _send_message(self):
        user_text = dpg.get_value("user_input").strip()

        if not user_text:
            dpg.set_value("status_text", "Please type a message first.")
            return

        dpg.set_value("user_input", "")
        self._append_message("You", user_text)

        self.messages.append({
            "role": "user",
            "content": user_text
        })

        dpg.configure_item("send_button", enabled=False, label="Thinking...")
        dpg.set_value("status_text", "Sending request to local Ollama API...")

        assistant_response = self.client.chat(self.messages)

        self.messages.append({
            "role": "assistant",
            "content": assistant_response
        })

        self._append_message("Assistant", assistant_response)

        dpg.configure_item("send_button", enabled=True, label="Send")
        dpg.set_value("status_text", "Ready")

    def mainloop(self):
        dpg.create_context()

        with dpg.window(tag="main_window", label="Local Ollama Chat", width=900, height=650):
            dpg.add_text(f"Local Ollama Chat | Model: {OLLAMA_MODEL}")
            dpg.add_separator()

            dpg.add_input_text(
                tag="chat_output",
                multiline=True,
                readonly=True,
                width=-1,
                height=420,
                default_value="Assistant:\nHi! I am a local desktop chat app connected directly to Ollama through an API.\n\n"
            )

            dpg.add_spacer(height=10)

            dpg.add_input_text(
                tag="user_input",
                multiline=True,
                width=-1,
                height=90,
                hint="Type your message here..."
            )

            dpg.add_spacer(height=8)

            with dpg.group(horizontal=True):
                dpg.add_button(
                    tag="send_button",
                    label="Send",
                    width=120,
                    height=35,
                    callback=self._send_message
                )
                dpg.add_text("Ready", tag="status_text")

        dpg.create_viewport(
            title="Local Ollama Chat",
            width=920,
            height=700
        )

        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("main_window", True)
        dpg.start_dearpygui()
        dpg.destroy_context()
