from asyncio import sleep
from dataclasses import dataclass, field
from random import choice

import flet as ft


@dataclass
@ft.observable
class Sorteados:
    inicio: int = 1
    maximo: int = 60
    valor: int = 0
    ultimo_valor: int | None = None
    fim: bool = False
    rodando: bool = False
    sorteados: list[int] = field(default_factory=list)
    cesta: list[int] = field(default_factory=lambda: list(range(1, 61)))

    async def _animar_sorteio(self) -> None:
        for _ in range(10):
            self.valor = choice(self.cesta)
            await sleep(0.12)

    async def rodar(self) -> None:
        if self.rodando:
            return
        if not self.cesta:
            self.fim = True
            return

        self.fim = False
        self.rodando = True
        try:
            await self._animar_sorteio()
            self.ultimo_valor = self.valor
            self.sorteados.append(self.valor)
            self.cesta.remove(self.valor)
            self.fim = not self.cesta
        finally:
            self.rodando = False

    def resetar(self) -> None:
        self.valor = 0
        self.ultimo_valor = None
        self.sorteados.clear()
        self.cesta = list(range(self.inicio, self.maximo + 1))
        self.fim = False

    def set_limite(self, limite: int) -> None:
        if limite < self.inicio:
            raise ValueError("O máximo precisa ser maior ou igual ao início.")
        self.maximo = limite
        self.resetar()

    def __str__(self) -> str:
        return " · ".join(f"{numero:02d}" for numero in self.sorteados) or "Nenhum número ainda"


