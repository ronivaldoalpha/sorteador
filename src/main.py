from asyncio import sleep
import flet as ft
from dataclasses import dataclass, field
from random import randint, choice

# Teste com dataclass e com ft.component
class Pop_UP(ft.AlertDialog):
    def __init__(self, titulo: str, on_cancel, on_confirm):
        super().__init__()
        self.title = ft.Text(titulo)
        self.actions = [
            ft.IconButton(
                icon=ft.Icons.CANCEL_OUTLINED,
                on_click=on_cancel
            ),
            ft.IconButton(
                icon=ft.Icons.CHECK_CIRCLE_OUTLINE,
                on_click=on_confirm
            )
        ]

class ConfigDialog(ft.AlertDialog):
    def __init__(self, on_cancel, on_confirm):
        super().__init__()
        self.tf_limite = ft.TextField(label="Novo Limite", keyboard_type=ft.KeyboardType.NUMBER)

        def handle_confirm(e):
            try:
                val = int(self.tf_limite.value)
                on_confirm(val)
            except ValueError:
                pass # Ignora entradas inválidas por enquanto

        self.title = ft.Text("Configurar Sorteio")
        self.content = self.tf_limite
        self.actions = [
            ft.TextButton("Cancelar", on_click=on_cancel),
            ft.TextButton("Confirmar", on_click=handle_confirm)
        ]


# 1. Definindo a Classe de Estado Observável
@dataclass
@ft.observable
class Sorteados:
    valor: int = 0
    utimo_valor: int = None
    fim: bool = False
    rodando: bool = False
    sorteados: list[int] = field(default_factory=list)
    cesta: list[int] = field(default_factory=lambda: list(range(1, 101)))

    # Métodos funcionais
    async def __randowm(self):
        for _ in range(10):
            self.valor = choice(self.cesta)

            await sleep(0.2)
        return self.valor

    # Métodos que alteram o estado
    async def rodar(self):
        if len(self.cesta) == 0:
            self.fim = True
            return

        if self.fim:
            self.fim = False

        self.rodando = True
        await self.__randowm()
        self.utimo_valor = self.valor
        self.sorteados.append(self.valor)
        self.cesta.remove(self.valor)
        self.rodando = False
        
    def resetar(self):
        self.valor = 0
        self.utimo_valor = None
        self.sorteados.clear()
        self.cesta = list(range(1, 61))
        self.fim = False

    def set_limite(self, limite: int):
        self.cesta = list(range(1, limite+1))
        self.resetar()
    
    def __str__(self) -> str:
        return "-".join(f'{i:02d}' for i in self.sorteados) or 'Nenhum'


# 3. App Principal gerenciando a instância do estado
@ft.component
def App():
    # Instanciamos o estado apenas uma vez aqui no topo da nossa aplicação
    state, _ = ft.use_state(Sorteados())
    show_popup, set_show_popup = ft.use_state(False)
    show_config, set_show_config = ft.use_state(False)

    def on_confirm_reset(e):
        state.resetar()
        set_show_popup(False)

    def on_confirm_config(val):
        state.set_limite(val)
        set_show_config(False)

    ft.use_dialog(
        Pop_UP(
            titulo='Deseja realmente Reiniciar o Sorteio?',
            on_cancel=lambda _: set_show_popup(False),
            on_confirm=on_confirm_reset
        ) if show_popup else None
    )

    ft.use_dialog(
        ConfigDialog(
            on_cancel=lambda _: set_show_config(False),
            on_confirm=on_confirm_config
        ) if show_config else None
    )

    async def handle_rodar(e):
        await state.rodar()

    painel = ft.Row(
        alignment=ft.MainAxisAlignment.START,
        controls=[
            ft.Text(
                value=f"{state if state.utimo_valor is not None else 'Nenhum'}",
                size=20
            )
        ]
    )

    texto = ft.Text(
        value=f"{state.valor:02d}" if not state.fim else f'Fim',
        size=150,
        color=ft.Colors.AMBER,
    )

    btn_rodar = ft.Button(
        content=ft.Text(value='RODAR',size=20),
        on_click=handle_rodar,
        disabled=state.rodando,
        autofocus=True,
        style=ft.ButtonStyle(
            elevation=3,
            side=ft.BorderSide(
                width=0.5,
                color=ft.Colors.WHITE_30,
            ),
            shadow_color=ft.Colors.BLUE,
        )
    )

    bnt_menu = ft.PopupMenuButton(
        content=ft.Icon(ft.Icons.MENU),
        items=[
            ft.PopupMenuItem(
                content=ft.Text('Reiniciar Sorteio'),
                on_click=lambda _: set_show_popup(True),
            ),
            ft.PopupMenuItem(
                content=ft.Text('Configurar Sorteio'),
                on_click=lambda _: set_show_config(True)
            )
        ]
    )

    interface = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
        controls=[
            painel,
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    texto
                ],
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    btn_rodar
                ]
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.END,
                margin=ft.Margin.only(top=100),
                controls=[
                    bnt_menu
                ]
            )
        ],
    )

    return ft.Container(
        expand=True,
        padding=0,
        margin=0,
        alignment=ft.Alignment.TOP_CENTER,
        bgcolor=ft.Colors.BLACK,
        image=ft.DecorationImage(
            src='background.jpg',
            fit=ft.BoxFit.COVER,
            opacity=0.3
        ),
        content=interface
    )

def main(page: ft.Page):
    page.window.maximized = True
    page.render(App)

ft.run(main)