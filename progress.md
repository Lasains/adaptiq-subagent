# SDD ledger — plan: PRD.md

Ruling: Initialize dedicated git tracking at repository root d:/backup/prd — allows exact commit range isolation for tasks per SDD contract — cost if wrong: commit ranges would reference external parent repo and pollute workspace history.
Ruling: Offline deterministic fallbacks retain full parity with PRD schemas when GEMINI_API_KEY is not set or offline — enables 100% test reproducibility and zero network flake in automated test harness — cost if wrong: tests fail in CI or offline environments.