def DialogoConfiguracao(limite: str, erro: str, on_change, on_cancel, on_confirm):
    return ft.AlertDialog(
        modal=True,
        bgcolor="#17233B",
        shape=ft.RoundedRectangleBorder(radius=22),
        title=ft.Text("Configurar sorteio", color=ft.Colors.WHITE),
        content=ft.Column(
            tight=True,
            spacing=12,
            controls=[
                ft.Text("Escolha o número máximo do intervalo.", color="#AAB7D0"),
                ft.TextField(
                    label="Número máximo",
                    value=limite,
                    keyboard_type=ft.KeyboardType.NUMBER,
                    on_change=on_change,
                    border={
                        ft.ControlState.DEFAULT: ft.OutlineInputBorder(
                            side=ft.BorderSide(color="#536987"),
                        ),
                        ft.ControlState.FOCUSED: ft.OutlineInputBorder(
                            side=ft.BorderSide(color="#7DE4D2", width=2),
                        ),
                    },
                    color=ft.Colors.WHITE,
                    autofocus=True,
                ),
                ft.Text(erro, color="#FF9D9D", size=13),
            ],
        ),
        actions=[
            ft.TextButton("Cancelar", on_click=on_cancel),
            ft.Button(
                "Aplicar e reiniciar",
                on_click=on_confirm,
                style=ft.ButtonStyle(bgcolor="#79E4D1", color="#10243A"),
            ),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )


def DialogoReinicio(on_cancel, on_confirm):
    return ft.AlertDialog(
        modal=True,
        bgcolor="#17233B",
        shape=ft.RoundedRectangleBorder(radius=22),
        title=ft.Text("Reiniciar sorteio?", color=ft.Colors.WHITE),
        content=ft.Text("Os números sorteados serão removidos.", color="#AAB7D0"),
        actions=[
            ft.TextButton("Cancelar", on_click=on_cancel),
            ft.Button("Reiniciar", on_click=on_confirm),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )


@ft.component
def App():
    state, _ = ft.use_state(Sorteados())
    show_reset, set_show_reset = ft.use_state(False)
    show_config, set_show_config = ft.use_state(False)
    config_limit, set_config_limit = ft.use_state(str(state.maximo))
    config_error, set_config_error = ft.use_state("")

    def abrir_configuracao(_):
        set_config_limit(str(state.maximo))
        set_config_error("")
        set_show_config(True)

    def confirmar_configuracao(_):
        try:
            maximo = int(config_limit)
            state.set_limite(maximo)
        except (TypeError, ValueError):
            set_config_error("Informe um número inteiro maior ou igual a 1.")
            return
        set_show_config(False)

    ft.use_dialog(
        DialogoReinicio(
            on_cancel=lambda _: set_show_reset(False),
            on_confirm=lambda _: (state.resetar(), set_show_reset(False)),
        )
        if show_reset
        else None
    )
    ft.use_dialog(
        DialogoConfiguracao(
            limite=config_limit,
            erro=config_error,
            on_change=lambda e: set_config_limit(e.control.value),
            on_cancel=lambda _: set_show_config(False),
            on_confirm=confirmar_configuracao,
        )
        if show_config
        else None
    )

    async def sortear(_):
        await state.rodar()

    menu = ft.PopupMenuButton(
        icon=ft.Icons.MORE_VERT,
        tooltip="Opções do sorteio",
        items=[
            ft.PopupMenuItem(
                content=ft.Text("Configurar intervalo"),
                on_click=abrir_configuracao,
            ),
            ft.PopupMenuItem(
                content=ft.Text("Reiniciar sorteio"),
                on_click=lambda _: set_show_reset(True),
            ),
        ],
    )

    return ft.Container(
        expand=True,
        padding=ft.Padding.symmetric(horizontal=24, vertical=28),
        image=ft.DecorationImage(src='images/Background.jpg', fit=ft.BoxFit.COVER),
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-0.9, -1),
            end=ft.Alignment(1, 1),
            colors=["#10162C", "#172C48", "#26385C"],
        ),
        content=ft.Column(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=24,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Column(
                            spacing=3,
                            controls=[
                                ft.Text("SORTEIO", size=13, weight=ft.FontWeight.BOLD, color="#79E4D1"),
                                ft.Text("Boa sorte!", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                            ],
                        ),
                        menu,
                    ],
                ),
                ft.Container(
                    width=480,
                    padding=ft.Padding.all(18),
                    border_radius=20,
                    bgcolor="#75131D33",
                    border=ft.Border.all(1, "#284A68"),
                    content=ft.Column(
                        spacing=8,
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Text("NÚMEROS SORTEADOS", size=12, weight=ft.FontWeight.BOLD, color="#91A5C5"),
                                    ft.Text(f"{len(state.sorteados)} números", size=12, color="#91A5C5"),
                                ],
                            ),
                            ft.Text(str(state), size=25, color=ft.Colors.WHITE, max_lines=3, overflow=ft.TextOverflow.ELLIPSIS),
                        ],
                    ),
                ),
                ft.Container(
                    width=480,
                    padding=ft.Padding.symmetric(horizontal=28, vertical=34),
                    border_radius=28,
                    bgcolor="#D9162035",
                    border=ft.Border.all(1, "#4AFFFFFF"),
                    shadow=ft.BoxShadow(blur_radius=36, spread_radius=1, color="#40000000", offset=ft.Offset(0, 16)),
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20,
                        controls=[
                            ft.Container(
                                padding=ft.Padding.symmetric(horizontal=16, vertical=9),
                                border_radius=30,
                                bgcolor="#2479E4D1",
                                content=ft.Text(
                                    f"{state.inicio} até {state.maximo}",
                                    size=15,
                                    weight=ft.FontWeight.BOLD,
                                    color="#A8FFF0",
                                ),
                            ),
                            ft.Text(
                                "FIM" if state.fim else f"{state.valor:02d}",
                                size=148,
                                weight=ft.FontWeight.BOLD,
                                color="#FFE08A",
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Button(
                                content=ft.Row(
                                    tight=True,
                                    spacing=10,
                                    controls=[ft.Icon(ft.Icons.CASINO_OUTLINED), ft.Text("SORTear".upper(), size=17, weight=ft.FontWeight.BOLD)],
                                ),
                                on_click=sortear,
                                disabled=state.rodando or state.fim,
                                style=ft.ButtonStyle(
                                    bgcolor="#79E4D1",
                                    color="#10243A",
                                    elevation=8,
                                    shadow_color="#6679E4D1",
                                    padding=ft.Padding.symmetric(horizontal=30, vertical=17),
                                    shape=ft.RoundedRectangleBorder(radius=16),
                                ),
                            ),
                        ],
                    ),
                ),
            ],
        ),
    )


def main(page: ft.Page):
    page.title = "Sorteio"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.render(App)


if __name__ == "__main__":
    ft.run(main)
