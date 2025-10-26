# pg-game

Minimal 2D game starter template — a small, extensible base for rapid prototyping and learning with Python + Pygame (or swap in another engine).

## Table of contents
- Description
- Features
- Quick start
- Running
- Configuration
- Project structure
- Development
- Contributing
- License

## Description
A focused, easy-to-extend project layout that provides a simple game loop, input and sprite handling, collision basics, and a place to add scenes/screens.

## Features
- Lightweight game loop and scene manager
- Sprite and input helpers
- Basic collision and scoring examples
- Configurable settings for fast iteration
- Ready for unit testing and CI

## Quick start
Prerequisites:
- Python 3.8+
- pip

Clone and install:
```bash
git clone <repo-url> pg-game
cd pg-game
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running
From the project root:
```bash
python -m pg_game.main
# or
python run.py
```
Tip: run from the project root so asset paths resolve correctly.

## Configuration
- `pg_game/config.py` holds default game settings (resolution, FPS, debug flags).
- Override settings with environment variables or a local config file (implement as needed).

## Project structure
- `pg_game/`         — package source
  - `main.py`        — entry point
  - `run.py`         — convenience runner
  - `assets/`        — images, sounds
  - `config.py`      — game settings
  - `scenes/`        — game states/screens
  - `entities/`      — game objects, sprites
  - `utils/`         — helpers and utilities
- `tests/`           — unit and integration tests
- `requirements.txt`
- `LICENSE`          — add your chosen license (e.g., MIT)
- `README.md`        — this file

## Development
- Follow PEP 8 and typing where practical.
- Run tests:
```bash
pytest
```
- Linters/formatters suggested: `flake8`, `black`, `isort`.
- Use feature branches and descriptive PRs.

## Contributing
- Open issues for bugs or feature requests.
- Keep changes small and focused.
- Include tests and update docs for new behavior.

## License
Add a `LICENSE` file to specify the project's license (MIT recommended for templates).

If you want, I can also add example scenes, a basic CI workflow, or a `tox` configuration.