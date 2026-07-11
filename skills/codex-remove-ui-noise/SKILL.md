---
name: codex-remove-ui-noise
description: Remove implementation leakage, domain-spec text, explanatory microcopy, and unnecessary UI chrome from frontend interfaces. Use when auditing or building UX that feels like documentation, when generated screens explain their own intent, or when labels expose internal workflows instead of showing only necessary actions, states, and results.
---

# Codex Remove UI Noise

Treat the interface as a product surface, not as documentation for the code that built it.

## Core rule

Show only what helps the user decide, act, understand a meaningful state, or inspect a requested result. If text merely explains why a component exists, how the system is implemented, or what a business rule says, remove it from the primary UX.

Prefer deletion over rewriting. A shorter label is not a fix when the element should not exist.

## Audit workflow

1. Inspect the complete screen and nearby flows before editing.
2. Inventory visible copy and classify every item as one of:
   - **Action:** a button, input, navigation item, or control the user can use.
   - **State:** a short status needed to understand what is happening now.
   - **Result:** output the user came to inspect.
   - **Required context:** information needed to make the next decision.
   - **Leakage:** implementation rationale, domain specification, internal nouns, agent orchestration, or filler explanation.
3. Delete leakage by default. Move necessary domain detail to the exercise brief, README, help, or an explicit details view.
4. Keep required context concise and adjacent to the decision it supports.
5. Use plain, human labels. Prefer a verb or short noun phrase over a sentence.
6. Verify the first viewport, loading state, empty state, error state, success state, and responsive layouts after the cleanup.

## Copy rules

- Use `Salvar`, `Enviar`, `Aceitar`, `Rejeitar`, `Revisão`, `Testes`, and `Resultados` when those are the actual actions or destinations.
- Use `Carregando…`, `Salvando…`, `Falhou`, or a quiet visual indicator for transient state. Do not narrate internal work such as “the agent is reading the workspace and preparing a revisable response.”
- Do not expose words such as `workspace`, `orchestration`, `pipeline`, `agent loop`, `implementation`, or `business rule` unless they are essential product language.
- Do not place acceptance criteria, edge cases, architectural rationale, or retry policy in the main workspace.
- Do not add helper paragraphs merely to fill empty space or prove that a component has a purpose.
- Preserve accessible names for controls. If visible copy is intentionally minimal, use an accessible label or `aria-label`; do not remove semantics.
- Keep error messages actionable: state what failed and the one useful recovery action. Do not explain the entire call chain.

## Common transformations

| Avoid | Prefer |
|---|---|
| `Mensagem para o agente` | `Pergunte ao agente` or an accessible unlabeled prompt field |
| `O agente está lendo o workspace e preparando uma resposta revisável` | `Analisando…` |
| `Preservar conteúdo manual` as a prominent UI explanation | `Retry` or `Tentar novamente` as the action; keep the rule in the exercise brief |
| `Somente notificações pendentes criadas por automação podem atualizar…` | No primary-screen copy; expose under `Ver regras` only if needed |
| `Esta seção permite revisar o código antes e depois` | `Código antes/depois` |
| `O sistema executará uma validação segura…` | `Rodar testes` |

## AI and reviewer surfaces

For coding-agent and reviewer UX:

- Make the candidate's action obvious without explaining the agent's architecture.
- Show the proposal, diff, score, feedback, and evidence as results.
- Keep AI status transient and terse.
- Put transcript, before/after code, and test evidence behind direct disclosure controls when they are secondary.
- Never let the AI narrate internal intent as product copy.

## Decision test

Before keeping a visible sentence, ask:

> Does the user need this to act, understand the current state, or evaluate the result right now?

If no, delete it or move it out of the primary flow.

## Completion check

Confirm that:

- the primary screen contains actions, states, results, and only necessary context;
- domain rules live in the exercise/specification layer unless directly needed for a decision;
- loading and error states are terse and actionable;
- no component explains its own implementation;
- accessibility names remain intact;
- responsive layouts do not reintroduce explanatory clutter;
- the UI still works after copy removal, rather than relying on text as hidden control logic.
