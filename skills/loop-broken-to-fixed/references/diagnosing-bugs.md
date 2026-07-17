# Diagnosing Bugs

Use for non-tiny failures or whenever more than one cause is plausible.

## Tight Feedback Loop

The verifier must be red-capable, deterministic, fast enough to repeat, and runnable by the agent. Reproduce and minimize before broad inspection. If production-only evidence prevents a local red test, state the limitation and use the narrowest reliable sensor.

## Hypotheses

Maintain 3–5 ranked, falsifiable hypotheses when the space is unclear. For each one record why it is plausible, evidence for and against, and the cheapest falsification step. Change one variable at a time.

## Evidence

- Add tagged temporary instrumentation only when existing signals are insufficient.
- For performance, record a baseline and use a profiler or trace before changing code.
- Prefer a regression test at the seam that owns the behavior. If no testable seam exists, record the architecture gap instead of faking coverage.

## Exit

Rerun the original scenario and the regression seam. Remove debug logs, flags, probes, and throwaway prototypes before completion.
