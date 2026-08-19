# Version Control Workflow — MLOps Iris Classifier

## 1. Overview
This document describes the Git-based version control workflow used for this Machine Learning project, developed as part of MLOps Lab Experiment 2.
- **Repository:** https://github.com/<your-username>/mlops-iris-classifier
- **Primary language:** Python

## 2. Branching Strategy
| Branch | Purpose |
|---|---|
| `main` | Stable, always-deployable code |
| `develop` | Integration branch for day-to-day development |
| `feature/<name>` | Individual features, branched from and merged into `develop` |
| `conflict-demo-*` | Demonstration branches created for conflict resolution practice |

**Rule:** No direct commits to `main`. All changes flow: `feature/*` → Pull Request → `develop` → `main`[cite: 1].

## 3. Commit Convention
Commits follow a short, imperative style with a type prefix[cite: 1]:
- `feat:` new feature[cite: 1]
- `fix:` bug fix[cite: 1]
- `docs:` documentation changes[cite: 1]
- `chore:` tooling/config changes[cite: 1]
- `refactor:` code change with no behavior change[cite: 1]

## 4. Standard Workflow
```bash
git switch develop[cite: 1]
git pull origin develop[cite: 1]
git switch -c feature/<short-description>[cite: 1]
# ... make changes ...
git add <files>[cite: 1]
git commit -m "feat: <description>"[cite: 1]
git push -u origin feature/<short-description>[cite: 1]