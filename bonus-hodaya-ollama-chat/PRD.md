# PRD – Local Ollama Desktop Chat

## Product Goal

The goal of this project is to build a desktop chat application with a graphical user interface that communicates with a local language model running through Ollama.

The application allows the user to type a message, send it to the local model through a direct API call, and view the model response inside the desktop chat window.

## Target Users

This project is intended for:

- The course evaluator
- Students in the LLM course
- Users who want to interact with a local language model without using an external web interface

## Main Requirements

- Desktop GUI application
- Local language model execution using Ollama
- Direct API communication with the local Ollama server
- Python virtual environment using venv
- Dependency management through requirements.txt
- Environment configuration through .env.example
- Clear engineering documentation

## User Flow

1. The user runs the application.
2. A desktop chat window opens.
3. The user types a message.
4. The application sends the message to the local Ollama API.
5. The local model generates a response.
6. The response is displayed in the chat window.

## Success Criteria

- The application opens as a desktop GUI.
- The user can type a message.
- The Send button sends the message to the model.
- A response is received from the local Ollama model.
- The project can be installed and executed from the GitHub repository.

## Limitations

- Ollama must be installed locally.
- The selected model must be available on the local machine.
- The application requires a local Python environment.
- The GUI is intentionally simple and focused on the assignment requirements.
