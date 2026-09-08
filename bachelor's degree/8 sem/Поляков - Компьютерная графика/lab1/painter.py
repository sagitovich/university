from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QPainter, QPen, QColor, QAction, QBrush
from PyQt6.QtCore import Qt
from shapes import Shape

class PainterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Painter")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: white;")
        self.current_shape = None
        self.shapes = []
        self.create_menu()

    def create_menu(self):
        menubar = self.menuBar()
        shapes_menu = menubar.addMenu("Фигуры")

        square_action = QAction("Сруглённый квадрат", self)
        square_action.triggered.connect(lambda: self.select_shape("Сруглённый квадрат"))
        shapes_menu.addAction(square_action)

        three_circles_action = QAction("Три круга в треугольнике", self)
        three_circles_action.triggered.connect(lambda: self.select_shape("Три круга в треугольнике"))
        shapes_menu.addAction(three_circles_action)

    def select_shape(self, shape_name):
        self.current_shape = shape_name
        print(f"✅ Выбран инструмент: {self.current_shape}")

    def mousePressEvent(self, event):
        if self.current_shape:
            print(f"🖱️ Клик в: {event.position()}")
            new_shape = Shape(self.current_shape, event.position())
            self.shapes.append(new_shape)
            print(f"📊 Фигур всего: {len(self.shapes)}")
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        # УБРАЛИ painter.begin() и painter.end()!
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        print("🎨 Рисуем фигуры...")
        for shape in self.shapes:
            shape.paint(painter)
        # НЕ вызываем painter.end()!
