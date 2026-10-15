
# -*- coding: utf-8 -*-
#!/usr/bin/env python

'''
Desarrollado Por: Cristian M. Veliz Cano

🎯 Soft - EN MEGA:
◢ ◤ CORRECTOR ORTOGRÁFICO (CYBERPUNK_EDITION v1.1 ◢ ◤
https://mega.nz/file/z1FhGJaa#g9fKw-mYN2v13LbjuClcN9rGhYQcJtDV9pLnpbPZK74
'''
##=========================================================================================
import sys, os
import re
from pathlib import Path
import ast

from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, 
    QPushButton, QLabel, QFileDialog, QMessageBox, QMenu, QAction, QStatusBar, QSplitter, QListWidget, 
    QListWidgetItem, QFrame, QPlainTextEdit, QShortcut, QDialog
)
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QRegExp, QPoint
from PyQt5.QtGui import (QColor, QFont, QSyntaxHighlighter, QTextCharFormat, QTextCursor, QKeySequence, 
    QPalette, QIcon
)

try:
    from spellchecker import SpellChecker
    SPELLCHECKER_AVAILABLE = True
except ImportError:
    SpellChecker = None
    SPELLCHECKER_AVAILABLE = False

from modules_list import DEFAULT_ALLOWED
from Dic_Rae import Diccionario_Palabras
from Diccionario_Ingles import Diccionario_Palabras_EN

##====================================================================================
# --- Clase para manejo de rutas de recursos ---
##====================================================================================
class Path():
    def resource_path(relative_path):
        """Get absolute path to resource, works for dev and for pyinstaller"""
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    # =========================
    # ✨ Devuelve, la Dirección Exacta de Cualquier, Archivo dentro de la App-Desk
    # =========================
    def resource_path_app():
        try:
            path_app = getattr(
                sys, "_MEIPASS",
                os.path.abspath(os.path.dirname(__file__))
            )
        except Exception as e:
            print(e)
        except IOError as error:
            print(error)
        return path_app

##====================================================================================
##====================================================================================
class CyberpunkStyle:
    """Paleta de colores Cyberpunk - Versión Masculina"""
    BG_DARK = "#0d1117"
    BG_PANEL = "#161b22"
    BG_INPUT = "#0c1020"
    NEON_CYAN = "#00d4ff"
    NEON_BLUE = "#0066ff"
    NEON_GREEN = "#00ff88"
    NEON_YELLOW = "#ffaa00"
    NEON_RED = "#ff3333"
    TEXT_GRAY = "#8b949e"
    TEXT_WHITE = "#c9d1d9"
    BORDER = "#30363d"

    @staticmethod
    def apply(app):
        app.setStyle("Fusion")
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(CyberpunkStyle.BG_DARK))
        palette.setColor(QPalette.WindowText, QColor(CyberpunkStyle.TEXT_WHITE))
        palette.setColor(QPalette.Base, QColor(CyberpunkStyle.BG_INPUT))
        palette.setColor(QPalette.AlternateBase, QColor(CyberpunkStyle.BG_PANEL))
        palette.setColor(QPalette.Text, QColor(CyberpunkStyle.TEXT_WHITE))
        palette.setColor(QPalette.Button, QColor(CyberpunkStyle.BG_PANEL))
        palette.setColor(QPalette.ButtonText, QColor(CyberpunkStyle.NEON_CYAN))
        palette.setColor(QPalette.Highlight, QColor(CyberpunkStyle.NEON_BLUE))
        palette.setColor(QPalette.HighlightedText, QColor(CyberpunkStyle.BG_DARK))
        app.setPalette(palette)

