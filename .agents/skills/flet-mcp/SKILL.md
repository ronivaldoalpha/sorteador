---
name: flet-mcp
description: Consultar a API versionada do Flet e usar as ferramentas MCP para controles, serviços, enums, ícones e exemplos. Use ao escrever, revisar ou depurar código Flet.
---

# Flet MCP

Use as ferramentas MCP do Flet para verificar a API que está indexada no servidor conectado antes de escrever ou corrigir código Flet.

## Verificar símbolos e APIs

- Se o nome de um controle, serviço, tipo, evento, enum ou função for conhecido, consulte `get_api(name)` primeiro. A resposta "not found" é negativa para a versão/indexação consultada pelo servidor.
- Use `member` para obter detalhes completos de uma propriedade, evento ou método; use `query` para filtrar membros. Use `format="json"` quando precisar dos tipos estruturados.
- Confira `package`: se apontar para algo diferente de `flet`, informe a dependência de extensão correspondente antes de propor o import.
- Trate métodos marcados `async: true` como assíncronos: devem ser aguardados e chamados por um handler `async def`.
- Use `list_controls` para descobrir controles e serviços. Ela também pode listar classes-base e tipos auxiliares, mas não enumera todos os dataclasses, eventos e enums. Para esses símbolos, consulte `get_api` pelo nome conhecido.
- Use `find_icon` para buscar um ícone por conceito. Para enum members, use `get_enum`, `search_enum_members` ou `enum_has_member`.

## Exemplos e limites

- Se `search_examples` e `get_example` estiverem disponíveis, pesquise exemplos e recupere o exemplo completo antes de adaptá-lo.
- Se as ferramentas de exemplos não estiverem disponíveis, habilite-as no ambiente do processo MCP com `FLET_MCP_ENABLE_EXAMPLES=1` e reinicie o servidor/cliente. No Codex, configure a variável em `[mcp_servers.flet.env]`.
- A documentação oficial do Flet informa que `search_docs` e `get_doc` ainda não estão habilitados. Não afirme que o MCP pode pesquisar a documentação; para explicações que não estejam na API indexada, consulte a documentação oficial do Flet.
- Os grupos API e Icons ficam habilitados por padrão; Examples e CLI são opcionais. As ferramentas realmente disponíveis nesta sessão são a fonte para saber quais grupos estão ativos.

## Catálogo

Consulte [references/catalog.md](references/catalog.md) para a lista de controles/serviços e pacotes de extensão encontrados na indexação atual. O catálogo é um instantâneo informativo; verifique sempre a API com `get_api` antes de depender de um símbolo.
