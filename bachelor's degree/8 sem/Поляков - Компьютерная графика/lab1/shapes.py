from PyQt6.QtGui import QPen, QBrush, QColor

class Shape:
    def __init__(self, shape_type, position):
        self.shape_type = shape_type
        self.position = position

    def paint(self, painter):
        print(f"🖌️ Рисую: {self.shape_type}")
        x, y = int(self.position.x()), int(self.position.y())
        
        # ГИГАНТСКИЙ КРАСНЫЙ КВАДРАТ 100x100 - НЕВОЗМОЖНО НЕ УВИДЕТЬ!
        painter.fillRect(x-50, y-50, 100, 100, QColor(255, 0, 0))
        
        if self.shape_type == "Сруглённый квадрат":
            painter.setPen(QPen(QColor(0, 0, 0), 3))
            painter.setBrush(QBrush(QColor(0, 191, 255)))
            painter.drawRoundedRect(x-30, y-60, 60, 120, 15, 15)
        
        elif self.shape_type == "Три круга в треугольнике":
            radius = 30
            painter.setPen(QPen(QColor(0, 0, 0), 3))
            painter.setBrush(QBrush(QColor(255, 105, 180)))
            
            # Три БОЛЬШИХ круга
            painter.drawEllipse(x, y-radius*1.5, radius*2, radius*2)      # Верх
            painter.drawEllipse(x-radius, y+10, radius*2, radius*2)        # Левый низ
            painter.drawEllipse(x+radius-20, y+10, radius*2, radius*2)     # Правый низ

    def get_region(self):
        return (0, 0, 100, 100)

