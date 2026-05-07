# ops-setup

CLI para bootstrap de **One Person Squad** em repositórios GitHub.

## O que este projeto faz

`ops-setup` conecta no seu GitHub, permite escolher um repositório e configura automaticamente a base operacional do fluxo agentic:

- cria labels de status do fluxo (`status: idea`, `status: in-progress`, etc.);
- configura secrets do provider selecionado (`gemini`, `claude`, `copilot`, `codex`);
- cria branch de setup (`feat/ops-setup`);
- adiciona arquivos padrão de operação:
  - `.github/workflows/agentic-squad.yml` (workflow multi-provider);
  - `.github/copilot-instructions.md`;
  - `.agentic/SQUAD.md` e `.agentic/GUARDRAILS.md`;
  - skills em `.agentic/skills/*` e `.agents/*`;
- abre um Pull Request com todas as mudanças.

## O que ele facilita na adoção do One Person Squad

- reduz setup manual e erros de configuração inicial;
- padroniza o fluxo de status, papéis e guardrails entre times/repos;
- acelera ativação de providers de IA com secrets e workflow prontos;
- entrega um PR único para revisão e rastreabilidade da adoção.

## Pré-requisitos

- Python `>= 3.12`
- `uv` instalado
- token GitHub com permissões para:
  - ler e escrever no repositório;
  - criar labels, secrets e pull requests.

Defina o token no ambiente:

```bash
export GITHUB_TOKEN=seu_token_aqui
```

## Como executar

```bash
make run
```

Ou:

```bash
uv build
uv run ops-setup
```

Durante a execução, você escolhe:

1. repositório no GitHub;
2. provider (`gemini`, `claude`, `copilot` ou `codex`);
3. valor do secret solicitado.

## Resultado esperado

Ao final, o repositório selecionado terá:

1. labels padrão do ciclo de trabalho;
2. branch `feat/ops-setup` com arquivos de configuração do One Person Squad;
3. PR aberto para revisão/merge da configuração inicial.
