---
name: flet-deprecations
description: >-
  Use esta skill sempre que for escrever, refatorar ou sugerir código utilizando o framework Flet.
  Esta skill fornece a lista de componentes e métodos depreciados e os seus respectivos substitutos modernos (ex: page.go, page.launch_url).
---

# Guia de Depreciações do Flet

Você está atuando em uma base de código Flet moderna. É estritamente proibido utilizar código, componentes ou propriedades desativadas. Sempre consulte a lista abaixo e utilize o MCP `flet-oficial` em caso de dúvidas.

## Mapeamento de Substitutos Oficiais

Abaixo estão os métodos depreciados encontrados no Flet e os seus **substitutos corretos** que DEVEM ser utilizados:

### Métodos e Propriedades de `Page`:

- **Evitar:** `page.go(...)`
  **Substituto:** Use `page.push_route(...)` para navegação de rotas.

- **Evitar:** `page.launch_url(...)`
  **Substituto:** Use a classe de serviço utilitária instanciando `UrlLauncher().launch_url(...)`.

- **Evitar:** `page.can_launch_url(...)`
  **Substituto:** Use `UrlLauncher().can_launch_url(...)`.

- **Evitar:** `page.close_in_app_web_view(...)`
  **Substituto:** Use `UrlLauncher().close_in_app_web_view(...)`.

- **Evitar:** `page.client_storage`
  **Substituto:** Use a classe de serviço utilitária `SharedPreferences()`.

- **Evitar:** `page.clipboard`
  **Substituto:** Use a classe de serviço utilitária `Clipboard()`.

- **Evitar:** `page.browser_context_menu`
  **Substituto:** Use a classe de serviço utilitária `BrowserContextMenu()`.

- **Evitar:** `page.storage_paths`
  **Substituto:** Use a classe de serviço utilitária `StoragePaths()`.

### Outras Funções e Classes do Flet:

- **Evitar:** Módulo `ft.colors` (ex: `ft.colors.RED`)
  **Substituto:** Use a classe Enum em maiúsculo `ft.Colors` (ex: `ft.Colors.RED`).

- **Evitar:** Módulo `ft.icons` (ex: `ft.icons.HOME`)
  **Substituto:** Use a classe Enum em maiúsculo `ft.Icons` (ex: `ft.Icons.HOME`).

- **Evitar:** Funções do módulo `ft.alignment` (ex: `ft.alignment.center`)
  **Substituto:** Use a classe principal `ft.Alignment` ou o respectivo Enum `ft.Alignment(...)`.

- **Evitar:** Módulo `ft.border` (ex: `ft.border.all(...)`)
  **Substituto:** Use a classe principal `ft.Border(...)` e as classes auxiliares `ft.BorderSide(...)`.

- **Evitar:** Propriedades estilísticas diretas no `ft.ElevatedButton` (como color, bgcolor, etc. se aplicável)
  **Substituto:** Use o objeto `style=ft.ButtonStyle(...)` no `ElevatedButton` para definir propriedades de estilo.

- **Evitar:** `ft.app(target=...)`
  **Substituto:** A propriedade `target` foi descontinuada, utilize o argumento `main` em vez dela: `ft.app(main=...)`.

## Regras Estruturais (Regras Globais do Projeto)

- **Evite:** `page.update()` manual (em abordagens declarativas).
  **Substituto:** Use `@ft.observable` e componentes marcados com `@ft.component`, injetando o estado para atualização reativa automática pelo framework.

## Validação via MCP `flet-oficial`

Sempre que houver incerteza sobre um controle, propriedade ou se algum outro método está depreciado:
1. Use a tool `call_mcp_tool` para acionar o servidor `flet-oficial`.
2. Utilize `list_controls` ou `get_api` para verificar a assinatura e a documentação oficial.
3. Prefira componentes e padrões modernos listados no MCP.
