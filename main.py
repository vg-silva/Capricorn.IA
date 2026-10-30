
import sys
from html import escape

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QTextBrowser,
    QLineEdit,
)
from PySide6.QtCore import Qt


class Capricorn(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CAPRICORN — Local Intelligence System")
        self.resize(1100, 700)

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout(central)

        # BARRA LATERAL
        sidebar = QVBoxLayout()

        logo = QLabel("CAPRICORN")
        logo.setObjectName("logo")

        subtitle = QLabel("LOCAL INTELLIGENCE SYSTEM")
        subtitle.setObjectName("subtitle")

        assistant_button = QPushButton("Assistente")
        tasks_button = QPushButton("Tarefas")
        documents_button = QPushButton("Documentos")
        settings_button = QPushButton("Configurações")

        sidebar.addWidget(logo)
        sidebar.addWidget(subtitle)
        sidebar.addSpacing(35)
        sidebar.addWidget(assistant_button)
        sidebar.addWidget(tasks_button)
        sidebar.addWidget(documents_button)
        sidebar.addStretch()
        sidebar.addWidget(settings_button)

        # ÁREA DO CHAT
        chat_layout = QVBoxLayout()

        title = QLabel("Assistente")
        title.setObjectName("title")

        status = QLabel("● SISTEMA LOCAL — INTERFACE ATIVA")
        status.setObjectName("status")

        self.chat_history = QTextBrowser()
        self.chat_history.setObjectName("chat")
        self.chat_history.setOpenExternalLinks(False)

        self.chat_history.append(
            '<p style="color:#E65B76;"><b>CAPRICORN</b></p>'
            '<p>Olá. Estou aguardando suas instruções.</p>'
        )

        # CAMPO DE MENSAGEM
        input_layout = QHBoxLayout()

        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText(
            "Digite uma mensagem para a CAPRICORN..."
        )

        send_button = QPushButton("Enviar")
        send_button.clicked.connect(self.send_message)

        self.message_input.returnPressed.connect(self.send_message)

        input_layout.addWidget(self.message_input)
        input_layout.addWidget(send_button)

        chat_layout.addWidget(title)
        chat_layout.addWidget(status)
        chat_layout.addWidget(self.chat_history, 1)
        chat_layout.addLayout(input_layout)

        main_layout.addLayout(sidebar, 1)
        main_layout.addLayout(chat_layout, 4)

        # IDENTIDADE VISUAL
        self.setStyleSheet("""
            QMainWindow {
                background-color: #101012;
            }

            QWidget {
                color: #F5F5F5;
                font-family: Segoe UI;
                font-size: 14px;
            }

            #logo {
                color: #E65B76;
                font-size: 25px;
                font-weight: bold;
            }

            #subtitle {
                color: #888888;
                font-size: 9px;
            }

            #title {
                font-size: 27px;
                font-weight: bold;
            }

            #status {
                color: #83D69A;
                font-size: 11px;
            }

            #chat {
                background-color: #17171C;
                border: 1px solid #292930;
                border-radius: 8px;
                padding: 15px;
                font-size: 14px;
            }

            QLineEdit {
                background-color: #1B1B20;
                border: 1px solid #393940;
                border-radius: 6px;
                padding: 12px;
                color: white;
            }

            QPushButton {
                background-color: #292930;
                color: white;
                border: none;
                padding: 12px;
                border-radius: 6px;
            }

            QPushButton:hover {
                background-color: #E65B76;
            }
        """)

    def send_message(self):
        message = self.message_input.text().strip()

        if not message:
            return

        safe_message = escape(message)

        self.chat_history.append(
            f'<p style="color:#83D69A;"><b>VOCÊ</b></p>'
            f'<p>{safe_message}</p>'
        )

        self.message_input.clear()

        # RESPOSTA TEMPORÁRIA
        self.chat_history.append(
            '<p style="color:#E65B76;"><b>CAPRICORN</b></p>'
            '<p>Mensagem recebida. Meu sistema de inteligência '
            'ainda não foi conectado.</p>'
        )


app = QApplication(sys.argv)

window = Capricorn()
window.show()

sys.exit(app.exec())