##====================================================================================
## BACK-END: MOTOR DE DICCIONARIO
##====================================================================================
class SpellBackend:
    """
    Motor central del corrector.

    La interfaz no decide si una palabra es correcta.
    Todo pasa por este backend para que:
      - el subrayado;
      - las sugerencias;
      - el reemplazo;
      - las estadísticas;
      - la lista de errores

    utilicen exactamente las mismas reglas.
    """

    WORD_RE = re.compile(r"\b[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]+\b", re.UNICODE)
    DEFAULT_ALLOWED = DEFAULT_ALLOWED()
    Diccionario_Palabras = Diccionario_Palabras()
    Diccionario_en_Ingles = Diccionario_Palabras_EN()

    def __init__(self):
        self.spellchecker = None
        self.language = None
        self.allowed_words = set(self.DEFAULT_ALLOWED)
        self.diccionario_palabras = set(self.Diccionario_Palabras)
        self.diccionario_en_EN = set(self.Diccionario_en_Ingles)

        # Cargar diccionario RAE
        self._load_rae_dictionary()
        self._load_dictionary_EN()

        # Palabras ignoradas durante la sesión actual
        self.ignored_words = set()
        self.personal_file = self._get_personal_dictionary_path()

        self._load_personal_dictionary()

        if SPELLCHECKER_AVAILABLE:
            try:
                self.spellchecker = SpellChecker(language="es")
                self.language = "ES"
            except Exception as exc:
                print(f"Error cargando diccionario español: {exc}")
                self.spellchecker = None
                self.language = None

    def _get_personal_dictionary_path(self):
        """
        En desarrollo: junto al .py.
        En PyInstaller: junto al ejecutable, no dentro de _MEIPASS.
        """
        try:
            if getattr(sys, "frozen", False):
                base = os.path.dirname(sys.executable)
            else:
                base = os.path.dirname(os.path.abspath(__file__))
        except Exception:
            base = os.path.abspath(".")

        return os.path.join(base, "diccionario_personal.txt")

    def _load_personal_dictionary(self):
        if not os.path.exists(self.personal_file):
            return

        try:
            with open(self.personal_file, "r", encoding="utf-8", errors='ignore') as fh:
                for line in fh:
                    word = line.strip().lower()
                    if word and not word.startswith("#"):
                        self.allowed_words.add(word)
        except Exception as exc:
            print(f"No se pudo cargar diccionario personal: {exc}")

    def _load_rae_dictionary(self):
        try:
            if getattr(sys, "frozen", False):
                base = os.path.dirname(sys.executable)
            else:
                base = os.path.dirname(os.path.abspath(__file__))
        except Exception:
            base = os.path.abspath(".")

        try:
            words = sorted(self.diccionario_palabras)
            for word in words:
                if word:
                    self.allowed_words.add(word)

            ## print(f"Diccionario RAE Cargado: {len(self.allowed_words)} Palabras")

        except Exception as exc:
            print(f"No se pudo cargar diccionario RAE: {exc}")

    def _load_dictionary_EN(self):
        try:
            if getattr(sys, "frozen", False):
                base = os.path.dirname(sys.executable)
            else:
                base = os.path.dirname(os.path.abspath(__file__))
        except Exception:
            base = os.path.abspath(".")

        try:
            words = sorted(self.diccionario_en_EN)
            for word in words:
                if word:
                    self.allowed_words.add(word)

            ## print(f"Diccionario En INGLES Cargado: {len(self.allowed_words)} Palabras")

        except Exception as exc:
            print(f"No se pudo cargar diccionario RAE: {exc}")

    def _save_personal_dictionary(self):
        try:
            words = sorted(self.allowed_words)
            with open(self.personal_file, "w", encoding="utf-8", errors='ignore') as fh:
                fh.write(
                    "# Diccionario personal - CORRECTOR ORTOGRÁFICO (CYBERPUNK_EDITION v1.1)\n"
                )
                for word in words:
                    fh.write(word + "\n")
            return True
        except Exception as exc:
            print(f"No se pudo guardar diccionario personal: {exc}")
            return False

    def normalize(self, word):
        return word.strip().lower()

    def is_special_word(self, word):
        """
        Palabras que no deben pasar por el diccionario ortográfico:
        acrónimos, términos técnicos, nombres con mayúsculas internas,
        etc.
        """
        if not word:
            return True

        normalized = self.normalize(word)

        if normalized in self.ignored_words:
            return True

        if len(normalized) <= 1:
            return True

        if normalized in self.allowed_words:
            return True

        # Acrónimos: PDF, OCR, TXT, API, etc.
        if word.isupper() and len(word) >= 2:
            return True

        # Siglas con mezcla de letras mayúsculas/minúsculas:
        # PyQt, OpenCV, QPlainTextEdit, etc.
        if any(ch.isupper() for ch in word[1:]):
            return True

        return False

    def is_correct(self, word):
        if self.is_special_word(word):
            return True

        if not self.spellchecker:
            return True

        return self.normalize(word) in self.spellchecker

    def is_error(self, word):
        return not self.is_correct(word)

    def words(self, text):
        return self.WORD_RE.findall(text)

    def errors(self, text):
        """
        Devuelve palabras únicas realmente consideradas errores.
        Conserva la primera escritura encontrada.
        """
        result = {}
        for word in self.words(text):
            if len(word) > 1 and self.is_error(word):
                key = self.normalize(word)
                if key not in result:
                    result[key] = word

        return set(result.values())

    def candidates(self, word):
        if not self.spellchecker:
            return []

        try:
            candidates = self.spellchecker.candidates(self.normalize(word))
        except Exception:
            return []

        if not candidates:
            return []

        # Orden estable y limitado en la interfaz.
        candidates = sorted(candidates, key=lambda value: value.lower())

        # Evitar devolver la misma palabra.
        normalized = self.normalize(word)
        result = []
        seen = set()

        for candidate in candidates:
            key = candidate.lower()
            if key == normalized or key in seen:
                continue
            seen.add(key)
            result.append(self.match_case(word, candidate))

        return result

    @staticmethod
    def match_case(original, replacement):
        """Conserva mayúsculas/minúsculas razonablemente al corregir."""
        if original.isupper():
            return replacement.upper()

        if original[:1].isupper():
            return replacement[:1].upper() + replacement[1:]

        return replacement.lower()

    def add_word(self, word):
        normalized = self.normalize(word)
        if not normalized:
            return False

        self.allowed_words.add(normalized)
        return self._save_personal_dictionary()

    def ignore_word(self, word):
        """
        Ignora una palabra durante la sesión actual.
        No modifica el diccionario personal.
        """
        normalized = self.normalize(word)

        if not normalized:
            return False

        self.ignored_words.add(normalized)
        return True

