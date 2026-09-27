---
name: flet-architecture
description: >-
  Use esta skill sempre que for criar novos arquivos, estruturar o projeto Flet, refatorar a base de código ou decidir em qual diretório um novo componente, página ou serviço deve ser colocado. Ela define a arquitetura escalável e a organização de pastas obrigatórias para o projeto.
---

# Arquitetura Escalável do Projeto Flet

Sempre que for adicionar novas funcionalidades ou refatorar o projeto, você DEVE respeitar a seguinte estrutura de pastas. Cada diretório tem uma finalidade específica projetada para manter o sistema robusto, organizado e escalável.

## Estrutura de Diretórios e Regras

### `database/`
- **Finalidade:** Modelos de banco de dados e serviços de conexão.
- **Regra:** Utilizar exclusivamente o **SQLAlchemy 2.0**.
- **Exemplo de conteúdo:** Configuração da *engine*, sessões (`sessionmaker`), definição de tabelas (classes mapeadas) e operações de CRUD.

### `services/`
- **Finalidade:** Lógica de negócios de backend e integrações com o sistema.
- **Regra:** Armazenar serviços que atuam nos bastidores. Nenhuma interface de usuário (`ft.Control`) deve ser definida aqui.
- **Exemplo de conteúdo:** Clientes de APIs externas, envios de e-mail (SMTP), integrações de pagamento, *cron jobs*/programações de tarefas de fundo, etc.

### `modules/`
- **Finalidade:** Elementos básicos de UI (Atômicos) altamente reutilizáveis.
- **Regra:** São componentes menores de interface gráfica que não dependem do contexto de uma página inteira. Devem ser agnósticos de regra de negócio, baseados unicamente em propriedades visuais e eventos de clique.
- **Exemplo de conteúdo:** Botões personalizados, pequenos cartões estilizados, formatação de tabelas simples, dicionários de temas (fontes, estilos) e paletas de cores.

### `models/`
- **Finalidade:** Elementos complexos e blocos maiores de interface (Moleculares/Organismos).
- **Regra:** São composições mais densas construídas muitas vezes a partir de componentes do diretório `modules/`. Costumam possuir estado próprio ou dependências diretas de lógica de tela.
- **Exemplo de conteúdo:** `Header`, `Sidebar`, `AppBar`, Tabelas paginadas avançadas, `Date_picker` customizado, formulários e *Pop-ups* (Diálogos) comuns a várias páginas.

### `layouts/`
- **Finalidade:** Estruturas base das páginas que definem a disposição dos componentes na tela.
- **Regra:** Servem como os "esqueletos" (templates) estruturais onde as interfaces finais serão injetadas. Lidam com a responsividade geral do aplicativo.
- **Exemplo de conteúdo:** Layouts responsivos para Mobile, Desktop, lógica de remanejamento/ocultamento de `Sidebar`, e *grids* principais das páginas.

### `utils/`
- **Finalidade:** Funções puras e utilitários que não dependem do framework Flet nem de banco de dados.
- **Regra:** Devem ser funções soltas, estáticas ou pequenos módulos focados em resolver um único problema computacional recorrente.
- **Exemplo de conteúdo:** Conversão de unidades/medidas, formatação de moedas/textos, cálculos matemáticos, cálculos e tratamentos de data/hora (`datetime`), e geradores de hashes ou senhas.

### `interfaces/`
- **Finalidade:** Telas e páginas finais da aplicação (Views).
- **Regra:** É aqui que ocorre a junção das partes: os layouts, os models, os modules e os serviços. Estas páginas devem ser desenhadas para serem carregadas no `main.py` conforme o sistema de rotas (Router).
- **Exemplo de conteúdo:** `HomeView`, `LoginView`, `DashboardView`, `SettingsView`. Nenhuma lógica de banco de dados direta; elas consomem o que está em `services/` e `database/`.

## Fluxo de Trabalho (Workflow)

Quando você (agente) for solicitado a criar uma nova tela ou funcionalidade:
1. **Identifique a camada:** Coloque utilitários matemáticos em `utils/`. Coloque conexão com banco de dados no `database/`.
2. **Construa de baixo para cima na UI:** Primeiro, crie pequenos botões em `modules/`. Agrupe-os em painéis no `models/`. Encaixe o painel no esqueleto em `layouts/`. Finalmente, renderize tudo na página pronta em `interfaces/`.
3. Mantenha as regras do Flet atualizadas, como o uso preferencial do `@ft.component` e `@ft.observable` descritas no seu contexto.
