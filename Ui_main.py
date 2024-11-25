import flet as ft
import numpy as np
from flet_core import InputBorder, BorderRadius
from flet_core.cupertino_colors import WHITE

from Ui_vectors import Vectors
from Ui_matrix import Matrix
from Ui_presets import Presets

def main(page: ft.Page):
    page.fonts = {
        "Intro1": "C:/Users/Tima/Algebra/matrix_and_Vectors_withUI/fronts/IntroDemo-BlackCAPS.otf",
        "Forum": "C:/Users/Tima/Algebra/matrix_and_Vectors_withUI/fronts/Forum-Regular.ttf",
    }

    vector_fields_a = []
    vector_fields_b = []
    matrix_a_fields = []
    matrix_b_fields = []
    rows = 2
    cols = 2

    def switch_view(view_name):
        if view_name == "vectors":
            page.views.append(vectors_view())
        elif view_name == "matrices":
            page.views.append(matrices_view())
        page.update()

    def go_back(e):
        page.window_resizable = False
        page.window_maximizable = False
        page.window_width = 1150
        page.window_height = 550
        if len(page.views) > 1:
            page.views.pop()
            page.update()

    def main_view():
        page.window_resizable = False
        page.window_maximizable = False
        page.window_width = 1150
        page.window_height = 550
        return ft.View(
            "/",
            controls=[
                ft.Text("Выполнить операцию над...", size=34, color=ft.colors.WHITE, style=ft.TextStyle(font_family="Forum")),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            "Векторы",
                            bgcolor= "#0cc0df",
                            on_click=lambda _: switch_view("vectors"),
                            width=150,
                            height=150,
                            style=ft.ButtonStyle(text_style=ft.TextStyle(font_family="Intro1"))
                        ),
                        ft.ElevatedButton(
                            "Матрицы",
                            bgcolor="#ff5757",
                            on_click=lambda _: switch_view("matrices"),
                            width=150,
                            height=150,
                            style=ft.ButtonStyle(text_style=ft.TextStyle(font_family="Intro1"))
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            bgcolor="#ffde59",
        )

    def vectors_view():
        page.window_resizable = False
        page.window_maximizable = False
        def add_remove_field(e):
            nonlocal vector_fields_a, vector_fields_b
            if e.control.text == "+":
                if len(vector_fields_a) < 5 and len(vector_fields_b) < 5:
                    vector_fields_a.append(
                        ft.Container(
                            content=ft.TextField(
                                width=50,
                                bgcolor=WHITE,
                                border=ft.InputBorder.NONE,
                            ),
                            border_radius=ft.border_radius.BorderRadius(
                                top_left=10, top_right=10, bottom_left=10, bottom_right=10
                            ),
                            bgcolor=WHITE,
                            padding=ft.padding.all(5),
                        )
                    )

                    vector_fields_b.append(
                        ft.Container(
                            content=ft.TextField(
                                width=50,
                                bgcolor=WHITE,
                                border=ft.InputBorder.NONE,
                            ),
                            border_radius=ft.border_radius.BorderRadius(
                                top_left=10, top_right=10, bottom_left=10, bottom_right=10
                            ),
                            bgcolor=WHITE,
                            padding=ft.padding.all(5),
                        )
                    )
            elif e.control.text == "-":
                if len(vector_fields_a) > 1 and len(vector_fields_b) > 1:
                    vector_fields_a.pop()
                    vector_fields_b.pop()
            vector_a_container.controls.clear()
            vector_b_container.controls.clear()
            for field in vector_fields_a:
                vector_a_container.controls.append(field)
            for field in vector_fields_b:
                vector_b_container.controls.append(field)
            page.update()

        vector_a_container = ft.Row(spacing=5)
        vector_b_container = ft.Row(spacing=5)
        for _ in range(3):
            vector_fields_a.append(
                ft.Container(
                    content=ft.TextField(
                        width=50,
                        bgcolor=WHITE,
                        border=ft.InputBorder.NONE,
                    ),
                    border_radius=ft.border_radius.BorderRadius(
                        top_left=10, top_right=10, bottom_left=10, bottom_right=10
                    ),
                    bgcolor=WHITE,
                    padding=ft.padding.all(5),
                )
            )

            vector_fields_b.append(
                ft.Container(
                    content=ft.TextField(
                        width=50,
                        bgcolor=WHITE,
                        border=ft.InputBorder.NONE,
                    ),
                    border_radius=ft.border_radius.BorderRadius(
                        top_left=10, top_right=10, bottom_left=10, bottom_right=10
                    ),
                    bgcolor=WHITE,
                    padding=ft.padding.all(5),
                )
            )

            vector_a_container.controls.append(vector_fields_a[-1])
            vector_b_container.controls.append(vector_fields_b[-1])

        def perform_vector_operation(e):
            try:
                vector_a = [int(field.content.value) for field in vector_fields_a if field.content.value]
                vector_b = [int(field.content.value) for field in vector_fields_b if field.content.value]

                if not vector_a or not vector_b:
                    page.dialog = ft.AlertDialog(
                        title=ft.Text("Ошибка", style=ft.TextStyle(font_family="Intro1"), color="#ff5757"),
                        content=ft.Text("Векторы не могут быть пустыми", style=ft.TextStyle(font_family="Intro1")),
                        actions=[
                            ft.TextButton("OK", on_click=lambda e: close_dialog())
                        ],
                    )
                    page.dialog.open = True
                    page.update()
                    return

                if len(vector_a) != len(vector_b):
                    page.dialog = ft.AlertDialog(
                        title=ft.Text("Ошибка", style=ft.TextStyle(font_family="Intro1"), color="#ff5757"),
                        content=ft.Text("Векторы должны быть одинаковой длины",
                                        style=ft.TextStyle(font_family="Intro1")),
                        actions=[
                            ft.TextButton("OK", on_click=lambda e: close_dialog())
                        ],
                    )
                    page.dialog.open = True
                    page.update()
                    return

                isGr = False

                vectors = Vectors(vector_a, vector_b)
                result = 0
                if e.control.text == "Сложение":
                    result = vectors.add()
                    isGr = False
                elif e.control.text == "Вычитание":
                    result = vectors.subtract()
                    isGr = False
                elif e.control.text == "Скалярное произвидение":
                    result = vectors.scalar()
                    isGr = False
                elif e.control.text == "Умножение на скаляр":
                    scalar_dialog(vectors)
                    isGr = False
                elif e.control.text == "График":
                    return vectors.plot()
                    isGr = True
                elif e.control.text == "Модуль 2х векторов":
                    magnitude_a = np.linalg.norm(vectors.vectorA)
                    magnitude_b = np.linalg.norm(vectors.vectorB)
                    result = f"Модуль вектора A: {magnitude_a}, Модуль вектора B: {magnitude_b}"
                    isGr = False

                if isGr == False:
                    page.dialog = ft.AlertDialog(
                        title=ft.Text("Результат", style=ft.TextStyle(font_family="Intro1")),
                        content=ft.Text(f"{result}"),
                        actions=[
                            ft.TextButton("OK", on_click=lambda e: close_dialog())
                        ],
                    )
                    page.dialog.open = True
                    page.update()

            except ValueError:
                page.dialog = ft.AlertDialog(
                    title=ft.Text("Ошибка", style=ft.TextStyle(font_family="Intro1"), color="#ff5757"),
                    content=ft.Text("Введите числа", style=ft.TextStyle(font_family="Intro1")),
                    actions=[
                        ft.TextButton("OK", on_click=lambda e: close_dialog())
                    ],
                )
                page.dialog.open = True
                page.update()

        def plot_vectors(e):
            try:
                vector_a = [int(field.content.value) for field in vector_fields_a if field.content.value]
                vector_b = [int(field.content.value) for field in vector_fields_b if field.content.value]

                if not vector_a or not vector_b:
                    page.dialog = ft.AlertDialog(
                        title=ft.Text("Ошибка", style=ft.TextStyle(font_family="Intro1"), color="#ff5757"),
                        content=ft.Text("Векторы не могут быть пустыми", style=ft.TextStyle(font_family="Intro1")),
                        actions=[
                            ft.TextButton("OK", on_click=lambda e: close_dialog())
                        ],
                    )
                    page.dialog.open = True
                    page.update()
                    return

                if len(vector_a) != len(vector_b):
                    page.dialog = ft.AlertDialog(
                        title=ft.Text("Ошибка", style=ft.TextStyle(font_family="Intro1"), color="#ff5757"),
                        content=ft.Text("Векторы должны быть одинаковой длины",
                                        style=ft.TextStyle(font_family="Intro1")),
                        actions=[
                            ft.TextButton("OK", on_click=lambda e: close_dialog())
                        ],
                    )
                    page.dialog.open = True
                    page.update()
                    return

                vectors = Vectors(vector_a, vector_b)
                vectors.plot()

            except ValueError as ex:
                page.dialog = ft.AlertDialog(
                    title=ft.Text("Ошибка", style=ft.TextStyle(font_family="Intro1"), color="#ff5757"),
                    content=ft.Text(f"Введите числа. {ex}", style=ft.TextStyle(font_family="Intro1")),
                    actions=[
                        ft.TextButton("OK", on_click=lambda e: close_dialog())
                    ],
                )
                page.dialog.open = True
                page.update()


            except ValueError as ex:
                page.dialog = ft.AlertDialog(
                    title=ft.Text("Ошибка", style=ft.TextStyle(font_family="Intro1"), color="#ff5757"),
                    content=ft.Text(f"Введите числа. {ex}", style=ft.TextStyle(font_family="Intro1")),
                    actions=[
                        ft.TextButton("OK", on_click=lambda e: close_dialog())
                    ],
                )
                page.dialog.open = True
                page.update()

        def scalar_dialog(vectors):
            def scalar_operation(e):
                try:
                    scalar = float(scalar_field.value)
                    result = vectors.scalar_multiply(scalar)
                    page.dialog = ft.AlertDialog(
                        title=ft.Text("Результат", style=ft.TextStyle(font_family="Intro1")),
                        content=ft.Text(f"Вектор A: {result[0]}, Вектор B: {result[1]}", style=ft.TextStyle(font_family="Intro1")),
                        actions=[
                            ft.TextButton("OK", on_click=lambda e: close_dialog())
                        ],
                    )
                    page.dialog.open = True
                    page.update()
                except ValueError:
                    page.dialog = ft.AlertDialog(
                        title=ft.Text("Ошибка", style=ft.TextStyle(font_family="Intro1"), color="#ff5757"),
                        content=ft.Text("Введите число", style=ft.TextStyle(font_family="Intro1")),
                        actions=[
                            ft.TextButton("OK", on_click=lambda e: close_dialog())
                        ],
                    )
                    page.dialog.open = True
                    page.update()

            scalar_field = ft.TextField(label="Введите скаляр", text_style=ft.TextStyle(font_family="Intro1"))
            page.dialog = ft.AlertDialog(
                title=ft.Text("Скаляр", style=ft.TextStyle(font_family="Intro1")),
                content=scalar_field,
                actions=[
                    ft.TextButton("OK", on_click=scalar_operation),
                ],
            )
            page.dialog.open = True
            page.update()

        def close_dialog():
            page.dialog.open = False
            page.update()

        return ft.View(
            "/vectors",
            controls=[
                ft.ElevatedButton("Назад", on_click=go_back, style=ft.ButtonStyle(text_style=ft.TextStyle(font_family="Intro1"))),
                ft.Text("Введите координаты векторов A и B:", size=18, style=ft.TextStyle(font_family="Intro1"), color=WHITE),
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Text("Вектор A", style=ft.TextStyle(font_family="Intro1")),
                                vector_a_container,
                            ]
                        ),
                        ft.Column(
                            controls=[
                                ft.Text("Вектор B", style=ft.TextStyle(font_family="Intro1")),
                                vector_b_container,
                            ]
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton("+", on_click=add_remove_field),
                        ft.ElevatedButton("-", on_click=add_remove_field),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Сложение", on_click=perform_vector_operation, style=ft.ButtonStyle(text_style=ft.TextStyle(font_family="Intro1"))),
                        ft.ElevatedButton("Вычитание", on_click=perform_vector_operation, style=ft.ButtonStyle(text_style=ft.TextStyle(font_family="Intro1"))),
                        ft.ElevatedButton("Умножение на скаляр", on_click=perform_vector_operation, style=ft.ButtonStyle(text_style=ft.TextStyle(font_family="Intro1"))),
                        ft.ElevatedButton("Скалярное произвидение", on_click=perform_vector_operation, style=ft.ButtonStyle(text_style=ft.TextStyle(font_family="Intro1"))),
                        ft.ElevatedButton("Модуль 2х векторов", on_click=perform_vector_operation, style=ft.ButtonStyle(text_style=ft.TextStyle(font_family="Intro1"))),
                        ft.ElevatedButton("График", on_click=plot_vectors, style=ft.ButtonStyle(text_style=ft.TextStyle(font_family="Intro1"))),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            ],
            bgcolor="#0cc0df",
        )

    def matrices_view():
        page.window_resizable = True
        page.window_maximizable = True
        def add_row_col(e):
            nonlocal rows, cols, matrix_a_fields, matrix_b_fields
            rows += 1
            cols += 1
            update_matrix_fields()

        def remove_row_col(e):
            nonlocal rows, cols
            if rows > 1 and cols > 1:  # Минимум 1 строка и 1 столбец
                rows -= 1
                cols -= 1
                update_matrix_fields()

        plus = ft.ElevatedButton("+", on_click=add_row_col)
        minus = ft.ElevatedButton("-", on_click=remove_row_col)

        def update_matrix_fields():
            nonlocal matrix_a_fields, matrix_b_fields
            matrix_a_fields = []
            matrix_b_fields = []
            for i in range(rows):
                row_a = []
                row_b = []
                for j in range(cols):
                    field_a = ft.TextField(width=50)
                    field_b = ft.TextField(width=50)
                    row_a.append(field_a)
                    row_b.append(field_b)
                matrix_a_fields.append(row_a)
                matrix_b_fields.append(row_b)

            matrix_a_container.controls.clear()
            matrix_b_container.controls.clear()
            for row in matrix_a_fields:
                matrix_a_container.controls.append(ft.Row(controls=row))
            for row in matrix_b_fields:
                matrix_b_container.controls.append(ft.Row(controls=row))
            page.update()

        matrix_a_container = ft.Column()
        matrix_b_container = ft.Column()
        update_matrix_fields()

        def perform_matrix_operation(e):
            try:
                matrix_a = []
                matrix_b = []
                for row in matrix_a_fields:
                    matrix_a.append([int(field.value) for field in row if field.value])
                for row in matrix_b_fields:
                    matrix_b.append([int(field.value) for field in row if field.value])

                if not matrix_a or not matrix_b:
                    page.dialog = ft.AlertDialog(
                        title=ft.Text("Ошибка", style = ft.TextStyle(font_family="Intro1"), color="#ff5757"),
                        content=ft.Text("Матрицы не могут быть пустыми", style = ft.TextStyle(font_family="Intro1")),
                        actions=[
                            ft.TextButton("OK", on_click=lambda e: close_dialog())
                        ],
                    )
                    page.dialog.open = True
                    page.update()
                    return

                matrix = Matrix(matrix_a, matrix_b)
                
                result = 0

                isMatrix = False
                if e.control.text == "Сложение":
                    result = matrix.add()
                    isMatrix = True
                elif e.control.text == "Вычитание":
                    result = matrix.subtract()
                    isMatrix = True
                elif e.control.text == "Транспонирование":
                    result = (matrix.transpose(matrix.matrixA), matrix.transpose(matrix.matrixB))
                    isMatrix = True
                elif e.control.text == "Скаляр":
                    result = scalar_dialog(matrix)
                    isMatrix = True
                elif e.control.text == "Определитель":
                    result = matrix.determinant()
                    isMatrix = False

                if isMatrix == True:
                    result_text = ""
                    if isinstance(result, tuple):
                        for res in result:
                            result_text += "\n".join([" ".join(map(str, row)) for row in res]) + "\n\n"
                    else:
                        result_text = "\n".join([" ".join(map(str, row)) for row in result])

                    page.dialog = ft.AlertDialog(
                        title=ft.Text("Результат", style=ft.TextStyle(font_family="Intro1")),
                        content=ft.Text(result_text),
                        actions=[
                            ft.TextButton("OK", on_click=lambda e: close_dialog())
                        ],
                    )
                    page.dialog.open = True
                    page.update()

                if isMatrix == False:
                    page.dialog = ft.AlertDialog(
                        title=ft.Text("Результат", style=ft.TextStyle(font_family="Intro1")),
                        content=ft.Text(f"{result}"),
                        actions=[
                            ft.TextButton("OK", on_click=lambda e: close_dialog())
                        ],
                    )
                    page.dialog.open = True
                    page.update()

            except ValueError:
                page.dialog = ft.AlertDialog(
                    title=ft.Text("Ошибка", style = ft.TextStyle(font_family="Intro1"), color="#ff5757"),
                    content=ft.Text("Введите числа", style = ft.TextStyle(font_family="Intro1")),
                    actions=[
                        ft.TextButton("OK", on_click=lambda e: close_dialog())
                    ],
                )
                page.dialog.open = True
                page.update()

        def scalar_dialog(matrix):
            def scalar_operation(e):
                try:
                    scalar = float(scalar_field.value)
                    result = matrix.scalar_multiply(scalar)
                    result_text = f"Матрица A:\n{result[0]}\n\nМатрица B:\n{result[1]}"
                    page.dialog = ft.AlertDialog(
                        title=ft.Text("Результат", style = ft.TextStyle(font_family="Intro1")),
                        content=ft.Text(result_text),
                        actions=[
                            ft.TextButton("OK", on_click=lambda e: close_dialog())
                        ],
                    )
                    page.dialog.open = True
                    page.update()
                except ValueError:
                    page.dialog = ft.AlertDialog(
                        title=ft.Text("Ошибка", style = ft.TextStyle(font_family="Intro1"), color="#ff5757"),
                        content=ft.Text("Введите число", style = ft.TextStyle(font_family="Intro1")),
                        actions=[
                            ft.TextButton("OK", on_click=lambda e: close_dialog())
                        ],
                    )
                    page.dialog.open = True
                    page.update()

            scalar_field = ft.TextField(label="Введите скаляр", text_style=ft.TextStyle(font_family="Intro1"))
            page.dialog = ft.AlertDialog(
                title=ft.Text("Скаляр", style=ft.TextStyle(font_family="Intro1")),
                content=scalar_field,
                actions=[
                    ft.TextButton("OK", on_click=scalar_operation),
                ],
            )
            page.dialog.open = True
            page.update()

        def close_dialog():
            page.dialog.open = False
            page.update()

        return ft.View(
            "/matrices",
            controls=[
                ft.ElevatedButton("Назад", on_click=go_back, style=ft.ButtonStyle(text_style=ft.TextStyle(font_family="Intro1"))),
                ft.Text("Введите элементы матрицы A и B:", size=18, style=ft.TextStyle(font_family="Intro1"), color=WHITE),
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Text("Матрица A", style=ft.TextStyle(font_family="Intro1"), color=WHITE),
                                matrix_a_container,
                            ]
                        ),
                        ft.Column(
                            controls=[
                                ft.Text("Матрица B", style=ft.TextStyle(font_family="Intro1"), color=WHITE),
                                matrix_b_container,
                            ]
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                ),
                ft.Row(
                    controls=[
                        plus,
                        minus
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Определитель", on_click=perform_matrix_operation, width=150, style=ft.ButtonStyle(text_style=ft.TextStyle(font_family="Intro1"))),
                        ft.ElevatedButton("Сложение", on_click=perform_matrix_operation, width=150, style=ft.ButtonStyle(text_style=ft.TextStyle(font_family="Intro1"))),
                        ft.ElevatedButton("Вычитание", on_click=perform_matrix_operation, width=150, style=ft.ButtonStyle(text_style=ft.TextStyle(font_family="Intro1"))),
                        ft.ElevatedButton("Скаляр", on_click=perform_matrix_operation, width=150, style=ft.ButtonStyle(text_style=ft.TextStyle(font_family="Intro1"))),
                        ft.ElevatedButton("Транспонирование", on_click=perform_matrix_operation, width=180, style=ft.ButtonStyle(text_style=ft.TextStyle(font_family="Intro1"))),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
            ],
            bgcolor="#ff5757",
        )

    page.views.append(main_view())
    page.update()

ft.app(target=main, assets_dir="assets")