##====================================================================================
## BACK-END: RESALTADO -- CORRECTOR ORTOGRÁFICO (CYBERPUNK_EDITION v1.1)
##====================================================================================
class SpellHighlighter(QSyntaxHighlighter):
    """Resalta palabras mal escritas con subrayado rojo"""

    def __init__(self, parent, backend):
        super().__init__(parent)
        self.backend = backend

        self.error_format = QTextCharFormat()
        self.error_format.setUnderlineColor(QColor(CyberpunkStyle.NEON_RED))
        self.error_format.setUnderlineStyle(QTextCharFormat.SpellCheckUnderline)
        self.error_format.setForeground(QColor("#ff5555"))

        # Expresión para encontrar palabras (evita números y símbolos)
        self.word_regex = QRegExp(r"\b[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]+\b")

    def highlightBlock(self, text):
        if not self.backend:
            return

        index = self.word_regex.indexIn(text)

        while index >= 0:
            length = self.word_regex.matchedLength()
            word = text[index:index + length]

            if self.backend.is_error(word):
                self.setFormat(index, length, self.error_format)

            index = self.word_regex.indexIn(text, index + length)


##====================================================================================
## BACK-END: EDITOR
##====================================================================================
class CyberTextEdit(QPlainTextEdit):
    """Editor de texto con corrección integrada"""

    wordClicked = pyqtSignal(str, QPoint)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.spellchecker = None
        self.backend = None
        self.highlighter = None
        self._checking = False
        self._suggestion_cursor = None

        self.setStyleSheet(f"""
            QPlainTextEdit {{
                background-color: {CyberpunkStyle.BG_INPUT};
                color: {CyberpunkStyle.NEON_CYAN};
                border: 2px solid {CyberpunkStyle.BORDER};
                border-radius: 8px;
                padding: 10px;
                font-family: 'Consolas', 'Courier New', monospace;
                font-size: 14px;
                selection-background-color: {CyberpunkStyle.NEON_BLUE};
                selection-color: #000000;
            }}
        """)

        self.setFont(QFont("Consolas", 11))

        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.check_spelling)
        self.textChanged.connect(self.on_text_changed)

    def set_spellchecker(self, backend):
        self.backend = backend
        self.spellchecker = backend.spellchecker if backend else None
        self.highlighter = SpellHighlighter(self.document(), backend)
        self.check_spelling()

    def on_text_changed(self):
        self.timer.stop()
        self.timer.start(500)

    def check_spelling(self):
        if self._checking or not self.highlighter:
            return

        self._checking = True
        try:
            self.highlighter.rehighlight()
        finally:
            self._checking = False

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton and self.backend:
            cursor = self.cursorForPosition(event.pos())
            cursor.select(QTextCursor.WordUnderCursor)
            word = cursor.selectedText()

            if word and len(word) > 1 and self.backend.is_error(word):
                self._suggestion_cursor = QTextCursor(cursor)
                self.show_suggestions(word, event.globalPos())
                return

        super().mousePressEvent(event)

    def show_suggestions(self, word, pos):
        menu = QMenu(self)
        menu.setStyleSheet(f"""
            QMenu {{
                background-color: {CyberpunkStyle.BG_PANEL};
                color: {CyberpunkStyle.NEON_CYAN};
                border: 2px solid {CyberpunkStyle.NEON_BLUE};
                border-radius: 5px;
                padding: 5px;
            }}
            QMenu::item {{
                padding: 8px 25px;
                border-radius: 3px;
            }}
            QMenu::item:selected {{
                background-color: {CyberpunkStyle.NEON_BLUE};
                color: {CyberpunkStyle.BG_DARK};
            }}
            QMenu::separator {{
                height: 2px;
                background-color: {CyberpunkStyle.BORDER};
                margin: 5px 0px;
            }}
        """)

        suggestions = self.backend.candidates(word)

        if suggestions:
            title = menu.addAction("¿Quisiste decir...?")
            title.setEnabled(False)
            menu.addSeparator()

            for suggestion in suggestions[:5]:
                action = menu.addAction(f"  ➤ {suggestion}")
                action.triggered.connect(
                    lambda checked=False, s=suggestion:
                    self.replace_word(word, s)
                )
        else:
            action = menu.addAction("Sin sugerencias")
            action.setEnabled(False)

        menu.addSeparator()

        # ==========================================================
        # 🚫 IGNORAR ERROR
        # ==========================================================
        action_ignore = menu.addAction("🚫 Ignorar error")
        action_ignore.triggered.connect(
            lambda checked=False: self.ignore_error(word)
        )

        # ==========================================================
        # 📖 AGREGAR AL DICCIONARIO --->>> OPCIONAL...
        # ==========================================================
        # action_add = menu.addAction("➕ Agregar al diccionario")
        # action_add.triggered.connect(
        #     lambda checked=False: self.add_to_dictionary(word)
        # )

        menu.exec_(pos)

    def replace_word(self, old_word, new_word):
        """
        Reemplaza únicamente la instancia sobre la que se abrió
        el menú contextual. No modifica todas las coincidencias
        del documento.
        """
        if not self._suggestion_cursor:
            return

        cursor = QTextCursor(self._suggestion_cursor)

        if cursor.hasSelection():
            selected = cursor.selectedText()

            if selected.lower() == old_word.lower():
                cursor.insertText(new_word)
                self.setTextCursor(cursor)
                self.ensureCursorVisible()

        self._suggestion_cursor = None
        self.check_spelling()

    def ignore_error(self, word):
        """
        Ignora la palabra durante la sesión actual.
        La palabra vuelve a ser revisada al cerrar y abrir el programa.
        """
        if not self.backend:
            return

        if self.backend.ignore_word(word):
            self._suggestion_cursor = None

            # Actualizar inmediatamente el subrayado
            self.check_spelling()

            # Actualizar inmediatamente la lista/estadísticas
            window = self.window()
            if hasattr(window, "actualizar_estadisticas"):
                window.actualizar_estadisticas()

