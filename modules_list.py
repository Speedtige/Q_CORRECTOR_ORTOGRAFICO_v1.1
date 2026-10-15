
# -*- coding: utf-8 -*-
#!/usr/bin/env python

'''
Desarrollado Por: Cristian M. Veliz Cano
'''
def DEFAULT_ALLOWED():

	mapeo = {
    # --- Lenguajes de Programación y Frameworks ---
    "python","py", "python3", "python programming", "python scripting", "python language", "python code", "python dev",
    "javascript","js", "javascript language", "ecmascript", "node.js", "nodejs", "frontend scripting", "js code",
    "java","java language", "jvm", "java development", "jdk", "jre", "spring boot", "maven", "gradle",
    "c++","cpp", "c plus plus", "gnu c++", "g++", "stl", "c++ standard library", "c++ development",
    "php","php language", "php scripting", "laravel", "symfony", "composer", "backend scripting",
    "ruby","ruby on rails", "rails framework", "ruby language", "gem", "bundler", "ruby scripting",
    "go","golang", "go language", "go programming", "go modules",
    "rust","rust lang", "rust programming", "cargo", "rust memory safety", "systems programming",
    "sql","structured query language", "sql query", "database query", "t-sql", "pl/sql", "mysql", "postgresql",
    "html","hypertext markup language", "html5", "web markup", "html code", "html tags",
    "css","cascading style sheets", "css3", "stylesheet", "style rules", "sass", "scss", "less",
    
    # --- Herramientas y Tecnologías de Desarrollo ---
    "git","git version control", "git repo", "github", "gitlab", "bitbucket", "git commit", "git branch", "git merge",
    "docker","containers", "containerization", "dockerfile", "docker compose", "docker image", "docker hub", "kubernetes", "k8s",
    "api","application programming interface", "rest api", "restful", "graphql", "api endpoint", "web service", "microservice",
    "aws","amazon web services", "ec2", "s3", "lambda", "rds", "cloud computing", "aws cloud",
    "azure","microsoft azure", "azure cloud", "azure services", "cloud platform ms",
    "gcp","google cloud platform", "gcp cloud", "google compute engine", "gke",
    "ci/cd","continuous integration", "continuous deployment", "jenkins", "github actions", "gitlab ci", "devops pipeline",
    "testing","unit testing", "integration testing", "pytest", "unittest", "jest", "selenium", "tdd", "test driven development",
    "linux","gnu linux", "linux kernel", "ubuntu", "debian", "centos", "shell scripting", "bash", "command line",
    "windows","win32", "powershell", "windows server", "active directory", "windows os",
    "macos","os x", "mac os", "cocoa", "swift", "xcode", "apple os",
    
    # --- Conceptos y Paradigmas ---
    "algoritmo","algorithm", "algorithm design", "complexity", "big o notation", "data structures", "sorting algorithms",
    "base de datos","database", "dbms", "rdbms", "nosql", "mongodb", "cassandra", "redis", "data storage", "sql database",
    "seguridad","security", "cybersecurity", "cryptography", "encryption", "hashing", "vulnerability", "penetration testing", "owasp",
    "osint","open source intelligence", "open-source intelligence", "intelligence gathering", "reconnaissance", "infosec",
    "machine learning","ml", "ai", "artificial intelligence", "deep learning", "neural networks", "tensorflow", "pytorch", "scikit-learn", "data science",
    "blockchain","distributed ledger", "smart contracts", "ethereum", "bitcoin", "cryptocurrency", "dlt", "web3",
    "devops","development operations", "infrastructure as code", "automation", "ansible", "puppet", "chef", "terraform",
    
    # --- Recursos y Comunidades ---
    "stackoverflow","stack overflow", "stackexchange", "programming q&a", "so", "coding forum",
    "github","git repo", "github repo", "code repository", "source control", "open source", "git hosting",
    "documentación","docs", "documentation", "api docs", "readthedocs", "tech reference", "manual",

    # --- Ingeniería de Software ---
    "arquitectura","software architecture", "system architecture", "microservices architecture", "design patterns", "arquitectura de sistemas",
    "uml","unified modeling language", "uml diagrams", "diagrama de clases", "casos de uso", "modelado",
    "poo","oop", "object oriented programming", "programación orientada a objetos", "clases y objetos", "herencia", "polimorfismo",
    "clean code","código limpio", "clean architecture", "refactoring", "buenas prácticas", "principios solid", "tdd", "arquitectura limpia",
    "debug","debugging", "depuración", "troubleshooting", "bug fixing", "error tracking",

    # --- Redes e Infraestructura ---
    "redes","networking", "network infrastructure", "routers", "switches", "protocolos de red", "tcp/ip", "dns", "dhcp",
    "vpn","virtual private network", "conexion segura", "remote access", "tunel vpn",
    "firewall","security firewall", "waf", "network filter", "protection layer", "filtrado de paquetes",
    "servidor","server", "dedicated server", "vps", "host", "http server", "nginx", "apache",

    # --- Ingeniería y electrónica ---
    "microcontrolador","microcontroller", "embedded system", "arduino", "esp32", "stm32", "programación embebida",
    "sensores","sensor", "iot sensor", "arduino sensors", "electronic measurement", "telemetría", "sensores iot",
    "robotica","robotics", "autonomous systems", "servo motors", "ros", "robot control", "mecatrónica",

    # --- Inteligencia Artificial avanzada ---
    "nlp","natural language processing", "procesamiento de lenguaje natural", "tokenization", "llm", "transformers",
    "vision","computer vision", "visión artificial", "image processing", "ocr", "detección de objetos",
    "dataset","data set", "training data", "conjunto de datos", "data labeling", "csv dataset",
    "reinforcement learning","rl", "aprendizaje por refuerzo", "agent training", "reward function",

    # --- Data Science, Big Data y Estadística ---
    "big data","large scale data", "hadoop", "spark", "databricks", "data lakes", "etl", "pipelines",
    "estadística","statistics", "probability", "regression", "anova", "data analysis", "modelos estadísticos",
    "visualización","data visualization", "plots", "dashboards", "matplotlib", "power bi", "tableau",

    # --- Ciberseguridad avanzada ---
    "malware","virus", "troyano", "spyware", "malicious software", "payload",
    "forense digital","digital forensics", "dfir", "análisis forense", "memory dump", "evidencia digital",
    "exploits","vulnerability exploit", "rce", "lfi", "rfi", "buffer overflow", "exploit db",

    # --- Desarrollo móvil ---
    "android","android dev", "apk", "kotlin", "java android", "android studio",
    "ios","iphone dev", "swiftui", "xcode project", "objective-c",

    # --- Matemáticas aplicadas a ingeniería ---
    "matrices","matrix", "matrix algebra", "álgebra lineal", "vectores", "numpy array",
    "calculo","calculus", "derivatives", "integrals", "math analysis", "matemáticas avanzadas",

    # --- Vida Diaria y Hogar ---
    "persona","person", "individual", "contact", "profile", "gente", "individuo", "sujeto",
    "ubicacion","location", "place", "address", "city", "site", "lugar", "sitio", "dirección", "posición",
    "casa","home", "house", "apartment", "flat", "domicilio", "vivienda", "hogar", "departamento",
    "comida","food", "meal", "cuisine", "dish", "alimento", "platillo", "vianda",
    "receta","recipe", "cooking recipe", "food recipe", "gastronomy", "cocina", "guía de cocina",
    "limpieza","cleaning", "cleaning tips", "house cleaning", "tidying", "aseo", "orden", "higiene",
    "compra","shopping", "purchase", "buying", "store", "market", "comprar", "adquisición",
    "dinero","money", "cash", "currency", "funds", "payment", "pago", "capital", "finanzas",
    "salud","health", "wellness", "fitness", "medicine", "well-being", "bienestar", "medicina", "forma física",
    "trabajo","job", "work", "employment", "career", "profession", "oficio", "empleo", "ocupación",
    "educación","education", "learning", "school", "university", "course", "study", "aprendizaje", "formación",
    "familia","family", "relatives", "kin", "household", "parientes", "familiares",
    "amigos","friends", "friendship", "buddies", "pals", "amistad", "compañeros",
    
    # --- Intereses y Ocio ---
    "deporte","sport", "sports", "exercise", "game", "match", "competency", "ejercicio físico", "competencia",
    "música","music", "song", "track", "melody", "tune", "canción", "tema musical",
    "viaje","travel", "trip", "journey", "vacation", "tourism", "viajar", "excursión", "turismo",
    "libro","book", "novel", "reading", "text", "publication", "lectura", "texto", "publicación",
    "película","movie", "film", "cinema", "motion picture", "cine", "filme",
    "coche","car", "automobile", "vehicle", "auto", "motorcar", "vehículo", "automóvil",
    "mascota","pet", "animal", "companion animal", "mascota", "animal doméstico",
    
    # --- Agricultura y Naturaleza ---
    "semillas","seed", "seeds", "plant seeds", "agriculture seeds", "semilla", "grano", "simiente",
    "fertilizantes","fertilizer", "fertilisers", "plant feed", "nutrients", "abono", "nutrientes para plantas",
    "planta","plant", "flora", "vegetation", "greenery", "vegetal", "flora local",
    "jardín","garden", "yard", "orchard", "patio", "cultivo", "huerto",
    "clima","weather", "climate", "temperature", "forecast", "tiempo atmosférico", "pronóstico del tiempo",
    
    # --- Conceptos Abstractos y Comunicación ---
    "idea","idea", "concept", "thought", "notion", "inspiration", "brainwave", "concepto", "pensamiento", "inspiración",
    "problema","problem", "issue", "challenge", "trouble", "dilemma", "obstacle", "inconveniente", "dilema", "obstáculo",
    "solución","solution", "answer", "fix", "resolution", "remedy", "solve", "respuesta", "arreglo", "resolución", "remedio",
    "tiempo","time", "moment", "duration", "period", "while", "ocasion", "momento", "duración", "período", "rato",
    "amor","love", "affection", "romance", "passion", "devotion", "cariño", "afecto", "pasión",
    "feliz","happy", "joyful", "glad", "cheerful", "delighted", "content", "alegre", "contento", "satisfecho",
    "triste","sad", "unhappy", "sorrowful", "melancholy", "depressed", "deprimido", "melancólico",
    "conversación","conversation", "talk", "chat", "dialogue", "discussion", "charla", "diálogo", "debate", "plática",
    "pregunta","question", "query", "inquiry", "doubt", "consulta", "duda", "preguntar",
    "respuesta","answer", "reply", "response", "retort", "respuesta", "réplica", "contestación",
    "información","information", "info", "data", "details", "facts", "knowledge", "datos", "detalles", "conocimiento", "saber",
    "noticia","news", "report", "update", "headline", "story", "reportaje", "titular", "actualidad",
    "evento","event", "occasion", "happening", "incident", "affair", "acontecimiento", "suceso", "incidente",
    "oportunidad","opportunity", "chance", "prospect", "opening", "oportunidad", "posibilidad", "ocasión",

    # --- Transporte ---
    "motocicleta","moto", "motorcycle", "bike", "motocicleta", "vehículo de dos ruedas",
    "autobús","bus", "coach", "transporte público", "camioneta pública",
    "bicicleta","bicycle", "bike", "cicla", "bici",

    # --- Oficios y trabajos técnicos civiles ---
    "electricista","electrician", "instalador eléctrico", "servicio eléctrico", "cables", "circuitos del hogar",
    "plomero","plumber", "fontanero", "tuberías", "reparación de fugas", "drenajes",
    "carpintero","carpenter", "madera", "ebanistería", "muebles",
    "albañil","mason", "construction worker", "block", "cemento", "yeso",
    "herramientas","tools", "hand tools", "kit de herramientas", "martillo", "llave inglesa",

    # --- Servicios públicos ---
    "agua","water", "servicio de agua", "suministro", "tuberías", "plomería",
    "electricidad","electricity", "power", "luz", "energía", "corriente",
    "internet","wifi", "network", "router", "conexión web",

    # --- Cocina y hogar avanzado ---
    "electrodoméstico","appliance", "home appliance", "cocina eléctrica", "microondas", "refrigerador",
    "bebida","drink", "beverage", "refresco", "jugo", "café", "té",

    # --- Seguridad doméstica ---
    "emergencia","emergency", "urgent situation", "accidente", "llamar ayuda",
    "primeros auxilios","first aid", "auxilio", "curación básica",
    "incendio","fire", "fuego", "accidente doméstico", "alarma",

    # --- Clima y fenómenos naturales ---
    "lluvia","rain", "heavy rain", "precipitación",
    "viento","wind", "breeze", "air flow",
    "terremoto","earthquake", "sismo", "temblor",

    # --- Oficina y documentos ---
    "documento","document", "file", "paper", "archivo",
    "correo","email", "mail", "mensaje", "inbox",
    "foto","photo", "image", "picture", "fotografía",

    # --- Tecnología general para civiles ---
    "celular","phone", "smartphone", "móvil", "android", "iphone",
    "computadora","computer", "pc", "laptop", "notebook",

    # --- Emociones adicionales ---
    "enojado","angry", "mad", "furious", "molesto",
    "relajado","relaxed", "calm", "tranquilo",
    "estresado","stressed", "anxious", "preocupado",

    # --- Conversación y expresión ---
    "mensaje","message", "text", "sms", "chat",
    "explicación","explanation", "clarification", "detalle",
    "historia","story", "tale", "narrative", "relato",

    # --- Objetos cotidianos ---
    "bolsa","bag", "purse", "saco", "mochila",
    "llave","key", "house key", "car key",
    "mesa","table", "desk", "mesón",
    "silla","chair", "seat",

    # --- Anime ---
    "anime","japanese animation", "animación japonesa", "otaku", "anime series", "anime show",
    "shonen","acción juvenil", "battle anime", "anime para jóvenes", "shounen",
    "shojo","romance anime", "anime para chicas", "shoujo",
    "isekai","otro mundo", "fantasy world anime", "isekai anime",
    "opening","op", "intro anime", "canción inicial",
    "ending","ed", "canción final", "ending theme",

    # --- Caricaturas ---
    "caricatura","cartoon", "animated show", "dibujos animados",
    "cartoon","serie animada", "caricatura americana", "cartoon network",
    "animado","animated", "dibujado", "animación",

    # --- Series (en general) ---
    "serie","tv show", "series", "episodios", "temporadas",
    "temporada","season", "t", "cycle",
    "episodio","episode", "capítulo", "ep", "cap",

    # --- Películas ---
    "pelicula","movie", "film", "cine", "largometraje",
    "actor","actor de cine", "film actor", "star",
    "directo","director", "filmmaker", "realizador",

    # --- Mangas / Manwhuas / Manhuas ---
    "manga","japanese comic", "comic japonés", "historieta japonesa",
    "manhwa","korean comic", "comic coreano", "manwhua",
    "manhua","chinese comic", "comic chino", "historieta china",
    "scan","scaneo", "raw", "capítulo escaneado",

    # --- Web Novels y Novelas ---
    "novela","novel", "story book", "literatura",
    "web novel","novela web", "historia online", "light novel",
    "light novel","ln", "novela ligera", "ficción japonesa",
    "libro","book", "ebook", "lectura", "volume",

    # --- Música ---
    "musica","music", "song", "audio", "melodía", "track",
    "cancion","song", "tema", "single",
    "album","disco", "álbum musical", "cd",
    "artista","musician", "cantante", "autor musical",

    # --- Arte ---
    "arte","art", "drawing", "painting", "creación artística",
    "pintura","paint", "artwork", "cuadro",
    "ilustración","illustration", "art digital", "dibujos",

    # --- Televisión ---
    "television","tv", "tele", "canal", "programa tv",
    "canal","channel", "station", "señal tv",
    "programa","show", "tv program", "transmisión",

    # --- Descargas y Servicios Gratuitos ---
    "gratis_mega","mega free", "link mega", "descarga mega", "mega.nz",
    "gratis_rapidshare","rapidshare", "descarga rápida", "host antigua",
    "gratis_google_drive","google drive", "gdrive", "link drive", "drive download",
    "descarga","download", "bajar archivo", "archivo descargable",

    # --- Libros / PDFs / Lectura ---
    "pdf","documento pdf", "archivo pdf", "ebook pdf",
    "ebook","digital book", "libro electrónico", "lectura digital",
    "biblioteca","library", "colección de libros", "book archive",

	# Términos técnicos/abreviaturas que no deben tratarse como faltas
    "ctrl", "alt", "shift", "esc", "tab", "enter", "space", "home", "end", "insert", "delete", "backspace",
    "pdf", "txt", "csv", "json", "xml", "html", "css", "js", "py", "pyw", "exe", "dll", "api", "gui", "ui", "ux",
    "qt", "pyqt", "pyqt5", "python", "opencv", "cv2", "numpy", "pillow", "pil", "flask", "sqlite", "sql",
    "github", "git", "windows", "linux", "android", "mouse", "scroll", "viewer", "image", "pro",
    "frontend", "backend", "cyberpunk", "neural", "link", "sensey",

	## 1. Tkinter
    # Widgets principales
    'Label', 'Entry', 'Canvas', 'Button', 'Checkbutton', 'Frame', 'LabelFrame', 'Listbox',
    'Menu', 'Menubutton', 'Message', 'OptionMenu', 'PanedWindow', 'Radiobutton', 'Scale', 'Scrollbar',
    'Spinbox', 'Text', 'Toplevel',
    # Diálogos y módulos auxiliares
    'colorchooser', 'filedialog', 'messagebox', 'simpledialog', 'font', 'scrolledtext', 'commondialog',
    # Variables Tkinter
    'StringVar', 'IntVar', 'DoubleVar', 'BooleanVar',
    # Otros
    'Tk', 'Misc', 'Wm', 'Variable', 'Event', 'PhotoImage', 'BitmapImage',

	## 2. CustomTkinter
    'CTk', 'CTkToplevel', 'CTkFrame', 'CTkScrollableFrame', 'CTkLabel', 'CTkButton', 'CTkCheckBox',
    'CTkRadioButton', 'CTkSwitch', 'CTkSlider', 'CTkProgressBar', 'CTkEntry', 'CTkComboBox',
    'CTkOptionMenu', 'CTkSegmentedButton', 'CTkTextbox', 'CTkTabview', 'CTkScrollbar', 'CTkCanvas',
    'CTkInputDialog',

	## 3. ttk
    'ttk_Button', 'ttk_Checkbutton', 'ttk_Combobox', 'ttk_Entry', 'ttk_Frame', 'ttk_Label', 
    'ttk_LabelFrame', 'ttk_Menubutton', 'ttk_Notebook', 'ttk_PanedWindow', 'ttk_Progressbar', 
    'ttk_Radiobutton', 'ttk_Scale', 'ttk_Scrollbar', 'ttk_Separator', 'ttk_Sizegrip', 'ttk_Spinbox', 
    'ttk_Treeview',

	## 4. PyQt5 — QtWidgets
    # Aplicación / ventanas
    'QApplication', 'QWidget', 'QMainWindow', 'QDialog', 'QDialogButtonBox', 'QWizard', 'QWizardPage',
    'QDockWidget', 'QMdiArea', 'QMdiSubWindow',
    # Botones
    'QPushButton', 'QToolButton', 'QRadioButton', 'QCheckBox', 'QCommandLinkButton',
    # Etiquetas / texto
    'QLabel', 'QLineEdit', 'QTextEdit', 'QPlainTextEdit', 'QTextBrowser',
    # Selección / entrada
    'QComboBox', 'QFontComboBox', 'QSpinBox', 'QDoubleSpinBox', 'QDateEdit', 'QTimeEdit', 'QDateTimeEdit',
    # Controles
    'QSlider', 'QDial', 'QScrollBar', 'QProgressBar', 'QLCDNumber',
    # Contenedores
    'QGroupBox', 'QFrame', 'QTabWidget', 'QTabBar', 'QStackedWidget', 'QToolBox', 'QScrollArea', 
    'QWidgetItem',
    # Listas / árboles / tablas
    'QListWidget', 'QListWidgetItem', 'QTreeWidget', 'QTreeWidgetItem', 'QTableWidget', 'QTableWidgetItem',
    # Vistas
    'QListView', 'QTreeView', 'QTableView', 'QColumnView', 'QHeaderView', 'QAbstractItemView',
    # Splitters
    'QSplitter', 'QSplitterHandle',
    # Layouts
    'QLayout', 'QBoxLayout', 'QVBoxLayout', 'QHBoxLayout', 'QGridLayout', 'QFormLayout', 'QStackedLayout',
    'QLayoutItem', 'QSpacerItem',
    # Menús / acciones
    'QMenu', 'QMenuBar', 'QAction', 'QActionGroup', 'QToolBar',
    # Estado / bandeja
    'QStatusBar', 'QSystemTrayIcon',
    # Diálogos
    'QFileDialog', 'QColorDialog', 'QFontDialog', 'QInputDialog', 'QMessageBox', 'QProgressDialog',
    # Calendario
    'QCalendarWidget',
    # Gráficos básicos
    'QGraphicsView', 'QGraphicsScene', 'QGraphicsItem', 'QGraphicsObject', 'QGraphicsWidget', 
    'QGraphicsPixmapItem', 'QGraphicsTextItem', 'QGraphicsLineItem', 'QGraphicsRectItem', 
    'QGraphicsEllipseItem', 'QGraphicsPolygonItem', 'QGraphicsPathItem', 'QGraphicsSimpleTextItem',
    # Propiedades / utilidades
    'QSizePolicy', 'QSpacerItem', 'QStyle', 'QStyleFactory', 'QAbstractButton', 'QAbstractSpinBox',
    'QAbstractSlider', 'QAbstractScrollArea', 'QButtonGroup',
    # Internacionalización
    'QLCDNumber',
    # Widgets especiales
    'QKeySequenceEdit', 'QFocusFrame', 'QToolTip', 'QWhatsThis', 'QDesktopWidget',

	## 5. PyQt5 — QtCore
    # Objetos / eventos
    'QObject', 'QEvent', 'QTimer', 'QBasicTimer', 'QTimerEvent', 'QCoreApplication', 'QEventLoop',
    'QAbstractEventDispatcher',
    # Hilos
    'QThread', 'QThreadPool', 'QRunnable', 'QMutex', 'QMutexLocker', 'QReadWriteLock', 'QReadLocker',
    'QWriteLocker', 'QSemaphore', 'QWaitCondition',
    # Archivos / dispositivos
    'QFile', 'QDir', 'QFileInfo', 'QFileInfoList', 'QIODevice', 'QBuffer', 'QSaveFile', 'QTemporaryFile',
    'QTemporaryDir', 'QDataStream', 'QTextStream',
    # Datos
    'QByteArray', 'QVariant', 'QBitArray', 'QDataStream',
    # Fechas
    'QDate', 'QTime', 'QDateTime', 'QTimeZone',
    # Geometría
    'QPoint', 'QPointF', 'QSize', 'QSizeF', 'QRect', 'QRectF', 'QMargins', 'QMarginsF', 'QLine',
    'QLineF', 'QVector2D', 'QVector3D', 'QVector4D',
    # URLs / MIME
    'QUrl', 'QUrlQuery', 'QMimeData',
    # Configuración
    'QSettings',
    # Procesos
    'QProcess', 'QProcessEnvironment',
    # JSON
    'QJsonDocument', 'QJsonObject', 'QJsonArray', 'QJsonValue',
    # Regex
    'QRegExp', 'QRegularExpression', 'QRegularExpressionMatch',
    # Modelos
    'QAbstractItemModel', 'QAbstractListModel', 'QAbstractTableModel', 'QAbstractProxyModel', 'QSortFilterProxyModel',
    # Utilidades
    'QItemSelection', 'QItemSelectionModel', 'QModelIndex', 'QPersistentModelIndex',
    # Qt
    'Qt', 'QMetaObject', 'QMetaClassInfo', 'QMetaMethod', 'QMetaProperty', 'QMetaType',
    # Decoradores PyQt
    'pyqtSignal', 'pyqtSlot', 'pyqtProperty',

	## 6. PyQt5 — QtGui
    # Imágenes
    'QImage', 'QPixmap', 'QBitmap', 'QPicture', 'QMovie',
    # Iconos / cursor
    'QIcon', 'QCursor',
    # Colores
    'QColor', 'QPalette',
    # Fuentes
    'QFont', 'QFontDatabase', 'QFontInfo', 'QFontMetrics', 'QFontMetricsF',
    # Pintura
    'QPainter', 'QPainterPath', 'QPen', 'QBrush', 'QGradient', 'QLinearGradient', 'QRadialGradient',
    'QConicalGradient',
    # Transformaciones
    'QTransform', 'QMatrix4x4', 'QQuaternion',
    # Texto
    'QTextCursor', 'QTextDocument', 'QTextBlock', 'QTextCharFormat', 'QTextBlockFormat', 'QTextListFormat',
    'QTextFrameFormat', 'QTextTableFormat', 'QTextImageFormat', 'QTextLength', 'QTextOption',
    # Resaltado
    'QSyntaxHighlighter',
    # Teclado / entrada
    'QKeySequence', 'QKeyEvent', 'QMouseEvent', 'QWheelEvent', 'QTabletEvent', 'QInputMethodEvent',
    # Drag & Drop
    'QDrag', 'QMimeData',
    # Animación
    'QStandardItem', 'QStandardItemModel',
    # Model/View
    'QAbstractTextDocumentLayout', 'QAbstractItemModel',
    # Otros
    'QRegion', 'QPolygon', 'QPolygonF', 'QPageLayout', 'QPageSize'

	## 7. PyQt5 — QtMultimedia
    'QCamera', 'QCameraInfo', 'QCameraImageCapture', 'QCameraViewfinder', 'QCameraViewfinderSettings',
    'QMediaPlayer', 'QMediaContent', 'QMediaPlaylist', 'QMediaRecorder', 'QAudioRecorder', 'QAudioInput',
    'QAudioOutput', 'QAudioFormat', 'QAudioDeviceInfo', 'QAudioProbe', 'QVideoProbe', 'QVideoFrame',
    'QVideoSurfaceFormat', 'QAbstractVideoSurface', 'QVideoWidget', 'QMediaMetaData', 'QRadioTuner',
    'QSound', 'QSoundEffect',

	## 8. PyQt5 — QtNetwork
    'QNetworkAccessManager', 'QNetworkRequest', 'QNetworkReply', 'QNetworkCookie', 'QNetworkCookieJar',
    'QNetworkInterface', 'QNetworkAddressEntry', 'QHostAddress', 'QHostInfo', 'QNetworkProxy',
    'QNetworkProxyQuery', 'QNetworkSession', 'QNetworkConfiguration', 'QNetworkConfigurationManager',
    'QSslSocket', 'QSslCertificate', 'QSslKey', 'QSslCipher', 'QAuthenticator', 'QHttpMultiPart',
    'QHttpPart', 'QAbstractSocket', 'QTcpSocket', 'QTcpServer', 'QUdpSocket', 'QLocalSocket', 
    'QLocalServer',

	## 9. PyQt5 — QtSql
    'QSqlDatabase', 'QSqlQuery', 'QSqlQueryModel', 'QSqlTableModel', 'QSqlRelationalTableModel', 
    'QSqlRecord', 'QSqlField', 'QSqlIndex', 'QSqlRelation', 'QSqlError', 'QSqlDriver', 'QSqlResult',

	## 10. PyQt5 — QtPrintSupport
    'QPrinter', 'QPrintDialog', 'QPrintPreviewDialog', 'QPrintPreviewWidget', 'QPageSetupDialog',

	## 11. PyQt5 — QtXml
    'QDomDocument', 'QDomElement', 'QDomNode', 'QDomNodeList', 'QDomAttr', 'QDomText', 'QDomComment',
    'QDomCDATASection', 'QDomDocumentType', 'QDomEntity', 'QDomEntityReference', 
    'QDomProcessingInstruction', 'QDomCharacterData', 'QXmlReader', 'QXmlContentHandler', 
    'QXmlDTDHandler', 'QXmlDeclHandler', 'QXmlDefaultHandler', 'QXmlEntityResolver', 'QXmlErrorHandler', 
    'QXmlLexicalHandler', 'QXmlLocator',

	## 12. Módulos estándar de Python
    # Sistema
    'os', 'sys', 'shutil', 'pathlib', 'glob', 'fnmatch', 'stat', 'filecmp', 'tempfile',
    # Procesos
    'subprocess', 'multiprocessing', 'threading', 'queue', 'asyncio', 'concurrent',
    # Fechas
    'datetime', 'calendar', 'time',
    # Datos
    'json', 'csv', 'sqlite3', 'pickle', 'shelve', 'dbm',
    # Texto
    'string', 're', 'textwrap', 'difflib', 'unicodedata',
    # Matemáticas
    'math', 'cmath', 'decimal', 'fractions', 'random', 'statistics',
    # Funcional
    'functools', 'itertools', 'operator',
    # Colecciones
    'collections', 'heapq', 'bisect', 'array',
    # Compresión
    'zipfile', 'tarfile', 'gzip', 'bz2', 'lzma', 'zlib',
    # Internet / red
    'urllib', 'http', 'socket', 'email', 'ftplib', 'smtplib', 'imaplib', 'poplib',
    # HTML / XML
    'html', 'xml', 'html.parser',
    # Seguridad / hashes
    'hashlib', 'hmac', 'secrets', 'ssl',
    # Sistema / hardware
    'platform', 'ctypes', 'errno', 'signal', 'resource',
    # Depuración
    'logging', 'traceback', 'warnings', 'pdb', 'profile', 'timeit',
    # Programación
    'abc', 'dataclasses', 'enum', 'typing', 'types', 'inspect', 'importlib', 'ast', 'dis', 'keyword', 
    'builtins',
    # Consola
    'argparse', 'cmd', 'getopt', 'readline',
    # Utilidades
    'copy', 'pprint', 'contextlib', 'io', 'weakref', 'gc', 'sysconfig', 'configparser', 'gettext',

    ## Módulos estándar de Python para terceros
    'PyQt5', 'customtkinter', 'PIL', 'cv2', 'numpy', 'pandas', 'matplotlib', 'requests', 'flask',
    'django', 'bs4', 'selenium', 'playwright', 'cryptography', 'paramiko', 'openpyxl', 'PyPDF2',
    'pymediainfo', 'psutil',

    ## Diccionario de Solo Nombres Propios
    'Aaron', 'Abasi', 'Abayomi', 'Abdalla', 'Abd-allah', 'Abdallah', 'Abdelahi', 'Abdkelkader',
    'Abdías', 'Abdi', 'Abdikarim', 'Abdiraxman', 'Abdón', 'Abebe', 'Abel', 'Abelardo',
    'Aberto', 'Abiel', 'Abihú', 'Abimael', 'Abiram', 'Abishai', 'Abner', 'Abrafo',
    'Abraham', 'Abram', 'Abramo', 'Absalón', 'Abshalom', 'Abubakar', 'Adael', 'Adalberto',
    'Adam', 'Adán', 'Adan', 'Adar', 'Addo', 'Adeben', 'Adel', 'Adelardo',
    'Adelio', 'Adelmo', 'Ademar', 'Adiel', 'Adif', 'Adín', 'Adino', 'Adi',
    'Adisa', 'Adiv', 'Adjatay', 'Admiel', 'Adofo', 'Adolfo', 'Adom', 'Adonai',
    'Adonis', 'Adrián', 'Adriano', 'Adriel', 'Adrik', 'Adwin', 'Afework', 'Afeworki',
    'Afram', 'Agamenón', 'Agapito', 'Agenor', 'Ageo', 'Agramant', 'Agrican', 'Aguinaldo',
    'Agur', 'Agustín', 'Agymah', 'Ahmad', 'Ahmadou', 'Ahriman', 'Ahuv', 'Ahuviá',
    'Aitor', 'Ajab', 'Aján', 'Ajidan', 'Ajiel', 'Ajiezer', 'Ajimán', 'Ajiram',
    'Ajishar', 'Ajitov', 'Ajshalom', 'Akello', 'Akhenaten', 'Aka', 'Alkiki', 'Al',
    'Akin', 'Akáns', 'Akinsanya', 'Akintunde', 'Akinwole', 'Akinyemi', 'Aladino', 'Alafin',
    'Alain', 'Alán', 'Alarico', 'Albano', 'Alberico', 'Alberto', 'Albino', 'Alcibíades',
    'Alcides', 'Aldemar', 'Aldetrudis', 'Aldo', 'Alejandro', 'Alejo', 'Alek, Alik, Aleksandr, Aleksis, Aleksi, Alexei', 'Aleron',
    'Alessandro', 'Alex', 'Alexandre', 'Alexis', 'Alfio', 'Alfonso', 'Alfredo', 'Algernon, Algrenon',
    'Alí', 'Ali', 'Aliz', 'Almagor', 'Almodis', 'Aloin, Aluin', 'Alón', 'Alonso',
    'Aloyoshenka, Aloysha', 'Alpha', 'Alvar', 'Alvaro', 'Amadeo', 'Amador', 'Amal', 'Aman',
    'Amancio', 'Amando', 'Amaranto', 'Amare', 'Amari', 'Amaru', 'Amaury', 'Amazu',
    'Ambrosi', 'Ambrosio', 'Amen, Amun, Ammon', 'Amenhotep', 'Amenophis', 'Amenra', 'Américo', 'Amiel',
    'Amiezer', 'Amijai', 'Amilcar', 'Amintor', 'Amior', 'Amir', 'Amiram', 'Amishalom',
    'Amishar', 'Amitai', 'Egipcio', 'Anacleto', 'Anán', 'Anan', 'Anastagio', 'Anastasio',
    'Anatoli', 'Anatolio', 'André', 'Andrea', 'Andrés', 'Andrusha, Andrya, Andrei', 'Angel', 'An-her, Anhur',
    'Aníbal', 'Aniceto', 'Anscario', 'Ansel, Ancil, Acel, Ansell', 'Anselmo', 'Antenor', 'Antón', 'Antonio',
    'Ant', 'Antosha, Antinko, Anton', 'Anubis, Anpus', 'Anum', 'Anwar', 'Anzety', 'Aparicio', 'Apis',
    'Apolo', 'Apophis', 'Aquiles', 'Aquilino', 'Aram', 'Arbel', 'Arber', 'Arcadio',
    'Arcángel', 'Archaimbaud, Archambault, Archenbaud', 'Archard', 'Archibaldo', 'Arduino', 'Arelí', 'Aren', 'Argentino',
    'Argimiro', 'Ari', 'Ariel', 'Arístides', 'Aristóbulo', 'Aristóteles', 'Arman', 'Armand',
    'Armando', 'Armanno', 'Arnaldo', 'Arnaud', 'Arno', 'Arnoldo', 'Arnou, Arnoux', 'Arnulfo',
    'Arquímedes', 'Arridano', 'Arrigo, Aroghetto, Alrigo', 'Arsenio', 'Artemio', 'Arturo', 'Artus', 'Artzi',
    'Asad', 'Asael', 'Asaf', 'As', 'Asante', 'Asdrúbal', 'Asher', 'Ashtaroth',
    'Ashur', 'Asiel', 'Asim', 'Assefa', 'Astolpho', 'Aswad', 'Ata', 'Atahualpa',
    'Atemu', 'Aten', 'Atila', 'Atlantes', 'Atsu', 'Atu', 'Atum', 'Atur',
    'Atzel', 'Aubert', 'Aubrey, Albaric', 'Audric,Aldrick, Aldrich', 'Augusto', 'Aureliano', 'Aurelio', 'Aurivlle',
    'Ausar Egipcio', 'Avdel', 'Avelino', 'Avenall, Avenelle, Aveneil', 'Avent, Advent', 'Avidor', 'Aviezri', 'Avimael',
    'Avimelej', 'Avinatán', 'Aviramv', 'Aviraz', 'Avishajar', 'Avitzedek', 'Awner', 'Awar',
    'Axel', 'Ayman', 'Aymon', 'Ayub', 'Ayubu', 'Azael', 'Azai', 'Azare',
    'Azariá', 'Azarias', 'Azariel', 'Azazael', 'Azekel', 'Azi', 'Azibo', 'Aziz',
    'Aizi', 'Avizi', 'Azul', 'Baal', 'Babafemi', 'Babatunde', 'Babu', 'Babukar',
    'Badru', 'Badu', 'Bailey, Bayley', 'Bak', 'Balbino', 'Baldassare, Baldassario', 'Baldomero', 'Baldovino',
    'Bald', 'Balisarda', 'Baltasar', 'Baltazar', 'Bankole', 'Bareh', 'Barnabás', 'Barry, Barrie',
    'Bartlett', 'Bartolomé', 'Baruc', 'Baruj', 'Baruti', 'Basel', 'Basem', 'Basilio',
    'Bassey', 'Bautista', 'Bayard', 'Beaufort', 'Beb, Bebti, Babu, Baba', 'Behdeti', 'Bekele', 'Belén',
    'Belisario', 'Bellamy, Bell', 'Belmiro', 'Beltane', 'Beltrán', 'Beluchi', 'Ben', 'Benaiá',
    'Benedicto', 'Beniamino', 'Benicio', 'Benigno', 'Benito', 'Benjamín', 'Berhanu', 'Berihun',
    'Bernabé', 'Bernardo', 'Bertoldo', 'Bertrán', 'Bertrand', 'Bertrando, Brando', 'Bes', 'Betel',
    'Betue', 'Bevis, Beauvais', 'Bilial', 'Blas', 'Boaz', 'Bobo', 'Bogdashka, bohdan', 'Bolaji',
    'Bolodenka', 'Bomani', 'Bonifacio', 'Borya, Boryenka, Boris', 'Braulio', 'Brencis', 'Brody', 'Brian',
    'Brice', 'Brigliadoro', 'Bruce, Brys', 'Brunelle', 'Bruno', 'Buenaventura', 'Burkett, Burcet', 'Burnell, Burel',
    'Burrell', 'Buz', 'Burian', 'Bwana', 'Byron', 'Byron, Buiron', 'Caín', 'Cainán',
    'Caleb', 'Calígula', 'Calixto', 'Calvino', 'Camara', 'Camilo', 'Campbell', 'Cándido',
    'Carim', 'Carlino, Carlo', 'Carlos', 'Charlus', 'Carmelo', 'Carolos, Carlo, Carolus, Carlos, Carel', 'Casandro', 'Caseareo, Ceasario, Cesare',
    'Casiano', 'Casildo', 'Casimiro', 'Casio', 'Cástor', 'Catón', 'Cayetano', 'Cecilio',
    'Cefas', 'Ceferino', 'Celedonio', 'Celso', 'César', 'Cesáreo', 'Cesario', 'Chafulumisa',
    'Chandler, Chanler', 'Channing', 'Chapin', 'Chappell, Chappel', 'Charbel', 'charif', 'Charles, Cearbhall', 'Charlot',
    'Chatha', 'Chatuluka', 'chauki', 'Cheikh', 'Cheney', 'Chenzira', 'Cheops', 'Cheslaw',
    'Chibale', 'Chigaru', 'Chike', 'Chinua', 'Chisisi', 'Christian', 'Christien, Cretien', 'Chueri',
    'Chuma', 'Cicerón', 'Cid', 'Cipriano', 'Giríaco', 'Cirilo', 'Ciro', 'Claudio',
    'Claus', 'Clemente', 'Clodomiro', 'Cloridan', 'Clovis', 'Cono', 'Conrado', 'Constancio',
    'Constantino', 'Cori', 'Cornelio', 'Cosme', 'Courtland, Courtney, Court, Curt, Courtnay, Cort', 'Crisólogo', 'Crisóstomo', 'Crístian o Christian',
    'Cristóbal', 'Cristoforo', 'Cruz', 'Curtis, Curtice, Curcio', 'Cusi', 'Dabir', 'Dagoberto', 'Dakarai',
    'Dalmacio', 'Dalmar', 'Dalmiro', 'Dámaso', 'Damián', 'Damocles', 'Dan', 'Daniachew',
    'Daniel', 'Daniele', 'Danilo', 'Danso', 'Dante', 'Danya', 'Deniska', 'Dima',
    'Dimitri', 'Darcy, D-arcy', 'Dardo', 'Daren', 'Darío', 'Darius', 'Darwishi', 'Davet',
    'David', 'davide', 'Dawit', 'Delaiá', 'Delfín', 'Delmar, Delmer', 'Demetrio', 'Demián',
    'Demissie', 'Demécrito', 'Demóstenes', 'Denis, Dennis, Denys, Dennet', 'Denis', 'Deodato', 'Desiderio', 'Desire, Didier',
    'Desta', 'Dexter', 'Día', 'Didier', 'Diego', 'Diji', 'Dino', 'Diógenes',
    'Dionisio', 'Dióscoro', 'Djoser', 'Domiciano', 'Domicio', 'Domingo', 'Donatello, Donato', 'Donatien',
    'Donato', 'Donkor', 'Dorcas', 'Doroteo', 'Duilio', 'Dzigbode', 'Eabrizio', 'Eabroni',
    'Ebenezer', 'Éber', 'Eberardo', 'Ebo', 'Edelmar', 'Edelmiro', 'Edet', 'Edgar',
    'Edgardo', 'Edik, Eduard', 'Egor', 'Evgenii', 'Edipo', 'Edmondo', 'Edmundo', 'Eduardo',
    'Eduardo, Edoardo', 'Effiom', 'Efraim', 'Efraín', 'Efrén', 'Egidio', 'Egisto', 'Eladio',
    'Elbio', 'Eleazar', 'Elenio', 'Eleodoro', 'Eleuterio', 'Eliahu', 'Elías', 'Eliecer',
    'Eliezer', 'Elifelet', 'Elihú', 'Elimu', 'Elio', 'Eliot, Eliot, Elliot', 'Eliseo', 'Eliud',
    'Elmer', 'Elmo', 'Eloy. Francés', 'Elpidio', 'Eluney', 'Elvio', 'Emanuel', 'Emeterio',
    'Emiliano', 'Emilio', 'Emir', 'Emmanuel', 'Enea', 'Eneas', 'Enoc', 'Enoch',
    'Enosh', 'Enrico, Enzo', 'Enrico', 'Enrique', 'Enzo', 'Epicuro', 'Epifanio', 'Erán',
    'Erasmo', 'Erasto', 'Eric', 'Erico', 'Ermanno', 'Ernesto', 'Eros', 'Enwin',
    'Esau', 'Esav', 'Esculapio', 'Esdrás', 'Esopo', 'Espartaco', 'Essien', 'Estanislao',
    'Este', 'Esteban', 'Etel', 'Ethán', 'Etienne', 'Ettore', 'Euclides', 'Eudoxio',
    'Eufrasio', 'Eugenio', 'Euladio', 'Eulalio', 'Eulogio', 'Eusebio', 'Eustacio o Eustasio', 'Eustaquio',
    'Evaristo', 'Evelio', 'Everardo', 'Eyén', 'Exeji', 'Ezequías', 'Ezequiel', 'Ezra',
    'Fabián', 'Fabio', 'Fabio, Fabiano', 'Fabiyan, Fabi', 'Fabricio', 'Facundo', 'Fadeyka, Fadey, Faddei', 'Fadi',
    'Fadil', 'Faki', 'Farajj', 'Fares', 'Farid', 'Faust, Fausto, Fel', 'Fausto', 'Favio',
    'Febo', 'Federico', 'Fedor, Fedya, Fyodor, Fedyenka', 'Fedor', 'Fedro', 'Fedyenka, Fyodor', 'Feliciano', 'Feliks',
    'Felipe', 'Felix', 'Fenuku', 'Fenyang', 'ferdinando', 'Fermín', 'Fernán', 'Fernando',
    'Fernando III', 'España', 'Ferragus', 'Ferrau', 'Fidel', 'Fidelio', 'Fiers', 'Fiberto',
    'Filip', 'Filippo, Filippio', 'Fiorello', 'Fitz', 'Flavio', 'Fletcher', 'Floreal', 'Florencio',
    'Fiorián', 'Florio', 'Florismart', 'Florus', 'Fodjour', 'Foma', 'Forrest', 'Fortun, Fortune',
    'Fortunato', 'Fouad o Fuad', 'Francesco', 'Francisco', 'Franco', 'Frank', 'Fredek', 'Froilán',
    'Frontino', 'Fructuoso', 'Fulgencio', 'Fulvio', 'Funsani', 'Fynn', 'Fyodor', 'Gabino',
    'Gabra, Gebre', 'Gabriel', 'Gabriele', 'Gad', 'Gadi', 'Gadiel', 'Gaeta', 'Gaetano',
    'Gahiji', 'Galileo', 'Galo Latín, Gallus', 'Gamaliel', 'Gandolfo', 'Ganelon, Gan', 'Gano', 'Garai',
    'García', 'Garcilaso', 'Garibaldo', 'Garland', 'Gaspar', 'Gaspar, Gaspard', 'Gastón', 'Gaston, Gascon',
    'Gaudencio', 'Gauthier, Gautier', 'Gavril', 'Geb', 'Genaro o Jenaro', 'Geoffrey', 'Georgio, Giorgio', 'Geraldo',
    'Gerardo', 'Germain, Germano', 'Germán', 'Germinal', 'Geroni', 'Gershom', 'Gershón', 'Gervasio',
    'Gesualdo', 'Getachew', 'Geteye', 'Getulio', 'Ghedi', 'Giacomo', 'Gian, Giovanni', 'Giancarlo',
    'Gifford, Guifford', 'Gil', 'Gilberto', 'Gildardo', 'Gill, Gil', 'Gino', 'Giorgio', 'Giovanni',
    'Giuliano, Giulio', 'Giuseppe', 'Godofredo', 'Gogo:', 'Gomer', 'Gonzalo', 'Gotardo', 'Gracián',
    'Gradasso', 'Granville, Grenvill', 'Gregorio', 'Grisha, Grigori, Grigorii', 'Grosvenor', 'Gualberto', 'Gualterio', 'Gualtiero, Galtero, Galterio',
    'Guedado', 'Guerin', 'Guglielmo', 'Guideón', 'Guido', 'Guilead', 'Guillermo', 'Gumersindo',
    'Gustavo', 'Guy', 'Gyamtfi', 'Gyasi', 'Habacuc', 'Habib', 'Hageo', 'Hagos',
    'Haji', 'Hakim', 'Hakizimana', 'Ham', 'Hamadi', 'Hamilton', 'Hanbal', 'Hani',
    'Hanif', 'Hapi', 'Hapu', 'Harakhty', 'Harbin', 'Harcourt', 'Hardouin', 'Haroldo',
    'Hasani', 'Hassan', 'Heber', 'Héctor', 'Hedeon', 'Helge', 'Heh', 'Heliodoro',
    'Henry', 'Heráclito', 'Heraldo', 'Heriberto', 'Hermán', 'Hermenegildo', 'Hermes', 'Herminio',
    'Hernán', 'Hernando', 'Herodes', 'Heródoto', 'Heru', 'Hervé', 'Higinio', 'Hilario',
    'Hillel', 'Hipólito', 'Hipólita', 'Hiram', 'Hogan', 'Homero', 'Hondo', 'Honorato',
    'Horacio', 'Horemheb', 'Hortensio', 'Horus', 'Hosea', 'Hu', 'Huberto', 'Huenu',
    'Hugh', 'Hugo', 'Huldá', 'Humberto', 'Husani', 'Hussein', 'Iadón', 'Iajín',
    'Ialeel', 'Iamín', 'Ian', 'Iazeel', 'Ibrahim', 'Icabod', 'Idogbe', 'Idrissa',
    'Iedidiá', 'Iejiel', 'Ignace', 'Ignacio', 'Igor', 'Igoryok, Igor', 'Iiya', 'Iian',
    'Ildefonso', 'Imanol', 'Inca', 'Indalecio', 'Ini-herit', 'Iniko', 'Innocenzio', 'Inocencio',
    'Inti', 'Iñaki', 'Iñigo', 'loachime', 'Ioakim', 'Iojanán', 'Iosef', 'Ireneo',
    'Irving', 'Isaac', 'Isaiah', 'Isaías', 'Ishag', 'Ishboshet', 'Ishmael', 'Ishmer',
    'Isidoro', 'Isidro', 'Iskinder', 'Ismael', 'Israel', 'Issa', 'Issachar', 'Issmat',
    'Italo', 'Itamar', 'Ithamat', 'Itzjac', 'Iván', 'Ivan', 'Iven', 'Jabari',
    'Jabel', 'Jabín', 'Jacinto', 'Jacob', 'Jacobo', 'Jacques, Jacquelin', 'Jacques', 'Jad o Yad',
    'Jafari', 'Jafet', 'Jahi', 'Jaime', 'Jair', 'Jairo', 'Jaja', 'Jaled',
    'Jalil', 'Janina', 'jJano', 'jJared', 'jJasón', 'jJavier', 'jJavilá', 'jJawara',
    'Jay, Jaye', 'jJazael', 'Jean', 'Jefté', 'Jehová', 'Jela', 'Jenaro', 'Jenofonte',
    'Jeofíroi, Jeffrey', 'Jeremías', 'Jeremiel', 'Jermija', 'Jerónimo', 'Jerusalén', 'Jesabel o Jezabel', 'Jesé',
    'Jesper, Jasper', 'Jesualdo', 'Jesús', 'Jethró', 'Jibade', 'Jimiyu', 'Jjiri', 'Joab',
    'Joachim', 'Joaquín', 'Job', 'Joel', 'Jomo', 'Jonás', 'Jonatan o Jonathan', 'Jonathan',
    'Jordán', 'Jorge', 'Josafat', 'José', 'Josías', 'Jotham', 'Jov', 'Juan',
    'Jubal', 'Judás', 'Jules, Julian, Jullien', 'Julián', 'Julio', 'Juma', 'Jumoke', 'Jurg,Jeirgif',
    'Justiniano', 'Justino', 'Justo', 'Juvenal', 'Juventino', 'Kafele', 'Kalid', 'Kalil',
    'Kamuzu', 'Kaphiri', 'Kareb', 'Karel', 'Karlens, Karlitis', 'Karim', 'Karolek, Karol', 'Kasiya',
    'Kazemde', 'Kek', 'Kenán', 'Kenaniá', 'Kerman', 'Kevin', 'Khafra', 'Khaldun, khalid',
    'Khalfani', 'Khentimentiu', 'Khepri', 'Khnemu', 'Khnum', 'Khons', 'Khufu', 'Kim',
    'Kiryl, Kril', 'Kneph', 'Kolenka, Kolya', 'Kontar', 'Kosey', 'Kostenka, Kostya, Konstantine', 'Labán', 'Labib',
    'Ladislao', 'Lahual', 'Lamech', 'Lance, Lancelot, Launcelot, Lancelin', 'Landers, Landis', 'Landolfo', 'Langley, Langley', 'Lateef',
    'Latimer', 'Laureano', 'Laurentij', 'Lauro', 'Lautaro', 'Lázaro', 'Leal', 'Leandro',
    'Legget', 'Lelio', 'Lemuel', 'Leo', 'Leobardo', 'Leocadio', 'León', 'Leon, Leone, Leonce, Leocadie, Leodegrance',
    'Leonardo', 'Leoncio', 'Leonel', 'Leonelo', 'Leónidas', 'Leonide, Lenya, Lyonechka, Levushka, Levka, Lyonya, Lev, Levka', 'Leonides', 'Leopoldo',
    'Leroy', 'Leuco', 'Leverett, Leveret', 'Levi', 'Levy', 'Liber', 'Liberal', 'Liberato',
    'Liborio', 'Licurgo', 'Lihue', 'Lino', 'Lisandro', 'Lisimba', 'Lisístrato', 'Livio',
    'Lorenzo', 'Loring', 'Lot', 'Lotario', 'Lothair', 'Louis', 'Lowell, Lovell, Lowe, Louvel', 'Loyal',
    'Lucas', 'Luciano', 'Lucio', 'Ludovico', 'Luigi', 'Luis', 'Lukasha, Lukyan, Luka', 'Lukman',
    'Luzige', 'Lyle, Lisle', 'Macabeo', 'Macario', 'Macedonio', 'Macto', 'Madus', 'Mahlá',
    'Mahlí', 'Mahoma', 'Mainque', 'Makalani', 'Maks, Maksimillan', 'Malagigi', 'Malaji', 'Malaquías',
    'Malco', 'Mallory, Mailhairer', 'Mamerto', 'Mampu', 'Mandel, Mantel', 'Manfredo', 'Manlio', 'Manu',
    'Manuel', 'Manville, Manneville', 'Manzur', 'Marc', 'Marcelino', 'Marcello, Marco', 'Marcelo', 'Marcelo Latín, Marcellus, diminutivo de marcus, o sea Marco',
    'Marcial Latín, Martialis, adjetivo de Mars, o sea Marte', 'Marcial', 'arcio', 'Marco', 'Marcos', 'Mariano', 'Marino', 'Mario',
    'Marlon', 'Marmion', 'Marón', 'Marshall, Marshal, Marsh', 'Marsillus', 'Martín', 'Martiniano', 'Martino',
    'Marwan o Maruan', 'Maskini', 'Maslin, Masselin', 'Mason, Masson', 'Masud', 'Matan', 'Mateo', 'Matías',
    'Matitiahu', 'Matsimela', 'Matteo', 'Matvey, Motka, Matyash', 'Mauricio', 'Maurizio', 'Mauro', 'Max',
    'Maximiano', 'Maximino', 'Máximo', 'Mayhew, Mahieu', 'Mbizi', 'Medardo', 'Medoro', 'Melchor',
    'Melecio', 'Melibeo', 'Melitón', 'Melquíades', 'Melville, Malleville', 'Memphis', 'Menajem', 'Menandro',
    'Menashé', 'Menes', 'Menkaura', 'Mensah', 'Mentor', 'Mercer', 'Mercurio', 'Merle',
    'Merlin, Merlion', 'Meshulam', 'Metushelaj', 'Micael', 'Michael', 'Michel', 'Michel, Michele', 'Michelangelo',
    'Michele, Michel', 'Midas', 'Miguel', 'Mijá', 'Mijael', 'Mijaiá', 'Mikizli', 'Milcíades',
    'Millard', 'Milton', 'Min', 'Minkah', 'Mishenka, Mishe, Misha, Mikhail', 'Modesto', 'Mohamed', 'Moisés',
    'Montague, Montaigu', 'Month', 'Moore, More, Moor', 'Mordejal', 'Morfeo', 'Moriz', 'Mosegi', 'Moshé',
    'Mosi', 'Moswen', 'Msamaki', 'Mstrah', 'Mudada', 'Mukhwana', 'Munir', 'Musa',
    'Muslim', 'Mustafá', 'Nabor', 'Nabucodonosor', 'Nader', 'Nadim', 'Nadir', 'Nacem',
    'Naftal', 'Nahuel', 'Nahum', 'Naim', 'Najja', 'Najor', 'Namo', 'Napoleón',
    'Narciso', 'Narmer', 'Nassor', 'Natal', 'Natalio', 'Natán', 'Natanael', 'Nataniel',
    'Nathanael', 'Nayi', 'Nazareno', 'Nazaret o Nazareth', 'Nazario', 'Neb-ertcher', 'Nefertum', 'Neftalí',
    'Nehemías', 'Nehuén', 'Nelson', 'Nemesio', 'Nephthys', 'Neptuno', 'Nereo', 'Neriá',
    'Nerón', 'Nestor', 'Neville, Neuveville', 'Nexeu', 'Neyén', 'Ngori', 'Nicandro', 'Nicanor',
    'Nicasio', 'Nicéforo', 'Nicolai, Nikita', 'Nicolás', 'Nicomedes', 'Niu', 'Nizam', 'Nhosi',
    'Nkrumah', 'Nkuku', 'Noah', 'Noaj', 'Nog', 'Noel', 'Nolasco', 'Norberto',
    'Norman', 'Normand, Norman, Norm', 'Normando', 'Norris, Norice, Noreis', 'Nouel', 'Numa', 'Nun', 'Nurus',
    'Oba', 'Obadiá', 'Octave', 'Octavio', 'Odion', 'Odo', 'Odon', 'Ofrá',
    'Ogier', 'Okpara', 'Olaf', 'Oleg, Olezka', 'Olegario', 'Oliver', 'Oliverio', 'Olivier',
    'Omar', 'Omari', 'Onan', 'Onésimo', 'Onfroi', 'Onofre', 'Onuris', 'Orestes',
    'Orfeo', 'Orlando', 'Orson, Ourson', 'Orville', 'Osahar', 'Osaze', 'Oscar', 'Osías',
    'Osiris, Un-nefer', 'Osmán', 'Osmar', 'Osmaro', 'Osmundo', 'Osvaldo', 'Osvan', 'Otelo',
    'Othniel', 'Otón', 'Otoniel', 'Ottah', 'Oubastet, Bastet', 'Ovidio', 'Pablo', 'Paciente',
    'Pacífico', 'Pacomio', 'Page, Paige, Padgett, Paget', 'Paien', 'Paki', 'Pampín', 'Pancracio', 'Pánfilo',
    'Pantaleón', 'Paolo', 'Parfait', 'París', 'Parménides', 'Pascal, Pascual, Pasquale', 'Pascual', 'Pashenka',
    'Pavlow', 'Pasquale, Pascal, Pascual', 'Pastor', 'Patricio', 'Patrick', 'Patrizio', 'Paul', 'Paulino',
    'Paulo', 'Pedro', 'Pehuén', 'Pehuen', 'Pepin, Pippin', 'Percy, Percival', 'Pericles', 'Perrin, Perren, Perryn, Perry, Pierre',
    'Petenka, Pyotr, Petya', 'Petiri', 'Petronio', 'Peverell, Piperel, Pepperell', 'Philip, Philippe, Philipe', 'Piero, Pietro', 'Pierpont, Pierrepont', 'Pili',
    'Pinabel', 'Pinjás', 'Pío', 'Pippino, Peppino', 'Piuque', 'Plácido', 'Platón', 'Platt, Plat',
    'Plauto', 'Plinio', 'Policarpo', 'Polifemo', 'Pomeroy, Pommeraie', 'Pompeyo', 'Porter, Portier, Porteur', 'Poseidón',
    'Ppsamtic', 'Prewitt, Pruit, Preruet, Pruet, Pruie', 'Príamo', 'Prilidíano', 'Primo', 'Procopio', 'Prometeo', 'Próspero',
    'Prudencio', 'Pryor, Priour', 'Psusennes', 'Ptah', 'Ptolemy', 'Publio', 'Qeb', 'Quaashie',
    'Quennel, Quesnel', 'Querubín', 'Quillén', 'Quillen', 'Quimey', 'Quincy, Quincey', 'Quintiliano', 'Quintílo',
    'Quintín', 'Quinto', 'Qurino', 'Ra', 'Rabican', 'Rachid', 'Rafael', 'Rafaele, Raphael, Rafaello',
    'Rafic', 'Raimondo', 'Raimundo', 'Rainero', 'Raiquen', 'Ramiro', 'Ramón', 'Ramses',
    'Ramzi', 'Randolfo', 'Ranger, Rainger', 'Raoul', 'Rashidi', 'Raúl', 'Ray, Roy, Rey, Rui, Royal', 'Re',
    'Reginaldo', 'Régulo', 'Re-harakhty', 'Reinaldo', 'Remigio', 'Remo', 'Remy, Remi', 'Renato',
    'René', 'Renzo', 'Reshef', 'Restituto', 'Reuel', 'Reuquén', 'Reynaldo', 'Ricardo',
    'Riccardo, Ricciardo', 'Rigoberto', 'Rinaldo', 'Robertino', 'Roberto', 'Robustiano', 'Roch, Roche, Rocke', 'Rodolfo',
    'Rodrigo', 'Rogelio', 'Roger', 'Rolán', 'Rolando', 'Romain', 'Román', 'Romelio',
    'Romeo', 'Romildo', 'Romochka, Roman', 'Romualdo', 'Rómulo', 'Roque', 'Rosario', 'Rosendo',
    'Rosiyn', 'Rushe, Rousse, Rushkin, Rousskin, Rust, Rousset', 'Royce', 'Royden', 'Rubén', 'Rufino', 'Rufo', 'Ruggero',
    'Rule, Ruelle, Reule', 'Runihura', 'Ruperto', 'Russell, Roussel', 'Ruy', 'Saa', 'Sabacio', 'Sabelio',
    'Saber', 'Sabino', 'Sabola', 'Sacha, Sasha, Shura, Shurochka, Sanya, Shurik, Shashenka', 'Sacha', 'Sacripant', 'Sadiki', 'Sahúl',
    'Salih', 'Salim', 'Salomón', 'Salustio', 'Salvador', 'Salvatore, Salvatorio', 'Salviano', 'Salvino',
    'Salvo', 'Sami', 'Samir', 'Samuel', 'Sancho', 'Sansón', 'Santiago', 'Santino',
    'Santo', 'Santos', 'Sargent', 'Satordi', 'Saturnino', 'Saturno', 'Saúl', 'Saulo',
    'Saverio', 'Saville, auville', 'Scoville', 'Searlas, Searle, Searlus', 'Seb', 'Sebak', 'Sebastián', 'Sebastiano',
    'Sefonías', 'Sefu', 'Segismundo', 'Segundo', 'Sekani', 'Sempronio', 'Semyon', 'Senapus',
    'Senior, Seignour', 'Sennet, Senet', 'Senusnet', 'Sept', 'Septimio', 'Serafín', 'Serapis', 'Sergio',
    'Seriozha, Seriozhenka, Serge, Serguei', 'Serug', 'Servando', 'Set, Sutekh', 'Seth', 'Sethos', 'Severino', 'Severo',
    'Seymour', 'Shabaka', 'Shakir', 'Sharón', 'Sheba', 'Shelomó', 'Shem', 'Shimeón',
    'Shu', 'Sidney, Sydney', 'Sifiye', 'Sigfrido', 'Silvano', 'Silverio', 'Silvestre', 'Silvino',
    'Silvio', 'Simeón', 'Simón', 'Simplicio', 'Sinesio', 'Sinforiano', 'Sinforoso', 'Siro',
    'Sixto', 'Sneferu', 'Sobk', 'Sócrates', 'Sofanor', 'Sófocles', 'Solano', 'Somer',
    'Somerville, Sumarville', 'Soren, Sorel, Sorrell', 'Sotero', 'Stanislow,Slavik', 'Stefan, Stepka, Stephen', 'Stefano', 'Sudi', 'Sumner',
    'Tabare', 'Tabaré', 'Tabari', 'Taciano', 'Tacio', 'Tácito', 'Tadeo', 'Talbot',
    'Talon', 'Tancredo', 'Tarik', 'Tarquino', 'Tarsicio', 'Tau', 'Tearlach', 'Tehuti',
    'Telémaco', 'Telford, Telfer, Tallefer, Telfor, Telfour', 'Telmo', 'Termán', 'Teo', 'Teobaldo', 'Teodorico', 'Teodoro',
    'Teodosio', 'Teófilo', 'Teraj', 'Teremun', 'Terencio', 'Thabit', 'Thiery, Thibaud, Tibault', 'Thoth, Astennu',
    'Thutmose', 'Tiberio', 'Tiburcio', 'Ticiano', 'Timoteo', 'Tirso', 'Tito', 'Tobías',
    'Tolenka, — Tolya', 'Tosya, Tusya', 'Tomás', 'Tommaso', 'Tonatiúh', 'Tor', 'Torcuato', 'Toribio',
    'Toufic o Tufic', 'Toussaint', 'Traful', 'Tránsito', 'Travers, Travis', 'Trinidad', 'Tristán', 'Trofimoff',
    'Tubal', 'Troy, Troyes', 'Tsekani', 'Tulio', 'Tum', 'Tumaini', 'Tupac', 'Turner',
    'Tutankhamun', 'Typhon', 'Tyson, Tyeis', 'Ubaid', 'Ubaldo', 'Ufa', 'Ugo', 'Ulises',
    'Ulrico', 'Umi', 'Unika', 'Ur, Ur-atum', 'Urbano', 'Uri', 'Uriá', 'Uriel',
    'Urso', 'Usi', 'Uthman', 'Uzi', 'Uzaiel', 'Vachel', 'Vaden', 'Vail, Vayle',
    'Valarico', 'Valdemar o Waldemar', 'Valdo', 'Valentín', 'Valentino, Valer', 'Valentino', 'Valeriano', 'Valerik, Valerii',
    'Valerio', 'Valfredo', 'Valiant', 'Vallis, Vallois', 'Vanechka, Vanyusha', 'Varden, Vardan, Vardon, Verddun', 'Vassily,Vassi, Vasya, Vas, Vasili', 'Venancio',
    'Venceslao o Wenceslao', 'Ventura', 'Verney, Vernay', 'Vernon', 'Verril, Verel, Verrall, Verrel, Veryl', 'Vespasiano', 'Vicente', 'Vick, Vic, Vice',
    'Víctor', 'Victoriano', 'Victorino', 'Victorio', 'Vidal', 'Vincenzio, Vittorio, Vito', 'Virgilio', 'Vital',
    'Vitenka', 'Vito', 'Vladimir', 'Vladimiro', 'Viadislav, Vladik, Vyacheslav', 'Vladmir, Vladmiri', 'Vladsislas', 'Volodya, Vladik, Vladya',
    'Wadih', 'Wafic', 'Walberto', 'Waldo', 'Walter', 'Wamukota', 'Warrane', 'Werner',
    'Wilfredo', 'William', 'Wilson', 'Wyatt, Wiatt', 'Xarles', 'xavier', 'Xochtil', 'Yael',
    'Yafeu', 'Yago', 'Yahya', 'Yakov', 'Yaremka, Yerik', 'Yasha', 'Yermolay', 'Yuri, Yurii, Yurik, Yura, Yurochka',
    'Yamil', 'Yazid', 'Yihad', 'Younes o Yunes', 'Yves', 'Yvon, Yvet', 'Zabulón', 'Zacarías',
    'Zadoc', 'Zah', 'Zahur', 'Zaid, Ziyad', 'Zaqueo', 'Zdenek', 'Zebadiá', 'Zebulún',
    'Zedequías', 'Zenón', 'Zerbino', 'Zhenechka, Zhenya', 'Zhorah, Zorya', 'Ziven, Zivon', 'Zimri', 'Zoel',
    'Zoilo', 'Zuberi', 'Nombres Femeninos', 'Abbi o Abby', 'Abdulía', 'Abelarda', 'Aberfa', 'Abertha',
    'Abi', 'Abiah', 'Abidán', 'Abigail', 'Abigaíl', 'Abir', 'Abril', 'Ada',
    'Adabella', 'Adain, Adenydd', 'Adalcira', 'Adalgisa', 'Adalia', 'Adalina', 'Adaluz', 'Adara',
    'Adaya', 'Adda', 'Addfwyn', 'Addiena, Addien', 'Adelaida', 'Adelfa', 'Adelgunda', 'Adelina',
    'Adelinda', 'Adelma', 'Adelmira', 'Adelvina', 'Adena', 'Adilia', 'Adna', 'Adolfa',
    'Adoniá', 'Adoración', 'Adria o Adriana', 'Adriana', 'Adyna', 'Aelwyd', 'Afra', 'Afreda',
    'Alfre', 'Alfy', 'Allfryda', 'Elfrieda', 'Ellírieda', 'Fredi', 'Africa', 'Afrodita',
    'Afton', 'Agafía', 'Agapita', 'Agar', 'Agata', 'Ageda', 'Aglae', 'Aglaia',
    'Agnes', 'Agnessa', 'Agnus', 'Agostina', 'Agripina', 'Agueda', 'Agustina', 'Aída',
    'Aida', 'Aidee / Aide / Haide / Haidee', 'Aidée Variante gráfica de Haydée', 'Ailen / Aylen / Aillén', 'Ailín / Aylin', 'AAime', 'Aimee', 'Ainara',
    'Aisha', 'Aixa', 'Akilina', 'Aquilina', 'Aladina', 'Alana', 'Alba', 'Albana',
    'Alberta', 'Albertina', 'Albina', 'Alcira', 'Alda', 'Aldana', 'Alegra', 'Alegría',
    'Aleja', 'Alejandra', 'Alejandrina', 'Aleksandra', 'Aleth', 'Alexandra', 'Alexia', 'Alfa',
    'alfilda', 'Alfonsina', 'Alfreda', 'Alicia', 'Aleida', 'Alina', 'Alisa', 'Allisah',
    'Alla, Allochka', 'Alma', 'Almira', 'Almudena', 'Alodía', 'Alonsa', 'Altagracia', 'Altair',
    'Altamira', 'Altea', 'Alva', 'Alvina', 'Ama', 'Amada', 'Amadea', 'Amadis',
    'Amalia', 'Amaliji', 'Amalsinda', 'Amancay / Amancai', 'Amancia', 'Amanda', 'Amaniá', 'Amapola',
    'Amaranta', 'Amariá', 'Amarilis', 'Amarilla / Amaril', 'Amata', 'Amatista', 'Amaya', 'Amazona',
    'Ambar', 'Ambrosia', 'Amelia', 'América', 'Amina', 'Aminta', 'Amira', 'Amneris',
    'Amparo', 'Amser', 'Amunet', 'Ana / Anna', 'Ana', 'Anabel', 'Anabella', 'Anacaona',
    'Anacleta', 'Anahí', 'Anaís', 'Analía', 'Analiria', 'Anani', 'Anastasia, Stasya, Nastya', 'Anastasia',
    'Anat', 'Anatilde', 'Anatolia', 'Anayance', 'Andrea Femenino de Andrés', 'Andreína', 'Andrómaca', 'Andrónica',
    'Anelida', 'Anelina', 'Anelisa', 'Anémona', 'Anfitrita', 'Angela', 'Angeles', 'Angélica',
    'Angelina', 'Angharad, Anghard', 'Angustias', 'Aniceta', 'Anilda', 'Anippe', 'Anselma', 'Antea',
    'Antífona', 'Antígona', 'Antolina', 'Antonella', 'Antonia', 'Antonina', 'Anunciación', 'Anya, Anitchka, Anna, Anechka, Asenka',
    'Aparicia', 'Apia', 'Apolinaria', 'Apolonia', 'Apuleya', 'Ara', 'Arabela', 'Araceli',
    'Aracelis', 'Aragonta', 'Aránzazu', 'Arbogasta', 'Arcadía', 'Arcelia', 'Archibalda', 'Ardelia',
    'Argel', 'Argelia', 'Argenea', 'Argentina', 'Argimira', 'Arglwyddes', 'Argoel', 'Argraff',
    'Aria / Ariadna', 'Ariadna', 'Arial', 'Ariana, Arian', 'Ariana', 'Arianrhod', 'Ariela', 'Arietta, Ariette',
    'Arkadina', 'Arlais', 'Arlene', 'Armanda / Arminda', 'Armandina', 'Armes', 'Armida', 'Arnulfa',
    'Artaith', 'Artemia', 'Artemisa', 'Arthes', 'Arwydd', 'Asela', 'Asgre', 'Ashley, Aisley',
    'Asia', 'Aspasia', 'Astarte', 'Asteria', 'Astra', 'Astrid / Astryd', 'Asunción', 'Atala',
    'Atanasia', 'Atenea', 'Atgas', 'Atica', 'Atilia', 'Atocha', 'Auda', 'Audrey',
    'Augusta', 'Aura', 'Aúrea', 'Aurelia', 'Auristela', 'Aurora', 'Aurora Latín, Aurora', 'Auset',
    'Austria', 'Auxiliadora', 'Ava', 'Avdotya', 'Avelina', 'Avril, Avril, Averyl, Avry', 'Awel', 'Ayelén',
    'Azalea', 'Aita', 'Azucena', 'Baby', 'Bahiti', 'Balbina', 'Baldomera', 'Balduina',
    'Banon', 'Bárbara', 'bárbara', 'bartola', 'Basilia', 'Bastet', 'Batilde', 'Baudilia',
    'Beata', 'Beatriz', 'Begoña', 'begoña', 'Begonia', 'Belinda', 'Belisa', 'Belisaria',
    'Belkis', 'Bella', 'Benedicta', 'Benigna', 'Benilda', 'Benita', 'Benjamina', 'Bennu',
    'Berengaria', 'Berenice', 'Berila', 'Berna', 'Bernabela', 'Bernarda', 'Bernardita', 'Berta',
    'berta', 'Berth', 'Berthog', 'Bertilda', 'Bertolda', 'Betania', 'Betia', 'Betiana',
    'Betina', 'Betsabé', 'Betulia', 'Beula', 'Beverly, Beverley', 'Bianca', 'Bibiana', 'Bienvenida',
    'Birdie, Birdy', 'Blanca', 'Blandina', 'Blasina', 'Blenda', 'Blessing, Bletsung', 'Bliss, Bliths', 'Blodwen, Blodwyn',
    'Blossom, Blostm', 'Blythe, Blithe', 'Bohdana', 'Bolonia', 'Bona', 'Bonfilia', 'Bonifacia', 'Bonnie, Bonny, Bonie',
    'Braith', 'Braulia', 'Bregus', 'Brenda', 'Briallan', 'Brígida', 'Brillana', 'Bronwen, Branwen, Bron, Bronwyn, Brangwen, Brangwy, Branwenn',
    'Brooke', 'Bruna', 'Brunella / Brunela', 'Brunilda', 'Buddug', 'Cadena, Cadyna', 'Cadi, Catrin', 'Cadwyn',
    'Caethes', 'Cafell', 'Caliope', 'Camelia', 'Camila', 'Candela', 'Calistena', 'Calixta',
    'Calivina', 'Canciana', 'Candelaria', 'Cándida', 'Canela', 'Caridad', 'Carina', 'Carisa',
    'Carla', 'Carlota', 'Caniad', 'Canuta', 'Cara', 'Caralampia', 'Carmela', 'Carmen',
    'Carola', 'Carolina', 'Carmya, Carmina, Carmine, Carmita, Charmaine', 'Carol, Caroline, Carolyn, Carolina, Carrie', 'Carolina Forma diminutiva femenina de Carlos', 'Caron', 'Casandra', 'Casilda',
    'Casimira', 'Catalina', 'Cecilia', 'Ceferina', 'Celeste', 'Celia', 'Celina', 'Celmira / Zelmira',
    'Celsa', 'Centola', 'Cesare / Cesarina', 'Casiana', 'Cassandra', 'Casta', 'Castalia', 'Cath',
    'Cayetana', 'Cesilia', 'Celedonia', 'Celerina', 'Celiflora', 'Celmira', 'Cenobia', 'Ceri',
    'Ceridwen, Ceri', 'Cesárea', 'Charis', 'Charlotta', 'Charo', 'Chelsea', 'Chepa', 'Cherezada',
    'Chila', 'Chione', 'Cibeles', 'Cielo', 'Cintia o Cinthia', 'Cira /  Cirila', 'Circe', 'Cirinea /  Cirenia',
    'Clara', 'Clarabella', 'Claribel', 'Clarisa', 'Claudía', 'Claudina', 'Clea. Cleo', 'Clelia',
    'Clemencia', 'Clementina', 'Cintia', 'Cipriana', 'Cira', 'Ciríaca', 'Cirila', 'Citlalli',
    'Claresta', 'Claudia', 'Cleantha', 'Cleofe', 'Cleopatra', 'Clidía / Clide', 'Clío', 'Clodovea',
    'Cloe', 'Clorinda', 'Colomba', 'Concepción', 'Constanza', 'Consuelo', 'Cora', 'Cordelia',
    'Comelia', 'Corina', 'Crimilda', 'Crispina', 'Cristina', 'Custodía', 'Chiara', 'Cleta',
    'Cleva', 'Clímaca', 'Climena', 'Clío', 'Clitia', 'Clodomira', 'Cloe Del Griego hierba verde', 'Clotilde',
    'Cody, Codie, Codi', 'Cointa', 'Coleta', 'Colombia', 'Colombina', 'Concepcion', 'Concordía', 'Conrada',
    'Constantina', 'Coral', 'Cordelia, Creiddylad', 'Corisanda', 'Corliss', 'Cornelia', 'Coromoto', 'Corona',
    'Corsen', 'Covadonga', 'Cragen', 'Crescencia', 'Crimilda', 'Crisanta', 'Crisogona', 'Cristobalina',
    'Cucufata', 'Cunegunda', 'Custodía', 'Cwen', 'Cymreiges', 'Cyne, Cym, Cim', 'Cyneburhleah, Cynburleigh, Cymberly, Cimberleigh', 'Dafne',
    'Daila', 'Daira', 'Dalia', 'Dalila', 'Dalma', 'Dalmacia', 'Damaris', 'Dana',
    'Dánae', 'Daniela', 'Danila', 'Dara', 'Daría', 'Débora / Déborah / Debra', 'Deidamia', 'Delfina',
    'Delia', 'Delicia', 'Demetria', 'Deonilde', 'Desdémona', 'Desideria', 'Desirée', 'Díana',
    'Dina', 'Dinora o Dinorah', 'Dionisia', 'Dolores', 'Dominga', 'Domínica', 'Dominique', 'Domitila',
    'Donina', 'Donosa', 'Dora / Dorina)', 'Doris', 'Dorotea', 'Dulce', 'Dulcinea', 'Daisy',
    'Dale, Dayle, Dael', 'Dalmara', 'Damiana', 'Damira', 'Darlene', 'Daryl', 'Dasha', 'Débora',
    'Decia', 'Dee, Du, Dierdre, Delia', 'Deifilia', 'Delmira Aféresis de Edelmira', 'Deodata', 'Deogracias', 'Dera', 'Derwen',
    'Devora', 'Deyanira Griego', 'Deyanira', 'Díamantina', 'Díanora', 'Dicra', 'Difyr', 'Digna',
    'Dilys, Dylis, Dyllis, Dil, Dill, Dilly', 'Dimitra', 'Dinorah', 'Dione', 'Dionisa', 'Dirce', 'Diva', 'Dolly',
    'Dominika', 'Dona', 'Donata', 'Drysi', 'Dulía', 'Dunyasha', 'Duscha', 'Eadda, Ede, Eda, Eda',
    'Eadwine, Edwina, Edina', 'Earlene, Erleen', 'Eartha, Ertha', 'Earwine, Earwyn, Enwina, Enwyna', 'Easter, Eastre', 'Ebe o Hebe', 'Eda o Edda', 'Edelia /  Edilma /  Edilia',
    'Edelmira / Edelira / Edelma / Delma', 'Edén', 'Edgarda', 'Edilia', 'Edit o Edith', 'Edita', 'Edna', 'Eber',
    'Ebrill', 'Echidna', 'Eda', 'Edelburga', 'Edelmira', 'Edesia', 'Edilberta', 'Edith',
    'Edith, Edyth, Eadgyth', 'Edlyn, Eathelin, Eathelyn, Edlin, Edlen', 'Edmonda, Eadmund, Edmunda, Edmanda, Eduarda', 'Edmunda', 'Eduarda', 'Edurne', 'Eduviges', 'Egda',
    'Egeria', 'Egidía', 'Egle', 'Ela', 'Eladía', 'Elba', 'Elcira', 'Elda o Helda',
    'Electra', 'Elena / Elina / Helena', 'Eleodora', 'Eleonora / Eleonor / Leonor / Nélida / Nelly / Nora', 'Ella / Eliana / Eliane / Helia', 'Elida', 'Elina', 'Edrea, Earric, Edra',
    'Eduvigis', 'Edvina', 'Efa', 'Eferhild, Eferhilda', 'Efige', 'Egberta, Egbertina, Egbertine, Egbertyne', 'Eglantina', 'Eheubryd',
    'Eira', 'Ekaterina', 'Elberta, Elberte, Elbertina, Elbertine, Elbertyna', 'Elda', 'Elen', 'Elena', 'Eleonora', 'Elethea, Elthia, Elethia',
    'Eleusipa', 'Eleuteria', 'Elfega', 'Elfida', 'Elfreda', 'Elfrida, Elfreda, Elfrieda, Elva, Elvie', 'Elga', 'Eliana',
    'Eligia', 'Elinda', 'Elisa', 'Eliodora', 'Elisabeth', 'Elisea', 'Elisheba', 'Elisabet',
    'Ella, Elle', 'Ella', 'Ellylw', 'Elma', 'Elmira, Elmyra', 'Elmira', 'Elodía', 'Eloísa',
    'Elpidía', 'Elsa', 'Elvia / Helvia', 'Elvina', 'Elvira', 'Elvisa', 'Ema / Emelina / Emelinda / Emma / Emna', 'Emerenciana',
    'Emerita', 'Emilia', 'Emiliana', 'Emperatriz', 'Encarnación', 'Engracia', 'Enriqueta o Enrica', 'Erica o Erika',
    'Erlinda', 'Ermelinda', 'Emnesta / Emestina', 'Escolástica', 'Esmerada / Esmeralda', 'Esperanza', 'Estefanía / Stefanía / Stephanie', 'Estela',
    'Estelinda', 'Estero Esther', 'Esterina', 'Estrella', 'Etel o Ethel', 'Eloína', 'Elsa Variante germánica de Elisa', 'Elva',
    'Elvena', 'Elvia', 'Emelia', 'Emelina', 'Emérita', 'Emeteria', 'Emilia Véase Emilio', 'Emilse',
    'Emira', 'Emma', 'Ena', 'Enedina', 'Eneida', 'Eneuawg', 'Enid', 'Enit, Enid',
    'Enrhydreg', 'Enriqueta', 'Epifania', 'Erda', 'Erdudvyl', 'Eréndira', 'Eres', 'Erica',
    'Ermengarda', 'Erna, Earna', 'Erna', 'Ernestina', 'Ernestine, Enerstyne, Enerstina, Earnestyna', 'Erosina', 'Erwina, Erwyna, Earwyna, Aerwyna', 'Eshe',
    'Esmeralda', 'Estefanía', 'Ester, Eszter, Esther, Estrela', 'Estervina', 'Esyllt', 'Etaina', 'Etel, Etilka, Ethel', 'Etelburga',
    'Etelinda', 'Etelvina', 'Eudosia / Eudoxia / Eufemia', 'Eufrasia', 'Eugenia', 'Eulalia / Olaya', 'Eulogia', 'Eunice',
    'Eurídice', 'Eusebia', 'Eva', 'Evangelina', 'Evelia', 'Evelina', 'Evelyn', 'Eteria',
    'Euda', 'Eudocia', 'Eufemia', 'Eufonia', 'Eufrosina', 'Eulalia', 'Eumelia', 'Euporia',
    'Eurnei', 'Eurolwyn', 'Eustaquia', 'Eustasia', 'Eutalia', 'Euterpe', 'Eutimia', 'Eutiquia',
    'Eutropia', 'Evarista', 'Exgenia', 'Evodía', 'Exaltación', 'Expedita', 'Expósita', 'Eysik',
    'Fabia', 'Fabiana', 'Fabiola Latín, Fabiola, diminutivo femenino de Fabio', 'Fabiola', 'Fabricia', 'Facunda', 'Faith, Faithe, Fayth', 'Fanny',
    'Faría', 'Farida', 'Fátima', 'Fausta', 'Fayre', 'Fe', 'fe', 'Febe',
    'Febronia', 'Federica', 'Fedora', 'Fedra', 'Felabeorht, Filberta, Felberta', 'Felicia', 'Felicidad', 'Felicitas',
    'Felipa', 'Felisa', 'Femi', 'Feodora', 'Fermina', 'Fern', 'Fernanda', 'Ffanci',
    'Fíraid', 'Fidela', 'Fidelia', 'Fidencia', 'Fifí', 'Filadelfia', 'Filandra', 'Filemona',
    'Filiberta', 'Filis', 'Filomela', 'Filomena', 'Filotea', 'Fina', 'Fiona', 'Fiorella',
    'Flaminia', 'Flavia', 'Flérida', 'Fleta, Flyta', 'Flor', 'Flora', 'Fiore, Fiorello', 'Florencia',
    'Floriana', 'Florinda', 'Fonda', 'Fortuna', 'Fortunata', 'Franca', 'Francisca', 'Freda',
    'Fredegunda', 'Fredesvinda', 'Freya', 'Frida', 'Friné', 'Froilana', 'Fructuosa', 'Fukayna',
    'Fulgencia', 'Fulvia', 'Fusca', 'Gabina', 'Gabriela', 'Gala', 'Galatea', 'Galenka, Galine, Galya',
    'Galia', 'Galina', 'Garan', 'Gardenia', 'Gasparina', 'Gaudencia', 'Gay, Gay]e, Gail, Gale', 'Gea',
    'Gelasia', 'Gema', 'Geminiana', 'Generosa', 'Genoveva', 'Genoveva es pues una variante de Ginebra', 'Georgia', 'Georgina',
    'Geraldina', 'Geraldine', 'Geranio', 'Gerarda', 'Gerásima', 'Gerda', 'Germana', 'Gertrudis',
    'Gervasia', 'Getulia', 'Giannina', 'Gijs', 'Gilberta', 'Gilda', 'Gina', 'Ginebra',
    'Gines', 'Gioconda', 'Giovanna', 'Grisela (Gisel / español por traducción del francés Giselle', 'Gisela', 'Giselle', 'Glad, Gleda', 'Gladis',
    'Gladys, Gladys, Gleda, Glad, Gladdie, Gladdy', 'Gladys', 'Glan', 'Glenda', 'Glenda, glyn, Glenn, Glen', 'Glenys, Glen', 'Gliceria', 'Gloria',
    'Gloriana, Glorianna, Gloriane', 'Glyn Gales', 'Glynis, Glynnis, Glyn', 'Godiva, Godgifu', 'Godofreda', 'Goewin', 'Goleuddydd', 'Gorasgwrn',
    'Gorawen', 'Gorgonia', 'Gracia', 'Gracia, Grace, Gracie', 'Graciana', 'Graciela', 'Gracilia', 'Gregoria',
    'Gregorina', 'Greta', 'Gretel', 'Grimalda', 'Grisel', 'Griselda', 'Guadalupe', 'Gualberta',
    'Gualteria', 'Gúdula', 'Guendolen', 'Guida', 'Guillermina', 'Guiomar', 'Gumersinda', 'Gunda',
    'Gundelinda', 'Gundenia', 'Gustava', 'Gwaeddan', 'Gwanwyn', 'Gwen', 'Gwenabwy', 'Gwendolen',
    'Gwendolina', 'Gwener', 'Gwenledyr', 'Gwenn alarch', 'Gytha, Githa', 'Habibah', 'Hada', 'Haidée',
    'Halima', 'Hannah', 'Haquikah', 'Hasina', 'Hathor, Hathor-sakmet', 'Hatshepsut', 'Hayde o Haydée', 'Hayley',
    'Hazel', 'Heallfith', 'Hebe', 'Heda', 'Hedda', 'Heidi', 'Helah', 'Helena',
    'Helenka', 'Helga', 'Heli', 'Helia', 'Heliana', 'Heliodora', 'Heloísa', 'Helvecia',
    'Helvia', 'Heraclia', 'Herculana', 'Heriberta', 'Hermelinda', 'Hermenegilda', 'Hermilda', 'Herminda',
    'Herminia', 'Hermione', 'Hersilia', 'Herta', 'Hertha', 'Herundina', 'Higinia', 'Hilaria',
    'Hilda', 'Hilda o llda', 'Hildebranda', 'Hildegarda', 'Hildegunda', 'Hilmer', 'Hlynn', 'Holly, Holea, Halig',
    'Homera', 'Honey, Hunig, Honbria, Honbrie', 'Honorata', 'Honoria', 'Honorina', 'Hope', 'Horacia', 'Hortensia',
    'Hrothbeorhta, Hrothberta, Hrothnerta, Hrothbertina', 'Humbelina', 'lafa', 'lanina', 'lara', 'Iciar o Izar', 'Ida', 'Idalia',
    'Idalina', 'Idara', 'Idelia', 'ledidá', 'Ife', 'Ifigenia', 'Ignacia', 'llde, Idla',
    'lldefonsa', 'lIdegunda', 'Ileana', 'lleana', 'lia', 'llona', 'Ilse', 'Iluminada',
    'Imelda', 'Indalecia', 'Indeg', 'Indíana', 'Inés', 'Inga', 'Ingrid', 'Inmaculada',
    'Inocencia', 'lola', 'lona', 'Iracema', 'Iraida', 'Irena, rina', 'Irene', 'Irenea',
    'Iriel', 'Irina', 'Iris', 'Irsa', 'Irma', 'Irupé', 'Irvette, Ivetta', 'Isabel',
    'Isadora', 'Isaura', 'Isberga', 'Iselda', 'Isidora', 'Isis', 'Ismelda', 'Ismenia',
    'Isolda', 'Isolde, Isolda', 'Isolina', 'Itala', 'Itatay', 'Itatí', 'Ivana o Ivanna', 'Ivana, Ivane',
    'Iverna', 'Ivón', 'Ivonne', 'Ivy, Ivey, fig', 'Jacarandá', 'Jacinta', 'Jacoba', 'Jocelyn',
    'Jacobina', 'Jacqueline', 'Jael', 'Jala', 'Jamila o Yamila', 'Jamila', 'Javiera', 'Jazmín',
    'Jeanette', 'Jeannette', 'Jeftzibá', 'Jelena', 'Jenara', 'Jendayi', 'Jénifer', 'Jennifer',
    'Jenny', 'Jerónima', 'Jésica o Jéssica', 'Jessica', 'Jesusa', 'Jezabel', 'Jimena', 'Joana o Johana',
    'Joaquina', 'Joba', 'Jocelín o Jocelyn', 'Jocelyn, Joscelyne, Josceline, Jocelyne', 'Jordana', 'Jorgelina', 'Josefa', 'Josephine',
    'Josefina', 'Jovita', 'Juana', 'Jucunda', 'Judit', 'Judith', 'Julia', 'Juliana',
    'Julieta', 'Juno', 'Justa', 'Justina', 'justa', 'Juvencia', 'Juventa', 'Kakra',
    'Kaled', 'Kamilah', 'Kanika', 'Karen', 'Karin', 'Karina', 'Karla', 'Katherina',
    'Katia', 'Katy', 'Keila', 'Keket', 'Kelemon', 'Kelly', 'Keren', 'Kerry',
    'Keyla', 'Kieve', 'Kigva', 'Kimberly, Kim, Kimbra', 'Kimbrough, Kimbro', 'Kira, Kirochka', 'Kisa', 'Kiska, katya, katarina, katyenka, katyuska, katherina',
    'Kissa', 'Ksana, Ksanochka', 'Laica', 'Laila', 'Lais', 'Lakmé', 'Landelina', 'Landrada',
    'Laodamia', 'Laodicea', 'Lara', 'Lara, Larisa, Larissa, Lanassa', 'Larisa', 'Lark, Larke', 'Lassie, Lasse, Llass', 'Laudelina',
    'Laura', 'Laureana', 'Lavinia', 'Layla', 'Lea', 'Leandra', 'Leda', 'Leigh, Ley, Lee, Lea, Leah, Leia',
    'Leiela', 'Leila', 'Lena', 'Lenusya', 'Leocadía', 'Leocricia', 'Leoma', 'Leonarda',
    'Leoncia', 'Leonela', 'Leonilda', 'Leonor', 'Leopolda', 'Leopoldina', 'Lesbia', 'Leticia',
    'Levina, Levene, levyna', 'Lía', 'Llana', 'Libera', 'Liberata', 'Libertad', 'Liberty', 'Libia',
    'Libitina', 'Libna', 'Liboria', 'Licia', 'Lida', 'Lidía', 'Lidía o Lydía', 'Lidija, Lidía, idiya, Llidochka, Lida',
    'Ligia', 'Lila', 'Lili', 'Lilia', 'Lilián', 'Liliana', 'Lilit', 'Lilybet',
    'Lina', 'Linda', 'Lindsay, Llindsey', 'Liria', 'Lis', 'Lisa', 'Lisandra', 'Lissa, Lyssa',
    'Lita', 'Livia', 'Liza', 'Lisabet', 'Lodema, Lodima, Lodyma', 'Loida', 'Lola', 'Lona, Lloni',
    'Loreley', 'Lorena', 'Lorenza', 'Loreta', 'Loreto', 'Lotus', 'Lourdes', 'Love, Lov',
    'Lowri', 'Lubiana', 'Lubmilla', 'Lucelía', 'Lucero', 'Lucía', 'Lucía Femenino de Lucio', 'Luciana',
    'Lucila', 'Lucina', 'Lucrecia', 'Lucy', 'Ludmila', 'Ludovica', 'Luisaa', 'Luisina',
    'Luna', 'Lupe', 'Lutgarda', 'Luz', 'Luzmelia', 'Lynn, Lyn, Lin, Linne', 'Lynn', 'Lyubov',
    'Lyudmila, lyuba, Iyubochka, luda, ludmila', 'Maat', 'Mabel', 'Mabli', 'Macarena', 'Macaria', 'Maclovia', 'Macra',
    'Mafalda', 'Magalí', 'Magdalena', 'Magna', 'Magnolia', 'Maia', 'Maida', 'Mair',
    'Maira', 'Maitane, Maite, Maitena', 'Maite', 'Maitena', 'Malají', 'Malena', 'Mali', 'Malisa',
    'Malú', 'Malvina', 'Mamerta', 'Mandisa', 'Manila', 'Manón', 'Manuela', 'Mara',
    'Marcela', 'Marcelina', 'Marcia', 'Margarete, Margosha', 'Margarita', 'Marged, Margred, Mererid, Meghan', 'María', 'Marián',
    'Mariana', 'Marianela', 'Mariángeles', 'Marianne, Marianna', 'Maribel', 'Maricel', 'Maricruz', 'Mariel',
    'Mariela', 'Marilín', 'Marilina', 'Marilú', 'Marina', 'Marine', 'Marinochka, Marina', 'Marión',
    'Marisa', 'Marisabel', 'Marisol', 'Marlene', 'Marquisela', 'Marta o Martha', 'Martina', 'Maruja',
    'Masha', 'Masika', 'Massiel', 'Matahari', 'Matea', 'Matilde', 'Maura', 'Maximiliana',
    'Méáximina', 'Maya', 'Medea', 'Mei', 'Melania', 'Melanie o Melany', 'Melba', 'Melchora',
    'Melicia', 'Melibea', 'Melinda', 'Melisa', 'Melitona', 'Melusina', 'Mercedes', 'Mercia',
    'Mercy', 'Meredith, Maredud, Meredydd', 'Merry', 'Mertice, Maertisa, Mertysa, Mertise', 'Mesi', 'Meskhenet', 'Messalina', 'Metodía',
    'Mía', 'Micaela', 'Michelle', 'Micol', 'Mika', 'Milena', 'Milagros', 'Milburga',
    'Milca', 'Mildreda', 'Minerva', 'Mirabel', 'Miranda', 'Mireya', 'Miriam o Myriam', 'Mirla',
    'Mirna o Myrna', 'Mirna', 'Mirta o Mirtha', 'Mirta', 'Mitra', 'Modesta', 'Modien', 'Moira',
    'Mona', 'Mónica', 'Monifa', 'Monserrat', 'Moraima', 'Morela', 'Morgan, Morgana, Morgant', 'Morgana',
    'Moria', 'Morvuddt', 'Mukamutara', 'Mukantagara', 'Munira', 'Muriel', 'Mut', 'Myfanawy',
    'Nabirye', 'Nadezhda', 'Nadyenka', 'Nadía', 'Nadina', 'Nacemah', 'Nahama', 'Nahir',
    'Naír', 'Naná', 'Nancy', 'Nantilde', 'Naomi', 'Narcisa', 'Natacha o Natasha', 'Natalí o Nataly',
    'Natalia', 'Natalya', 'Nesha, Nessa, Nesya', 'Nikolaevna, Nika', 'Nathifa', 'Natividad', 'Naunet', 'Náyade',
    'Nayla', 'Nazarena', 'Nazaret', 'Nazaria', 'Nebt-het, Nephthys', 'Neda', 'Nefertari', 'Nefertiti',
    'Nélida', 'Nellwyn, Nelwin, Nelwina, Nelwyna', 'Nelly', 'Nemesia', 'Nerea', 'Nereida', 'Narina', 'Net, Neith',
    'Neued', 'Nicanora', 'Nicasia', 'Nicolasa', 'Nicole', 'Nidía', 'Nidía o Nydía', 'Nieves',
    'Nikita, Nakita', 'Nilda', 'Nile', 'Nimia', 'Nina', 'Ninfa', 'Ninochka, Nina', 'Ninoska',
    'Niobe', 'Noelia', 'Nominanda', 'Nona', 'Nora', 'Nora Abreviación de Eleonora', 'Norka', 'Norma',
    'Nubia', 'Numeria', 'Nuria', 'Nuru', 'Nusa', 'Obdulia', 'Octavia', 'Odila',
    'Oda. diminutivo', 'Ofelia', 'Oksanochka, Oksana', 'Olegaria', 'Olga', 'Olga, Olya, Olenka, Olechka', 'Olimpia', 'Olinda',
    'Oliveria', 'Olivia', 'Olwen, Olwyn, Olwina, Olwyna', 'Omaira', 'Ondina', 'Onésima', 'Onfalia', 'Oralia',
    'Orelia', 'Orfelina', 'Orfilia', 'Oria', 'Oriana', 'Orlenda', 'Ornella', 'Orquídea',
    'Otilde', 'Otilia', 'Ovidía', 'Paciana', 'Paciencia', 'Pacomia', 'Palaciada', 'Palixena',
    'Palma', 'Palmira', 'Paloma', 'Pamela', 'Pancracia', 'Pandora', 'Pánfila', 'Paola',
    'Parasha, Parashie, Pasha', 'Parmenia', 'Partenia', 'Pascua', 'Pascuala', 'Pastora', 'Patricia', 'Paula',
    'Paulina. diminutivo', 'Paulina', 'Pauline, Paulina', 'Paz', 'Peace, Pax', 'Pelagia', 'Penarddun', 'Penélope',
    'Perfecta', 'Perla', 'Perpetua', 'Pérsida', 'Petra', 'Petrona', 'Philberta', 'Pía',
    'Piedad Advocación de la Virgen María', 'piedad', 'Pilar', 'Pimpinela', 'Piuquén', 'Placencia', 'Plácida', 'Polibia',
    'Policarpa', 'Polidora', 'Polixena', 'Pompeya', 'Pompilia', 'Ponciana', 'Popea', 'Poppy',
    'Porcia', 'Porfiria', 'Práxedes', 'Preciosa', 'Presentación', 'Primavera', 'Primitiva', 'Prisca',
    'Priscila', 'Procopia', 'Prócula', 'Proserpina', 'Próspera', 'Providencia', 'Prudencia', 'Pulqueria',
    'Pura', 'Purificación', 'Queena, Queenie', 'Querida', 'Querina', 'Quintilia', 'Quionia', 'Quirina',
    'Quiteria', 'Radegunda', 'Rafaela', 'Rahil', 'Raimunda', 'Raingarda', 'Raisa', 'Rajel',
    'Ramona', 'Ranevskaya, Ranya', 'Raquel', 'Raquildis', 'Rathtyen', 'Ratrudis', 'Rayén', 'Rebeca',
    'Refugio', 'Regina', 'Reina', 'Relinda', 'RemeDios', 'Remigia', 'Renata', 'Renée',
    'Restituta', 'Rhan', 'Rhawn', 'Rhedyn', 'Rhiain', 'Rhiannon', 'Rhianwen, Rhianwyn', 'Rhonwen',
    'Rhosyn', 'Ricarda', 'Rigoberta', 'Rillette, Rilletta', 'Rina', 'Rita', 'Roberta', 'Robustiana',
    'Rocío', 'Rodía', 'Rodriga', 'Rogaciana', 'Rogelia', 'Romana', 'Romilda', 'Romina',
    'Romualda', 'Roquelia', 'Rosa', 'Rosalinda', 'Rosalba', 'Rosalía Del Latín rosa', 'Rosalía', 'Rosamunda',
    'Rosana', 'Rosaura', 'Roselia', 'Rosenda', 'Rosicler', 'Rosilda', 'Rosina', 'Rosmira',
    'Roswinda', 'Rotrauda', 'Roxana', 'Rubí', 'Rubina', 'Rudi', 'Rufina', 'Ruperta',
    'Rut o Ruth', 'Rutilda', 'Rutilia', 'Sabina', 'Sabrina', 'Sacha, Sasha, Sashenka', 'Sacramento', 'Saeth',
    'Saffir', 'Safira', 'Safo', 'Sagrario', 'Salaberga', 'Salomé', 'Salustiana', 'Salvadora',
    'Samanta o Samantha', 'Sandra Abreviación de Alejandra', 'Sandra', 'Santa', 'Sara', 'Sarff', 'Saturnina', 'Scarlett, Scarlet',
    'Sebastiana', 'Secundina', 'Séfora', 'Segismunda', 'Selene', 'Selena', 'Selma', 'Selva',
    'Semíramis', 'Serafina', 'Serafine', 'Serapia', 'Seren', 'Serena', 'Servanda', 'Severina',
    'Sharon', 'Sheila', 'Shelley, Scelfleah', 'Sherry, Sherri, Shirley', 'Sian, sioned', 'Sibila', 'Sigfrida', 'Siglinda',
    'Sigrid', 'Silvana', 'Silvia', 'Silvina', 'Simona', 'Simplicia', 'Sinclética', 'Sinforosa',
    'Sinovia, Sinya', 'Sintiques', 'Sira', 'Sixta', 'Socorro', 'Sofía', 'Sofiya', 'Sofronia',
    'Sol', 'Solana', 'Solange', 'Soledad', 'Sonia, Sonya, Sonja, Sonechka', 'Sonia', 'Soraya', 'Sotera',
    'Starr, Starla, Star', 'Stella Maris', 'Stephania', 'Stockard, Stockhart, Stockhard, Stokkard', 'Sulamita', 'Suleika', 'Sulpicia', 'Summer, Suma',
    'Sunny', 'Susana', 'Susana Hebreo, Shushannah', 'Svetlana, Sveta', 'Tabita', 'Taciana', 'Tácita', 'Tadea',
    'Tais', 'Talaith', 'Talar', 'Talia', 'Talía', 'Talitha', 'Tally', 'Tamara',
    'Tamary', 'Tangwen', 'Tania', 'Tanya', 'Tarian', 'Tarren', 'Tarsicia', 'Tarsilia',
    'Tasya', 'Tatiana', 'Tea', 'Tecla', 'Teleri', 'Telesfora', 'Telma o Thelma', 'Telma',
    'Telyn', 'Temis', 'Teodequilda', 'Teodolinda', 'Teodomira', 'Teodora', 'Teodosia', 'Teódula',
    'Teófil', 'Teolinda', 'Teotista', 'Teresa', 'Teresita', 'Terpsicore', 'Terrwyn', 'Tesira',
    'Tetis', 'Thaís', 'Theodosía, Theda, Thedya', 'Tiberia', 'Tiburcia', 'Ticiana', 'Timotea', 'Tíndara',
    'Tirsa', 'Tita', 'Tomasa', 'Torcuata', 'Toreth', 'Toribia', 'Torlan', 'Torri',
    'Toscana', 'Tranquilina', 'Trifena', 'Trifonia', 'trinidad', 'Tristana', 'Troya', 'Tuesday, Tiwesdaeg',
    'Tula', 'Tulia', 'Tusnelda', 'Tyne, Tyna, Tina', 'Ulrica', 'Umbelina', 'Una', 'Urania',
    'Urbana', 'Urola, Ursula', 'Ursula', 'Ursulina', 'Vala', 'Valburga', 'Valdrada', 'Valentina',
    'Valeria', 'Valeska', 'Valkiria', 'Vanda', 'Vanessa', 'Vania, Vanya', 'Vanina', 'Vanora',
    'Varvara, Varya, Varinka, Varushka', 'Vassillissa, Vasilissa, Vasya', 'Velika', 'Velvet, Velouette', 'Venancia', 'Venus', 'Venustiana', 'Vera',
    'Verochka, Viveka', 'Verbena', 'Veredigna', 'Verna', 'Verónica', 'vespasiana', 'Vesta', 'Vicenta',
    'Victoria', 'Vidalina', 'Vigilia', 'Vilma', 'Violeta', 'Virgilia', 'Virginia', 'Virtudes',
    'Visitación', 'Vita', 'Viviana', 'Volupia', 'Walkária o Walkyria', 'Walls, Wales', 'Wanda', 'Wanetta, Wann',
    'Welcome', 'Welsa, Welsie', 'Wendy', 'Wereburga', 'Wílfrida', 'Wílla', 'Wilma', 'Winefrida',
    'Winnifred, Wynnifred', 'Wulflde', 'Wynne, wyn', 'Xenia', 'Xenobia', 'Ximena', 'Xiomara', 'Xóchitl',
    'Yajaira', 'Yalena, Yalenchka', 'Yamilet', 'Yanet', 'Yanina', 'Yanira', 'Yara', 'Yedda',
    'Yelizaveta', 'Yetta', 'Yocasta', 'Yolanda', 'Yoli', 'Yone', 'Ysbail', 'Yuliya, Yulenka',
    'Yuraima', 'Yvette', 'Yvonne', 'Zahira', 'Zahra', 'Zaida', 'Zaira', 'Zaneta',
    'Zarina', 'Zavrina, Zabrina', 'Zelma', 'Zelmira', 'Zenaida', 'Zenevieva', 'Zenobia', 'Zenya, Zenechka',
    'Zeonchka, zena', 'Zila', 'Zilla', 'Zinerva', 'Zita', 'Zoé', 'Zoila', 'Zoraida',
    'Zoyechka, Zoyenka, Zoya', 'Zulecia', 'Zuleica', 'Zulema', 'Zulima', 'Zulma',
    # Sistema
    'os', 'sys', 'shutil', 'pathlib', 'glob', 'fnmatch', 'stat', 'filecmp', 'tempfile',
    # Procesos
    'subprocess', 'multiprocessing', 'threading', 'queue', 'asyncio', 'concurrent',
    # Fechas
    'datetime', 'calendar', 'time',
    # Datos
    'json', 'csv', 'sqlite3', 'pickle', 'shelve', 'dbm',
    # Texto
    'string', 're', 'textwrap', 'difflib', 'unicodedata',
    # Matemáticas
    'math', 'cmath', 'decimal', 'fractions', 'random', 'statistics',
    # Funcional
    'functools', 'itertools', 'operator',
    # Colecciones
    'collections', 'heapq', 'bisect', 'array',
    # Compresión
    'zipfile', 'tarfile', 'gzip', 'bz2', 'lzma', 'zlib',
    # Internet / red
    'urllib', 'http', 'socket', 'email', 'ftplib', 'smtplib', 'imaplib', 'poplib',
    # HTML / XML
    'html', 'xml', 'html.parser',
    # Seguridad / hashes
    'hashlib', 'hmac', 'secrets', 'ssl',
    # Sistema / hardware
    'platform', 'ctypes', 'errno', 'signal', 'resource',
    # Depuración
    'logging', 'traceback', 'warnings', 'pdb', 'profile', 'timeit',
    # Programación
    'abc', 'dataclasses', 'enum', 'typing', 'types', 'inspect', 'importlib', 'ast', 'dis', 'keyword', 'builtins',
    # Consola
    'argparse', 'cmd', 'getopt', 'readline',
    # Utilidades
    'copy', 'pprint', 'contextlib', 'io', 'weakref', 'gc', 'sysconfig', 'configparser', 'gettext',
    ## Módulos estándar de Python para terceros
    'PyQt5', 'customtkinter', 'PIL', 'cv2', 'numpy', 'pandas', 'matplotlib', 'requests', 'flask',
    'django', 'bs4', 'selenium', 'playwright', 'cryptography', 'paramiko', 'openpyxl', 'PyPDF2',
    'pymediainfo', 'psutil',
    # Resaltador de sintaxis básico para el help de Python
    "class", "def", "import", "from", "return", "if", "else", "elif", "for", "while", "try", "except", 
    "finally", "with", "as", "in", "is", "not", "and", "or", "True", "False", "None",
	    }

	return mapeo