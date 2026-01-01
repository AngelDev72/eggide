import flet as ft
import flet as ft


def main(page: ft.Page):
    page.title = "EGGIDE"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.spacing = 0

    # -----------------
    # STATE
    # -----------------
    sidebar_visible = True

    # -----------------
    # SIDEBAR
    # -----------------
    sidebar = ft.Container(
        width=220,
        bgcolor=ft.colors.SURFACE,
        padding=10,
        content=ft.Column(
            controls=[
                ftclear.Text("📁 Projects", weight="bold"),
                ft.Text("main.py", size=12),
                ft.Text("boot.py", size=12),
                ft.Divider(),
                ft.Text("🔌 Devices", weight="bold"),
                ft.Text("ESP32 • USB", size=12),
                ft.Divider(),
                ft.Text("🧠 Eggbert", weight="bold"),
                ft.Text("Todo estable", size=12),
            ],
        ),
    )

    # -----------------
    # SIDEBAR TOGGLE
    # -----------------
    def toggle_sidebar(e):
        nonlocal sidebar_visible
        sidebar_visible = not sidebar_visible
        sidebar.visible = sidebar_visible
        sidebar.width = 220 if sidebar_visible else 0
        page.update()

    # -----------------
    # TOPBAR BUTTONS
    # -----------------
    btn_play = ft.IconButton(ft.icons.PLAY_ARROW, tooltip="Run")
    btn_upload = ft.IconButton(ft.icons.UPLOAD, tooltip="Upload")
    btn_stop = ft.IconButton(ft.icons.STOP, tooltip="Stop")
    btn_settings = ft.IconButton(ft.icons.SETTINGS, tooltip="Settings")

    actions_row = ft.Row(
        spacing=10,
        alignment=ft.MainAxisAlignment.END,
        controls=[
            btn_play,
            btn_upload,
            btn_stop,
            btn_settings,
        ],
    )

    # -----------------
    # TOPBAR
    # -----------------
    topbar = ft.Container(
        height=48,
        padding=ft.padding.symmetric(horizontal=10),
        bgcolor=ft.colors.SURFACE_VARIANT,
        content=ft.Row(
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.IconButton(
                    icon=ft.icons.MENU,
                    tooltip="Toggle sidebar",
                    on_click=toggle_sidebar,
                ),
                ft.Text("🥚 EGGIDE", weight="bold"),
                ft.VerticalDivider(width=15),
                ft.Text("Proyecto: chickntec", size=12),
                ft.Container(expand=True),  # spacer dinámico
                actions_row,
            ],
        ),
    )

    # -----------------
    # EDITOR
    # -----------------
    editor = ft.TextField(
        value="# Bienvenido a EGGIDE\nprint('Hola mundo 🥚')",
        multiline=True,
        expand=True,
        border=ft.InputBorder.NONE,
        text_size=14,
        cursor_color=ft.colors.GREEN,
    )

    editor_container = ft.Container(
        expand=True,
        bgcolor=ft.colors.BLACK,
        padding=10,
        content=editor,
    )

    # -----------------
    # TERMINAL
    # -----------------
    terminal = ft.TextField(
        value=">>> REPL listo\n",
        multiline=True,
        expand=True,
        border=ft.InputBorder.NONE,
        text_size=12,
    )

    terminal_container = ft.Container(
        height=150,
        bgcolor=ft.colors.SURFACE_VARIANT,
        padding=10,
        content=terminal,
    )

    # -----------------
    # LAYOUT
    # -----------------
    page.add(
        ft.Column(
            expand=True,
            spacing=0,
            controls=[
                topbar,
                ft.Row(
                    expand=True,
                    spacing=0,
                    controls=[
                        sidebar,
                        ft.Column(
                            expand=True,
                            spacing=0,
                            controls=[
                                editor_container,
                                terminal_container,
                            ],
                        ),
                    ],
                ),
            ],
        )
    )

    # -----------------
    # RESPONSIVE LOGIC
    # -----------------
    def on_resize(e):
        nonlocal sidebar_visible
        w = page.width

        # ---- Sidebar ----
        if w < 600:
            sidebar_visible = False
            sidebar.visible = False
            sidebar.width = 0
        elif w < 1024:
            sidebar_visible = True
            sidebar.visible = True
            sidebar.width = 60
        else:
            sidebar_visible = True
            sidebar.visible = True
            sidebar.width = 220

        # ---- Topbar buttons ----
        if w < 600:
            actions_row.alignment = ft.MainAxisAlignment.CENTER
            actions_row.spacing = 20
            btn_play.visible = True
            btn_upload.visible = False
            btn_stop.visible = False
            btn_settings.visible = False

        elif w < 1024:
            actions_row.alignment = ft.MainAxisAlignment.SPACE_AROUND
            actions_row.spacing = 30
            btn_play.visible = True
            btn_upload.visible = True
            btn_stop.visible = False
            btn_settings.visible = False

        else:
            actions_row.alignment = ft.MainAxisAlignment.END
            actions_row.spacing = 10
            btn_play.visible = True
            btn_upload.visible = True
            btn_stop.visible = True
            btn_settings.visible = True

        page.update()

    page.on_resize = on_resize
    on_resize(None)  # ajuste inicial


ft.app(
    target=main,
    view=ft.WEB_BROWSER,
    host="0.0.0.0",
    port=8550,
)