## OPCIONAL...
    # def add_to_dictionary(self, word):
    #     if not self.backend:
    #         return

    #     if self.backend.add_word(word):
    #         self.check_spelling()
    #         QMessageBox.information(
    #             self,
    #             "Diccionario",
    #             f"'{word}' agregada al diccionario"
    #         )
    #     else:
    #         QMessageBox.warning(
    #             self,
    #             "Diccionario",
    #             "No se pudo guardar el diccionario personal."
    #         )


##====================================================================================
## VENTANA PRINCIPAL
##====================================================================================
class CorrectorOrtografico(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("⚡ CORRECTOR ORTOGRÁFICO (CYBERPUNK_EDITION v1.1) ⚡")
        ##self.setGeometry(100, 100, 1200, 800)

        # Icono
        icon_path = Path.resource_path("Ico\\1.ico")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        self.center_on_screen()

        # BACK-END: una sola instancia del motor.
        self.backend = SpellBackend()
        self.spellchecker = self.backend.spellchecker

        self.setup_ui()
        
        # Atajos de teclado
        info_software = QShortcut(QKeySequence('F1'), self)
        info_software.activated.connect(lambda: CorrectorOrtografico.show_app_info(self))
        
        key_info_software = QShortcut(QKeySequence('Ctrl+K'), self)
        key_info_software.activated.connect(self.key_app_info)
        
        key_Open = QShortcut(QKeySequence('Ctrl+O'), self)
        key_Open.activated.connect(self.abrir_archivo)
        
        key_Save = QShortcut(QKeySequence('Ctrl+G'), self)
        key_Save.activated.connect(self.guardar_archivo)
        
        key_Read = QShortcut(QKeySequence('Ctrl+R'), self)
        key_Read.activated.connect(self.verificar_todo)
        
        key_cleaner = QShortcut(QKeySequence('Ctrl+L'), self)
        key_cleaner.activated.connect(self.limpiar_texto)

        self.key_app_info()

    def setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        # Título
        title = QLabel("◢ ◤ CORRECTOR ORTOGRÁFICO (CYBERPUNK_EDITION v1.1) ◢ ◤")
        title.setStyleSheet(f"""
            QLabel {{
                color: {CyberpunkStyle.NEON_CYAN};
                font-size: 24px;
                font-weight: bold;
                font-family: 'Consolas', monospace;
                padding: 10px;
                border-bottom: 2px solid {CyberpunkStyle.NEON_BLUE};
            }}
        """)
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Barra de herramientas
        toolbar = QHBoxLayout()

        btn_abrir = self.create_neon_button("📂 Abrir TXT", CyberpunkStyle.NEON_CYAN)
        btn_abrir.clicked.connect(self.abrir_archivo)

        btn_guardar = self.create_neon_button("💾 Guardar", CyberpunkStyle.NEON_GREEN)
        btn_guardar.clicked.connect(self.guardar_archivo)

        btn_verificar = self.create_neon_button("🔍 Verificar", CyberpunkStyle.NEON_YELLOW)
        btn_verificar.clicked.connect(self.verificar_todo)

        btn_limpiar = self.create_neon_button("🗑️ Limpiar", CyberpunkStyle.NEON_RED)
        btn_limpiar.clicked.connect(self.limpiar_texto)

        toolbar.addWidget(btn_abrir)
        toolbar.addWidget(btn_guardar)
        toolbar.addWidget(btn_verificar)
        toolbar.addWidget(btn_limpiar)
        toolbar.addStretch()

        layout.addLayout(toolbar)

        # Splitter
        splitter = QSplitter(Qt.Horizontal)
        self.editor = CyberTextEdit()
        self.editor.set_spellchecker(self.backend)
        splitter.addWidget(self.editor)

        panel = self.create_side_panel()
        splitter.addWidget(panel)
        splitter.setSizes([800, 300])

        layout.addWidget(splitter)

        # Barra de estado
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.status.setStyleSheet(f"""
            QStatusBar {{
                background-color: {CyberpunkStyle.BG_PANEL};
                color: {CyberpunkStyle.NEON_CYAN};
                border-top: 2px solid {CyberpunkStyle.NEON_BLUE};
                padding: 5px;
                font-family: 'Consolas', monospace;
            }}
        """)

        idioma = self.backend.language if self.backend.language else "NO DISPONIBLE"
        self.status.showMessage(f"Sistema listo | Diccionario: {idioma}")

        self.setStyleSheet(f"""
            QMainWindow {{
                background-color: {CyberpunkStyle.BG_DARK};
            }}
            QWidget {{
                background-color: {CyberpunkStyle.BG_DARK};
            }}
        """)

        self.stats_timer = QTimer()
        self.stats_timer.timeout.connect(self.actualizar_estadisticas)
        self.stats_timer.start(1000)

    def create_neon_button(self, text, color):
        btn = QPushButton(text)
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {CyberpunkStyle.BG_PANEL};
                color: {color};
                border: 2px solid {color};
                border-radius: 8px;
                padding: 10px 20px;
                font-family: 'Consolas', monospace;
                font-weight: bold;
                font-size: 12px;
                min-width: 120px;
            }}
            QPushButton:hover {{
                background-color: {color};
                color: {CyberpunkStyle.BG_DARK};
            }}
            QPushButton:pressed {{
                background-color: {CyberpunkStyle.BG_DARK};
                color: {color};
            }}
        """)
        btn.setCursor(Qt.PointingHandCursor)
        return btn

    def create_side_panel(self):
        panel = QFrame()
        panel.setStyleSheet(f"""
            QFrame {{
                background-color: {CyberpunkStyle.BG_PANEL};
                border: 2px solid {CyberpunkStyle.NEON_BLUE};
                border-radius: 10px;
                padding: 10px;
            }}
        """)

        layout = QVBoxLayout(panel)

        lbl_stats = QLabel("📊 ESTADÍSTICAS")
        lbl_stats.setStyleSheet(f"color: {CyberpunkStyle.NEON_BLUE}; font-weight: bold; font-size: 14px;")
        layout.addWidget(lbl_stats)

        self.lbl_palabras = QLabel("Palabras: 0")
        self.lbl_palabras.setStyleSheet(f"color: {CyberpunkStyle.TEXT_WHITE}; font-family: Consolas;")
        layout.addWidget(self.lbl_palabras)

        self.lbl_errores = QLabel("Errores: 0")
        self.lbl_errores.setStyleSheet(f"color: {CyberpunkStyle.NEON_RED}; font-family: Consolas;")
        layout.addWidget(self.lbl_errores)

        self.lbl_lineas = QLabel("Líneas: 0")
        self.lbl_lineas.setStyleSheet(f"color: {CyberpunkStyle.NEON_CYAN}; font-family: Consolas;")
        layout.addWidget(self.lbl_lineas)

        layout.addSpacing(20)

        lbl_errors = QLabel("⚠️ ERRORES DETECTADOS:")
        lbl_errors.setStyleSheet(f"color: {CyberpunkStyle.NEON_YELLOW}; font-weight: bold; font-size: 12px;")
        layout.addWidget(lbl_errors)

        self.lista_errores = QListWidget()
        self.lista_errores.setStyleSheet(f"""
            QListWidget {{
                background-color: {CyberpunkStyle.BG_INPUT};
                color: {CyberpunkStyle.TEXT_WHITE};
                border: 1px solid {CyberpunkStyle.BORDER};
                border-radius: 5px;
                padding: 5px;
                font-family: Consolas;
            }}
            QListWidget::item {{
                padding: 5px;
                border-bottom: 1px solid {CyberpunkStyle.BORDER};
            }}
            QListWidget::item:selected {{
                background-color: {CyberpunkStyle.NEON_BLUE};
                color: black;
            }}
        """)
        self.lista_errores.itemClicked.connect(self.ir_a_error)
        layout.addWidget(self.lista_errores)

        layout.addStretch()

        help_text = QLabel("💡 Tip: Click derecho\nen palabra subrayada\npara ver sugerencias")
        help_text.setStyleSheet(f"color: {CyberpunkStyle.TEXT_GRAY}; font-size: 10px;")
        layout.addWidget(help_text)

        return panel

    ##=========================================================================================
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            sys.exit()
        else:
            super().keyPressEvent(event)

    ##=========================================================================================
    def center_on_screen(self):
        screen = QApplication.primaryScreen().availableGeometry()
        w, h = 1000, 700
        x = (screen.width() - w) // 2
        y = (screen.height() - h) // 2 + 10
        self.setGeometry(x, y, w, h)

    ##=========================================================================================
    def show_app_info(self):
        dialog = app_info(self)
        dialog.exec_()

    def key_app_info(self):
        dialog_k = key_info(self)
        dialog_k.exec_()

    ##=========================================================================================
    def abrir_archivo(self):
        fname, _ = QFileDialog.getOpenFileName(
            self, "Abrir archivo", "",
            "Texto (*.txt *.md *.py *.json *.csv);;Todos los archivos (*)"
        )
        if fname:
            try:
                with open(fname, "r", encoding="utf-8", errors='ignore') as f:
                    contenido = f.read()
                self.editor.setPlainText(contenido)
                self.status.showMessage(f"Archivo cargado: {fname}")
                self.actualizar_estadisticas()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo abrir:\n{str(e)}")

    def guardar_archivo(self):
        fname, _ = QFileDialog.getSaveFileName(
            self, "Guardar archivo", "",
            "Texto (*.txt);;Markdown (*.md);;Todos los archivos (*)"
        )
        if fname:
            try:

                with open(fname, "w", encoding="utf-8", errors='ignore') as f:
                    f.write(self.editor.toPlainText())
                self.status.showMessage(f"Guardado: {fname}")
                QMessageBox.information(self, "Aviso", f"✅ Archivo Guardado Exitosamente en:\n{str(fname)}")
            
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo guardar:\n{str(e)}")

    def verificar_todo(self):
        self.editor.check_spelling()
        self.actualizar_estadisticas()
        self.status.showMessage("Verificación completada", 2000)

    def limpiar_texto(self):
        self.editor.clear()
        self.status.showMessage("Texto eliminado", 2000)

    def actualizar_estadisticas(self):
        texto = self.editor.toPlainText()

        # Mantiene el mismo criterio visual del Front-End:
        # palabras separadas por límites de palabra.
        palabras = len(re.findall(r"\b\w+\b", texto, re.UNICODE))
        lineas = texto.count("\n") + 1 if texto else 0

        errores = set()
        if self.backend:
            errores = self.backend.errors(texto)

        self.lbl_palabras.setText(f"Palabras: {palabras}")
        self.lbl_errores.setText(f"Errores: {len(errores)}")
        self.lbl_lineas.setText(f"Líneas: {lineas}")

        self.lista_errores.clear()

        for error in sorted(errores, key=str.lower)[:20]:
            item = QListWidgetItem(f"❌ {error}")
            item.setData(Qt.UserRole, error)
            self.lista_errores.addItem(item)

    def ir_a_error(self, item):
        palabra = item.data(Qt.UserRole)

        if palabra:
            cursor = self.editor.textCursor()
            texto = self.editor.toPlainText()

            # Buscar desde el principio, ignorando mayúsculas/minúsculas.
            match = re.search(
                r"\b" + re.escape(palabra) + r"\b",
                texto,
                re.IGNORECASE | re.UNICODE
            )

            if match:
                cursor.setPosition(match.start())
                cursor.setPosition(
                    match.end(),
                    QTextCursor.KeepAnchor
                )
                self.editor.setTextCursor(cursor)
                self.editor.ensureCursorVisible()
                self.editor.setFocus()

##======================================================================================
# DICCIONARIOS CARGADOS || REFUERZO
##======================================================================================
try:

    rae_allowed_words = set()
    EN_allowed_words = set()
    dic_personal = set()
    total_palabras = set()

    words = sorted(Diccionario_Palabras())
    for word in words:
        if word:
            rae_allowed_words.add(word)
            total_palabras.add(word)

    words = sorted(Diccionario_Palabras_EN())
    for word in words:
        if word:
            EN_allowed_words.add(word)
            total_palabras.add(word)

    palabras = sorted(DEFAULT_ALLOWED())
    for word in palabras:
        if word:
            dic_personal.add(word)
            total_palabras.add(word)

    print(f"--> Diccionario RAE cargado: {len(rae_allowed_words)} palabras")
    print(f"--> Diccionario en INGLES cargado: {len(EN_allowed_words)} palabras")
    print(f"--> Diccionario Personal cargado: {len(dic_personal)} palabras")
    print(f"--> Palabras Cargadas en Diccionarios: {len(total_palabras)} palabras")

except Exception as exc:
    print(f"No se pudo cargar diccionario RAE: {exc}")
##======================================================================================
##======================================================================================
# Diálogo de información
class app_info(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setWindowTitle("✨ Información del Software ||  (CYBERPUNK_EDITION v1.0) ✨")
        self.setFixedSize(600, 500)
        self.setModal(True)
        
        icon_path = Path.resource_path('Ico\\1.ico')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        
        self.init_ui()

        idioma = f'''
➜ "Dic. RAE: {len(rae_allowed_words)} palabras")
➜ "Dic. EN cargado: {len(EN_allowed_words)} palabras")
➜ "Dic. PERS.: {len(dic_personal)} palabras")
➜ "WORDs Dic.: {len(total_palabras)} palabras")
        '''

        self.parent = parent
        self.parent.status.showMessage(f"Sistema listo | Diccionarios: {idioma}")
    
    def init_ui(self):
        layout = QVBoxLayout(self)
        
        title = QLabel("◢ ◤ CORRECTOR ORTOGRÁFICO ◢ ◤")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                font-size: 24pt;
                font-weight: bold;
                color: #00A3FF;
            }
        """)
        layout.addWidget(title)
        
        info_text = QTextEdit()
        info_text.setReadOnly(True)
        info_text.setText(f'''
Desarrollado por: 👉 Cristian M. Veliz Cano ✔
Versión del Soft: 👉 V-1.1
Nombre del Soft: CORRECTOR ORTOGRÁFICO (CYBERPUNK_EDITION v1.1)
✨ CORRECTOR ORTOGRÁFICO ✨

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📎 DICCIONARIOS CARGADOS |📑| PARA REFUERZO:

➜ "Diccionario RAE cargado: {len(rae_allowed_words)} palabras")
➜ "Diccionario EN cargado: {len(EN_allowed_words)} palabras")
➜ "Diccionario Personal cargado: {len(dic_personal)} palabras")
➜ "Palabras Cargadas en Diccionarios: {len(total_palabras)} palabras")
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 Licencia:

MIT License

Copyright (c) 2026 Cristian M. Veliz Cano

Se concede permiso, de forma gratuita, a cualquier persona
que obtenga una copia de este software...

EL SOFTWARE SE PROPORCIONA "TAL CUAL",
SIN GARANTÍA DE NINGÚN TIPO.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Todas las definiciones de la RAE en .txt
Las palabras se extrajeron del trabajo de: 
✔ https://github.com/JorgeDuenasLerin/diccionario-espanol-txt

Puede llegar y tomar los .txt y usarlos puesto que ya están pulidos. 
Si quiere saber sobre el método de extracción lea lo que sigue.

📎 NOTA:
   • Para Agregar, el Diccionario, RAE, solamente, se Agregaron, 
   las    Claves, es decir, las Palabras, más no su Definición, 
   puesto que, no le mire, ninguna Finalidad, Todo el Trabajo, 
   Sobre el Dic. RAE, las Key_Words, son las Genuinas, y se le 
   agregan como Soporte a la Libreria: SpellChecker de 
   spellchecker.

📎 NOTA 2:
   • El Diccionario, Nuevo Agregado, es el Diccionario
   en Ingles, la Referencia, que me pasaron sobre este
   es:
    *Contact *GitHub *API *Training *Shop Blog *About 
    © 2017 *GitHub, Inc. *Terms *Privacy *Security Status
    *Help

   • El Diccionario no me Pertenece, pero se Encuentra en 
   GitHub con el nombre de:  [*javierarce/Words]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📦 De Caracter Gratuito, Portable,
🎭 Open-Source, Didáctico y Free-Code.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⌨️ Atajos del Teclado:

📎 F1
• Para mostrar información del software.

📎 CTRL+K
⌨️ Para mostrar los Atajos del Teclado.

📎 ESC
• Cierra inmediatamente el Soft-Ware.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        ''')
        
        info_text.setStyleSheet("""
            QTextEdit {
                background-color: #1E1E1E;
                color: #F1F1F1;
                border: 1px solid #5A5A5A;
                border-radius: 5px;
                padding: 8px;
                font-size: 10pt;
            }
        """)
        layout.addWidget(info_text)
        
        close_button = QPushButton("Cerrar")
        close_button.clicked.connect(self.close)
        close_button.setFixedHeight(32)
        layout.addWidget(close_button)

    ##=========================================================================================
    def closeEvent(self, event):
        print('Cerrando [closeEvent]...')
        self.parent.status.showMessage("Sistema listo | Diccionario: ES")
        event.accept()

    ##=========================================================================================
    def keyPressEvent(self, event):
        
        if event.key() == Qt.Key_Escape:
            print('1- Cerrando [keyPressEvent]...')
            self.parent.status.showMessage("Sistema listo | Diccionario: ES")
            event.accept()
            self.close()
        else:
            print('2- Cerrando [keyPressEvent]...')
            self.parent.status.showMessage("Sistema listo | Diccionario: ES")
            event.accept()
            self.close()

