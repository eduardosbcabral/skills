# Batch Grill Me

Use this decision interview only when unresolved choices block the current state transition.

## Frontier Round

1. Read available domain docs, glossary, ADRs, source artifacts, and current code before asking.
2. Build the **decision frontier**: independent decisions that are unresolved and currently answerable.
3. Ask the whole frontier in one batch. For each decision provide:
   - the concrete question;
   - why it matters now;
   - 2–3 materially different options;
   - a recommended answer and tradeoff.
4. Do not include dependent questions until their prerequisites are answered.
5. Reconcile answers with source facts and domain language. Expose contradictions; do not silently choose for the user.
6. Repeat with the next frontier. Stop when no blocking decision remains and confirm the settled result.

Facts discoverable from the environment are research tasks, not interview questions. The user owns product and business decisions.
