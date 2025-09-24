# Control & Perception Knowledge Hub — README

**One-line:** a single-repo knowledge hub & portfolio template for learning, experimenting and showcasing work in
Model Predictive Control (MPC), Robust Control, Networked Control Systems (NCS), Sensor Fusion, and Machine-Learning for Perception & Control.

This README is  *complete navigation manual + contributor guide*. It explains the repository layout, how to use each folder, where to add new content (with expected formats), a beginner roadmap, contribution rules, and reproducible setup (Conda, pip, and Docker).
---

> **Quick links**
>
> * Root README (this file): `README.md`
> * Environment: `environment.yml` / `requirements.txt`
> * Example project (MPC): `projects/mpc-cartpole/`
> * Notebooks: `notebooks/`
> * Source code: `src/`
> * Literature: `literature/bib/master.bib`, `literature/summaries/`
> * Templates: `templates/`
> * CI workflow: `.github/workflows/ci.yml`

---

## Table of contents

1. [Purpose & goals](#purpose--goals)
2. [Top-level folder guide (what goes where)](#top-level-folder-guide-what-goes-where)
3. [How to use the repo (first steps and daily flows)](#how-to-use-the-repo-first-steps-and-daily-flows)
4. [Where and how to add new materials (formats & examples)](#where-and-how-to-add-new-materials-formats--examples)
5. [Roadmap for beginners (recommended learning path)](#roadmap-for-beginners-recommended-learning-path)
6. [Contribution guidelines & developer workflow](#contribution-guidelines--developer-workflow)
7. [Reproducibility: Conda / pip / Docker (how to set up and run)](#reproducibility-conda--pip--docker-how-to-set-up-and-run)
8. [Testing, CI, notebooks execution & tips](#testing-ci-notebooks-execution--tips)
9. [Project documentation templates & examples](#project-documentation-templates--examples)
10. [Publishing & showcasing (GitHub pages, badges, citations)](#publishing--showcasing-github-pages-badges-citations)
11. [License, citation, contact](#license-citation-contact)

---

## Purpose & goals

This repository is designed to:

* **Teach**: host tutorial Jupyter notebooks and structured learning modules for the five core topics.
* **Organize**: collect papers, summaries, and reference implementations (code snippets, small libraries).
* **Experiment**: contain small reproducible projects (not research-grade, but portfolio-ready).
* **Showcase**: provide ready-to-run demos and clear documentation so you can point employers or supervisors to reproducible work.
* **Scale**: offer templates and a consistent structure so you (or collaborators) can add new topics, data, or projects without chaos.

---

## Top-level folder guide (what goes where)

Use these rules when reading, adding, or reorganizing files.

```
control-perception-hub/
├─ README.md                 # this file
├─ LICENSE
├─ environment.yml           # conda environment for reproducibility
├─ requirements.txt          # pip fallback
├─ Dockerfile                # (optional) reproducible docker environment
├─ .github/                  # CI and GitHub templates
├─ docs/                     # built site / tutorials (MkDocs / Jupyter Book)
├─ notebooks/                # didactic Jupyter notebooks (topic-organized)
├─ projects/                 # self-contained demo projects (portfolio pieces)
├─ literature/               # bib database + summaries + zettelkasten notes
├─ src/                      # installable python package & reusable modules
├─ data/                     # small, curated datasets + download scripts
├─ assets/                   # images, GIFs used in READMEs and demos
├─ templates/                # notebook header, paper-summary, project proposal templates
└─ tests/                    # unit tests and smoke tests
```

### `notebooks/`

* Purpose: interactive tutorials, learning-first notebooks.
* Organization: numeric prefix `01_MPC/`, `02_RobustControl/`, `03_NetworkedControl/`, `04_SensorFusion/`, `05_ML_Perception/`.
* Naming convention: `NN_short-title.ipynb` (e.g., `01_MPC/mpc_cartpole_tutorial.ipynb`).
* Notebook header requirement: include a **Learning Goals** section, **Environment** cell (packages, Python version), and a **References** cell.
* Keep notebooks focused: aim for 10–30 cells and <20–30 minutes execution time for CI smoke tests.

### `projects/`

* Purpose: reproducible mini-projects/demos that can be shown in portfolio.
* Folder structure for each project:

  ```
  projects/<project-name>/
    README.md            # project summary, steps to reproduce, results
    environment.yml      # optional (project-specific)
    run_demo.py / main.py
    notebooks/            # one or more project-specific notebooks
    src/                  # project-specific modules (if needed)
    data/                 # small sample data (only if <= 10 MB)
    results/              # saved images, plots, GIFs, model weights
  ```
* README must include quick run instructions and expected outputs (screenshots/GIFs recommended).
* Keep each project self-contained so others can clone and run it quickly.

### `src/`

* Purpose: reusable python modules and the installable package.
* Conventions:

  * Package root under `src/` for `pip install -e .` compatibility.
  * Use `snake_case` module filenames and `CamelCase` classes.
  * Include docstrings and minimal unit tests in `tests/`.
* When adding new library modules, update `setup.py` / `pyproject.toml` and `requirements.txt` if new dependencies are required.

### `literature/`

* `bib/master.bib` — central BibTeX file for citations.
* `summaries/` — one markdown file per paper: `YYYY_author_short-title.md`.
* Summary file format (YAML front-matter + sections): title, authors, year, tags, bibkey; then 1-sentence summary, methods, results, notes, ideas.
* Tagging: add topical tags (e.g., `MPC`, `RobustControl`, `SLAM`) to the YAML header for automatic indexing later.

### `data/`

* Purpose: small, curated datasets for demos or tests.
* Conventions:

  * DO NOT commit large raw data (>50 MB) directly. Instead:

    * Add `data/scripts/download_<dataset>.sh` to fetch large files.
    * Or store smaller subsets (e.g. sample sequences) with clear provenance and license.
  * Place raw as `data/raw/` and processed as `data/processed/`.
* Formats recommended: CSV for tabular, NPZ/HDF5 for numpy arrays, TFRecord for TensorFlow, small images as `.png`. Include a short `README.md` describing the dataset and source/DOI.

### `docs/`

* Purpose: generated site (MkDocs / Jupyter Book).
* Contains pages that collate tutorials, project overviews, and literature indexes.
* Build & deploy: docs are built by `mkdocs build` or `jupyter-book build` and can be published to GitHub Pages.

### `templates/`

* Keep canonical templates for:

  * Notebook header (`templates/notebook_header.md`)
  * Paper summary (`templates/paper-summary.md`)
  * Project proposal (`templates/project_proposal.md`)
  * Issue & PR templates (in `.github/`)

### `.github/`

* Contains CI workflows and GitHub issue/PR templates.
* Keep PR checklist and `CONTRIBUTING.md` here.

### `tests/`

* Use `pytest` to run unit tests for `src/` modules.
* Keep CI-friendly smoke tests (fast, deterministic) here.

---

## How to use the repo — first steps & daily workflows

### 1) Clone & install (recommended)

```bash
git clone https://github.com/<your-username>/control-perception-hub.git
cd control-perception-hub
```

**Conda (recommended)**:

```bash
conda env create -f environment.yml
conda activate control-hub
pip install -e .
```

**Pip (if you don’t use Conda)**:

```bash
python -m pip install -r requirements.txt
pip install -e .
```

### 2) Run the example demo (MPC cart-pole)

```bash
python projects/mpc-cartpole/run_demo.py
# results saved to projects/mpc-cartpole/results_demo.png
```

Open the generated PNG in `projects/mpc-cartpole/results_demo.png`.

### 3) Open a notebook

```bash
jupyter lab
# or
jupyter notebook
```

Navigate to a notebook in `notebooks/<topic>/` and run the cells. Follow the **Learning goals** and **Exercises** sections.

### 4) Add a new paper summary

* Copy `templates/paper-summary.md` into `literature/summaries/` as `YYYY_authors_short.md`.
* Fill YAML fields: title, authors, year, tags, bibkey.
* Add 1-sentence summary, key methods, notable results, and 2–3 takeaway points.

### 5) Start a new project

* Create `projects/<your-project>/` following the project structure above.
* Add a README with Quick Run, Dependencies, and Expected Outputs.
* Add a small notebook that demonstrates the result and a `run_demo.py` script to reproduce core outputs.

---

## Where and how to add new materials — expected formats & examples

### Notebooks

* Location: `notebooks/<NN_Topic>/your_notebook.ipynb`
* Naming: `NN_short-description.ipynb` (e.g., `01_MPC/mpc_linear_qp.ipynb`)
* Required header cells:

  * Title & one-sentence description
  * **Learning goals**
  * **Environment** (Python version & major packages)
  * **References**
* Keep notebooks deterministic and set seeds for reproducibility.

### Code

* Location: `src/<package>/...` for reusable libraries, `projects/<project>/src/` for project-specific code.
* File formatting: follow PEP8; use `black` and `isort` pre-commit hooks.
* Unit tests: add tests in `tests/` mirroring the package (e.g., `tests/test_my_module.py`).
* Packaging: update `setup.py` / `pyproject.toml` when adding top-level packages.

### Data

* Small files (≤ 10 MB): may be committed in `projects/<project>/data/` or `data/raw/`.
* Large files (> 10–50 MB): do **not** commit. Add a download script `data/scripts/download_<name>.sh` and a small README describing the source and how to obtain credentials (if needed).
* Data format conventions: CSV/TSV for tabular, NPZ/HDF5 for arrays, PNG/JPEG for images (no TIFFs > 10MB).

### Literature

* Add BibTeX entry to `literature/bib/master.bib`.
* Add summary markdown file in `literature/summaries/` with front-matter.
* Tag summaries for indexing: `tags: [MPC, survey, 2021]`.

### Documentation & Tutorials

* Write docs in Markdown in `docs/` or re-use notebook conversion (`notebook -> markdown`) for tutorials.
* Add a top-level docs index linking to topic pages.

---

## Roadmap learning path inside this repo

**Goal:** get from conceptual understanding → small reproducible project → portfolio-ready demo

1. **Explore literature (week 1):**

   * Read `literature/bib/master.bib` top entries and their `summaries/`.
   * Add 3–5 short summaries for papers you read.

2. **Hands-on notebooks (week 1–2):**

   * Start `notebooks/01_MPC/mpc_cartpole_tutorial.ipynb`: run it, inspect the code.
   * Move to `notebooks/04_SensorFusion/ekf_imu_gps.ipynb` to learn EKF basics.

3. **Mini projects (weeks 2–4):**

   * Fork `projects/mpc-cartpole/`: extend it with constrained MPC (do-mpc) or add plotting and a GIF artifact.
   * Build `projects/ekf-ukf-compare/` to compare EKF and UKF on simulated trajectories.

4. **Intermediate (weeks 4–8):**

   * Implement a small networked control experiment (`notebooks/03_NetworkedControl/`) simulating packet drops and event-triggered control.
   * Explore ML perception: fine-tune a small object detector on a toy dataset in `projects/`.

5. **Polish & showcase (week 8+):**

   * Write clear project READMEs, add GIFs in `assets/`, generate docs, and ensure reproducibility (environment.yml, Dockerfile).
   * Submit one project as a portfolio piece with a short report.

---

## Contribution guidelines & developer workflow

We welcome contributions! The goal is to keep the repository useful, reproducible and easy to follow.

### How to contribute

1. Fork the repo and create a feature branch: `feature/<short-description>` (e.g., `feature/mpc-demo-improvement`).
2. Open an issue describing the planned change and link it to the PR.
3. Implement changes, add tests (if code), and update docs/templates as needed.
4. Submit a PR referencing an issue. Maintain a clean commit history.

### Branch naming

* `feature/<topic>-<short>`
* `bugfix/<short>`
* `fix/ci-<short>`

### PR checklist (add as PR template)

* [ ] Followed formatting (`black`, `isort`)
* [ ] Added/updated unit tests and they pass locally
* [ ] Updated `requirements.txt` or `environment.yml` if dependencies changed
* [ ] Added documentation (README, notebooks, or docs) where applicable
* [ ] For large data — added download scripts, not the dataset itself

### Issue tagging & labels

Use labels such as: `good first issue`, `documentation`, `project`, `notebook`, `bug`, `enhancement`, `thesis`, `help wanted`.

### Code style & pre-commit

* Use `black` and `isort`. We recommend installing pre-commit hooks:

```bash
pip install pre-commit
pre-commit install
```

Modify `.pre-commit-config.yaml` to include `black`, `isort`, `ruff`/`flake8`.

---

## Reproducibility: Conda / pip / Docker

You have three reproducibility options. Pick one and stick with it.

### 1) Conda (recommended)

```bash
conda env create -f environment.yml
conda activate control-hub
pip install -e .
```

* `environment.yml` contains conda channels + a pip section for packages not available in conda.
* If you add new packages, update BOTH `environment.yml` and `requirements.txt`.

### 2) Pip only

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

### 3) Docker (containerized reproducibility)

```
content
```

---

## Testing, CI, and executing notebooks

### Tests

* Run unit tests:

```bash
pytest -q
```

* Keep tests small and deterministic (no long training jobs or long simulations).

### Notebook smoke tests

* CI runs a smoke notebook execution (see `.github/workflows/ci.yml`).
* Notebooks intended for CI should run within 5–10 minutes and avoid external downloads or heavy GPU tasks.

### Executing a notebook locally (and saving output)

```bash
jupyter nbconvert --to notebook --execute notebooks/01_MPC/mpc_cartpole_tutorial.ipynb \
  --output notebooks/01_MPC/mpc_cartpole_tutorial_executed.ipynb \
  --ExecutePreprocessor.timeout=600
```

For programmatic execution in scripts, use `papermill` or `nbclient`.

---

## Project documentation templates & examples

### Project README checklist

Every `projects/<project>/README.md` should contain:

* Project title and 1-line description
* What it demonstrates (methods & expected results)
* Quick setup & run commands
* Files layout (where to find notebooks, code, data)
* Reproducibility notes (commit hash, environment)
* Screenshot/GIF of results
* License and citation (if you used datasets or models)

### Notebook header

Top cells to include in every notebook:

1. Title & short description
2. Learning goals (3 bullet points)
3. Environment (Python + major libs + pip/conda instructions)
4. Reproducibility seeds (set `np.random.seed`, `torch.manual_seed`)
5. Short table of contents or links to sections

### Paper summary (markdown)

Place a summary in `literature/summaries/` using `templates/paper-summary.md`. Always include DOI and BibTeX key.

---

## Publishing

* Use `docs/` (MkDocs or Jupyter Book) to aggregate tutorials and project listings. Configure automatic builds on push using GitHub Actions.
* Add badges to the repository README:

  * Build/CI status
  * Python version
  * License
  * Papers / Downloads (if relevant)
* Use `assets/` to store a small `demo.gif` (≤ 3 MB) for the root README so visitors grasp your work quickly.

---

## Common FAQs & troubleshooting

**Q: Notebook fails in CI due to missing heavy dependency (e.g., CasADi)?**
A: Keep CI notebooks lightweight. Create a separate workflow that runs heavy notebooks optionally (manually or with larger runners), and document the requirements in `projects/<project>/environment.yml`.

**Q: Where do I put a new dataset?**
A: Add small sample data to `projects/<project>/data/`. For large datasets, add a `data/scripts/download_<name>.sh` script and provide instructions in the project README.

**Q: How do I cite this repo?**
A: Add a `CITATION.cff` file at the root (optional). For now, include a `citation` section in your project README if you want others to reference your work.

---

## License, citation & contact

* **License:** MIT (see `LICENSE` for full text).
* **Citation:** If you build on this hub for academic work, cite core papers you used; optionally add `CITATION.cff` with repository metadata.
* **Contact:** Add your preferred contact information in `README.md` or your GitHub profile. For supervision / thesis, list a supervisor/contact in project READMEs.

---

## Wrap-up / checklist

run through this checklist before opening a PR:

* [ ] Does the addition have a short README or header explaining purpose?
* [ ] Are notebooks deterministic (set seeds) and documented with learning goals?
* [ ] Have you updated `environment.yml` / `requirements.txt` if you added dependencies?
* [ ] Did you add tests or smoke-exec notebooks where appropriate?
* [ ] Are large data files excluded from git and instead downloaded via scripts?
* [ ] Did you follow code style (black/isort) and add or update tests?
* [ ] Does the PR description reference an Issue or clearly explain what’s being added and why?

---