##====================================================================================
##====================================================================================
class key_info(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setWindowTitle("Atajo de Teclas")
        self.setFixedSize(520, 420)
        self.setModal(True)
        
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout(self)
        
        title = QLabel("Atajo de Teclas")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                font-size: 16pt;
                font-weight: bold;
                color: #00A3FF;
            }
        """)
        layout.addWidget(title)
        
        info_text = QTextEdit()
        info_text.setReadOnly(True)
        info_text.setText(f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⌨️ Atajos del Teclado:

📎 F1
• Para mostrar información del software.

📎 CTRL+K
⌨️ Para mostrar los Atajos del Teclado.

📎 CTRL+O
⌨️ Para abrir, un Archivo (*.txt).

📎 CTRL+G
⌨️ Para guardar en Texto Plano, las Modificaciónes.

📎 CTRL+R
⌨️ Para verificar, el Texto Ingresado, con (Copy|Paste).

📎 CTRL+L
⌨️ Para Limpiar la Caja de Texto.

📎 ESC
• Cierra inmediatamente el Soft-Ware.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 Licencia:

MIT License

Copyright (c) 2026 Cristian M. Veliz Cano

Se concede permiso, de forma gratuita...

EL SOFTWARE SE PROPORCIONA "TAL CUAL",
SIN GARANTÍA DE NINGÚN TIPO.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📎 DICCIONARIOS CARGADOS |📑| PARA REFUERZO:

➜ "Diccionario RAE cargado: {len(rae_allowed_words)} palabras")
➜ "Diccionario EN cargado: {len(EN_allowed_words)} palabras")
➜ "Diccionario Personal cargado: {len(dic_personal)} palabras")
➜ "Palabras Cargadas en Diccionarios: {len(total_palabras)} palabras")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Todas las definiciones de la RAE en .txt
Las palabras se extrajeron del trabajo de: 
✔ https://github.com/JorgeDuenasLerin/diccionario-espanol-txt

Puede llegar y tomar los .txt y usarlos puesto que ya están pulidos. 
Si quiere saber sobre el método de extracción lea lo que sigue.

📎 NOTA:
   • Para Agregar, el Diccionario, RAE, solamente, se 
   Agregaron, las    Claves, es decir, las Palabras, 
   más no su Definición,    puesto que, no le mire, 
   ninguna Finalidad, Todo el Trabajo, Sobre el 
   Dic. RAE, las Key_Words, son las Genuinas, y se le 
   agregan como Soporte a la Libreria: SpellChecker de 
   spellchecker.

📎 NOTA 2:
   • El Diccionario, Nuevo Agregado, es el Diccionario
   en Ingles, la Referencia, que me pasaron sobre este
   es:
    *Contact *GitHub *API *Training *Shop Blog *About 
    © 2017 *GitHub, Inc. *Terms *Privacy *Security Status
    *Help

   • El Diccionario no me Pertenece, pero se Encuentra en 
   GitHub con el nombre de:  [*javierarce/Words]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
        
        info_text.setStyleSheet("""
            QTextEdit {
                background-color: #1E1E1E;
                color: #F1F1F1;
                border: 1px solid #5A5A5A;
                border-radius: 5px;
                padding: 8px;
                font-size: 10.5pt;
            }
        """)
        layout.addWidget(info_text)
        
        close_button = QPushButton("Cerrar")
        close_button.clicked.connect(self.close)
        close_button.setFixedHeight(32)
        layout.addWidget(close_button)

##====================================================================================
# INNICIO DEL PROGRAMA (INI || MAIN)
##====================================================================================
def main():
    app = QApplication(sys.argv)
    CyberpunkStyle.apply(app)

    font = QFont("Consolas", 10)
    if not QFont(font).exactMatch():
        font = QFont("Courier New", 10)
    app.setFont(font)

    ventana = CorrectorOrtografico()
    ventana.show()
    sys.exit(app.exec_())

##====================================================================================
# fIN DEL PROGRAMA (INI || MAIN)
##====================================================================================
if __name__ == "__main__":
    main()
##====================================================================================
##====================================================================================