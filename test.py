import unittest
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from main import draw_sphere, draw_tetrahedron

class TestDrawFunctions(unittest.TestCase):
    def setUp(self):
        """
        Установка окружения для тестов.
        Инициализация Pygame, создание окна и настройка OpenGL.
        """
        pygame.init()
        self.display = (800, 600)
        pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)
        gluPerspective(45, (self.display[0] / self.display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)

    def tearDown(self):
        """
        Завершение окружения после выполнения тестов.
        Освобождение ресурсов Pygame.
        """
        pygame.quit()

    def test_draw_sphere(self):
        """
        Тестирование функции draw_sphere.
        Проверяет, что функция не вызывает ошибок при отрисовке сферы.
        """
        self.assertIsNone(draw_sphere())

    def test_draw_tetrahedron(self):
        """
        Тестирование функции draw_tetrahedron.
        Проверяет, что функция не вызывает ошибок при отрисовке тетраэдра.
        """
        self.assertIsNone(draw_tetrahedron())
