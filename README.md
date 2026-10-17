# Sorteio

Aplicação de sorteios numéricos feita com Flet.

## Publicar no GitHub Pages

O workflow em `.github/workflows/github-pages.yml` gera uma versão estática do app
e publica no GitHub Pages. Ele executa o build em pull requests para `main`, mas
publica o site quando há push em `main` ou quando o workflow é iniciado
manualmente pela aba **Actions**.

Para ativar a publicação no repositório:

1. Abra **Settings → Pages**.
2. Em **Build and deployment → Source**, selecione **GitHub Actions**.
3. Envie o workflow para o GitHub. Após o primeiro deploy, acompanhe o resultado
   na aba **Actions**; o endereço do site aparece no ambiente `github-pages`.

O workflow define o caminho base a partir do nome do repositório, então funciona
para o Pages de projeto (`/<nome-do-repositório>/`). O app roda no navegador como
site estático usando Pyodide; o Python e as dependências são carregados pelo
cliente.

As dependências de execução contêm somente `flet`, que é compatível com o
ambiente web estático. Ao atualizar o Flet, mantenha `flet`, `flet-cli`,
`flet-desktop`, `flet-web` e `flet[test]` na mesma versão no `pyproject.toml`.

## Run the app

### uv

Run as a desktop app:

```bash
uv run flet run
```

Run as a web app:

```bash
uv run flet run --web
```

For more details on running the app, refer to the [Getting Started Guide](https://flet.dev/docs/).

## Build the app

### Android

```bash
flet build apk -v
```

For more details on building and signing `.apk` or `.aab`, refer to the [Android Packaging Guide](https://flet.dev/docs/publish/android/).

### iOS

```bash
flet build ipa -v
```

For more details on building and signing `.ipa`, refer to the [iOS Packaging Guide](https://flet.dev/docs/publish/ios/).

### macOS

```bash
flet build macos -v
```

For more details on building macOS package, refer to the [macOS Packaging Guide](https://flet.dev/docs/publish/macos/).

### Linux

```bash
flet build linux -v
```

For more details on building Linux package, refer to the [Linux Packaging Guide](https://flet.dev/docs/publish/linux/).

### Windows

```bash
flet build windows -v
```

For more details on building Windows package, refer to the [Windows Packaging Guide](https://flet.dev/docs/publish/windows/).

### Web

```bash
flet build web -v
```

For more details on building Web app, refer to the [Web Packaging Guide](https://flet.dev/docs/publish/web/).
