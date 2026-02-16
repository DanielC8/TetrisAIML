# Tetris AI with Genetic Algorithms

This project implements an automated Tetris player using multiple AI algorithms. A genetic algorithm evolves a population of agents over generations to learn optimal piece placement strategies. The best trained model cleared approximately 14,000 lines.

## Features
- Four AI algorithms for playing Tetris: Genetic Algorithm, Greedy Heuristic, Monte Carlo Tree Search, and Random Baseline.
- Genetic algorithm training pipeline with population-based evolution, crossover, and mutation.
- 9-feature board evaluation function covering aggregate height, holes, bumpiness, pits, wells, transitions, and row clears.
- Parallelized training using Python multiprocessing (30 workers).
- Manual play mode with keyboard controls.
- Visual rendering with pygame or headless mode for fast training.

## Project Structure
```
tetris_a/
├── src/
│   ├── main.py                # Entry point — selects play mode and loads models
│   ├── game.py                # Game loop, rendering, and event handling
│   ├── board.py               # Board state, piece placement, and row clearing
│   ├── piece.py               # Tetris piece definitions and rotation logic
│   ├── greedy.py              # Greedy heuristic AI (weighted cost function)
│   ├── genetic2.py            # Genetic algorithm agent (9-gene weight vector)
│   ├── genetic_helpers.py     # Board feature extraction (peaks, holes, bumpiness, etc.)
│   ├── genetic_controller.py  # Alternative genetic algorithm implementation
│   ├── mcts.py                # Monte Carlo Tree Search AI
│   ├── randomChoice.py        # Random baseline algorithm
│   ├── custom_model.py        # Template for implementing custom models
│   └── run_experiments.py     # Training script for genetic algorithm
├── genes/                     # Saved trained models (joblib format)
│   ├── test1/                 # Generation snapshots from training run 1
│   ├── test1f.joblib          # Final model from training run 1
│   └── test2f.joblib          # Final model from training run 2
├── AI_Final_Project_Report.pdf
├── TETRIS_present.ipynb
└── requirements.txt
```

## How It Works

1. **Game Environment**: Standard 10x20 Tetris board with 7 piece types. Pieces spawn at the top, and the AI selects a rotation (0-3) and x-position (0-9) for each piece, giving 40 possible placements per move.

2. **Genetic Algorithm Training**:
   - A population of 100 agents is initialized with random 9-dimensional weight vectors.
   - Each agent plays Tetris and is scored by lines cleared.
   - The top 35% survive as parents; the remaining 65% are replaced by offspring produced via crossover and Gaussian mutation.
   - This repeats for 100 generations. The best agent from each generation is saved.

3. **Board Evaluation**: Each agent scores a board state using a weighted sum of 9 features:
   - Aggregate height, number of holes, bumpiness, number of pits, max well depth, columns with holes, row transitions, column transitions, and rows cleared.

4. **Other Algorithms**:
   - **Greedy**: Evaluates all 40 placements using a hand-tuned cost function and picks the best.
   - **MCTS**: Builds a search tree with UCB1 selection and uses the greedy heuristic for rollout evaluation.
   - **Random**: Selects random rotations and positions as a baseline.

## Setup
1. Clone this repository.
2. Install dependencies:
   ```bash
   cd tetris_a
   pip install -r requirements.txt
   ```

## Usage

**Manual play:**
```bash
python src/main.py player
```
Controls: `A` (left), `D` (right), `W` (rotate), `S` (drop).

**Genetic Algorithm AI** (loads pre-trained model):
```bash
python src/main.py genetic
```

**Greedy AI:**
```bash
python src/main.py greedy
```

**Monte Carlo Tree Search AI:**
```bash
python src/main.py mcts
```

**Random Baseline:**
```bash
python src/main.py random
```

**Train a new genetic algorithm model:**
```bash
python src/run_experiments.py
```

## Training Parameters
| Parameter | Value |
|-----------|-------|
| Population size | 100 |
| Generations | 100 |
| Survival rate | 35% |
| Elite count | 5 |
| Mutation std dev | 0.2 |
| Gene dimensions | 9 |
| Parallel workers | 30 |

## Limitations
- MCTS uses only 1 simulation iteration, limiting its search depth.
- Greedy heuristic weights are manually tuned, not learned.
- Piece generation is uniform random rather than the standard Tetris "bag" system.
- An initial reinforcement learning approach was abandoned after it stopped improving beyond 30 pieces.

## Requirements
- Python 3.x
- numpy
- pygame
- joblib
- pandas

Install all dependencies:
```bash
pip install -r requirements.txt
```

## Credits
Based on https://github.com/danielchang2002/tetris_ai
