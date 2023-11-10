import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import numpy as np

vertices_tetrahedron = [
    (0, 1, 0),
    (1, -1, -1),
    (-1, -1, -1),
    (0, -1, 1)
]

faces_tetrahedron = [
    (0, 1, 2),
    (0, 1, 3),
    (0, 2, 3),
    (1, 2, 3)
]


def draw_sphere(radius=1.0, slices=50, stacks=50):
    """
        Отрисовывает сферу с заданными параметрами

        :param radius: радиус сферы
        :param slices: количество сегментов вдоль долготы
        :param stacks: количество сегментов вдоль широты
        """
    for j in range(0, stacks):
        lat0 = math.pi * (-0.5 + (j / float(stacks)))
        z0 = math.sin(lat0)
        zr0 = math.cos(lat0)

        lat1 = math.pi * (-0.5 + ((j + 1) / float(stacks)))
        z1 = math.sin(lat1)
        zr1 = math.cos(lat1)

        glBegin(GL_LINE_STRIP)  # Изменили тип примитива на GL_LINE_STRIP
        for i in range(0, slices + 1):
            lng = 2 * math.pi * (i / float(slices))
            x = math.cos(lng)
            y = math.sin(lng)

            glNormal3f(x * zr0, y * zr0, z0)
            glVertex3f(x * zr0, y * zr0, z0)
            glNormal3f(x * zr1, y * zr1, z1)
            glVertex3f(x * zr1, y * zr1, z1)
        glEnd()


def draw_tetrahedron():
    """
    Отрисовывает тетраэдр
    """
    glBegin(GL_TRIANGLES)
    for face in faces_tetrahedron:
        for vertex in face:
            glVertex3fv(vertices_tetrahedron[vertex])
    glEnd()


def check_intersection(vertex, radius):
    """
      Проверяет, пересекает ли заданная точка тетраэдр с заданным радиусом

      :param vertex: координаты точки
      :param radius: радиус
      :return: True, если точка пересекает тетраэдр, иначе False
      """
    distances = [np.linalg.norm(np.array(vertex) - np.array(v)) for v in vertices_tetrahedron]
    return any(d <= radius for d in distances)


import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import numpy as np

vertices_tetrahedron = [
    (0, 1, 0),
    (1, -1, -1),
    (-1, -1, -1),
    (0, -1, 1)
]

faces_tetrahedron = [
    (0, 1, 2),
    (0, 1, 3),
    (0, 2, 3),
    (1, 2, 3)
]


def draw_sphere(radius=1.0, slices=50, stacks=50):
    """
        Отрисовывает сферу с заданными параметрами

        :param radius: радиус сферы
        :param slices: количество сегментов вдоль долготы
        :param stacks: количество сегментов вдоль широты
        """
    for j in range(0, stacks):
        lat0 = math.pi * (-0.5 + (j / float(stacks)))
        z0 = math.sin(lat0)
        zr0 = math.cos(lat0)

        lat1 = math.pi * (-0.5 + ((j + 1) / float(stacks)))
        z1 = math.sin(lat1)
        zr1 = math.cos(lat1)

        glBegin(GL_LINE_STRIP)  # Изменили тип примитива на GL_LINE_STRIP
        for i in range(0, slices + 1):
            lng = 2 * math.pi * (i / float(slices))
            x = math.cos(lng)
            y = math.sin(lng)

            glNormal3f(x * zr0, y * zr0, z0)
            glVertex3f(x * zr0, y * zr0, z0)
            glNormal3f(x * zr1, y * zr1, z1)
            glVertex3f(x * zr1, y * zr1, z1)
        glEnd()


def draw_tetrahedron():
    """
    Отрисовывает тетраэдр
    """
    glBegin(GL_TRIANGLES)
    for face in faces_tetrahedron:
        for vertex in face:
            glVertex3fv(vertices_tetrahedron[vertex])
    glEnd()


def check_intersection(vertex, radius):
    """
      Проверяет, пересекает ли заданная точка тетраэдр с заданным радиусом

      :param vertex: координаты точки
      :param radius: радиус
      :return: True, если точка пересекает тетраэдр, иначе False
      """
    distances = [np.linalg.norm(np.array(vertex) - np.array(v)) for v in vertices_tetrahedron]
    return any(d <= radius for d in distances)


def main():
    """
    Основная функция, отвечающая за инициализацию окна и отрисовку сцены
    """
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    rotation_speed = 1.0  # Скорость вращения

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            glRotatef(rotation_speed, 0, 1, 0)
        if keys[pygame.K_RIGHT]:
            glRotatef(-rotation_speed, 0, 1, 0)
        if keys[pygame.K_UP]:
            glRotatef(rotation_speed, 1, 0, 0)
        if keys[pygame.K_DOWN]:
            glRotatef(-rotation_speed, 1, 0, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)
        glColor3f(0.5, 0.1, 1.0)
        draw_sphere()

        glColor3f(1.0, 1.0, 0.0)
        draw_tetrahedron()

        sphere_center = (0, 0, 0)
        sphere_radius = 1.0
        if check_intersection(sphere_center, sphere_radius):
            glColor3f(0.0, 1.0, 0.0)
            draw_tetrahedron()

            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            glEnable(GL_POLYGON_OFFSET_FILL)
            glPolygonOffset(-1, -1)
            draw_tetrahedron()
            glDisable(GL_POLYGON_OFFSET_FILL)
            glDisable(GL_BLEND)

        pygame.display.flip()
        pygame.time.wait(20)


if __name__ == "__main__":
    main()
