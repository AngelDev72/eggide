import flet as ft

def build_layout(page: ft.Page):
    sidebar = ft.Container(
        width=70,
        bgcolor=ft.colors.GREY_900,
        content=ft.Column(
            [
                ft.Icon(ft.icons.FOLDER),
                ft.Icon(ft.icons.CODE),
                ft.Icon(ft.icons.SETTINGS),
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=20,
        ),
        padding=10,
    )

    editor = ft.Container(
        expand=True,
        bgcolor=ft.colors.BLACK,
        content=ft.Text(
            "Editor 📝\n(próximamente poderoso)",
            color=ft.colors.GREEN_200,
        ),
        padding=10,
    )

    console = ft.Container(
        height=100,
        bgcolor=ft.colors.GREY_800,
        content=ft.Text(
            "Consola ▶ esperando órdenes...",
            size=12,
        ),
        padding=10,
    )

    return ft.Column(
        [
            ft.Row([sidebar, editor], expand=True),
            console,
        ],
        expand=True,
    )
