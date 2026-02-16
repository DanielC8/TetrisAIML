# Tetris AI with Genetic Algorithms

This project implements an automated Tetris player using a genetic algorithm. A population of agents evolves over generations to learn optimal piece placement strategies. The best trained model cleared approximately 14,000 lines.

## Features
- Genetic algorithm training pipeline with population-based evolution, crossover, and mutation.
- 9-feature board evaluation function covering aggregate height, holes, bumpiness, pits, wells, transitions, and row clears.
- Parallelized training using Python multiprocessing (30 workers).
- Visual rendering with pygame or headless mode for fast training.
- Pre-trained models included.

## Project Structure
```
tetris_a/
├── src/
│   ├── main.py                # Entry point — selects play mode and loads models
│   ├── game.py                # Game loop, rendering, and event handling
│   ├── board.py               # Board state, piece placement, and row clearing
│   ├── piece.py               # Tetris piece definitions and rotation logic
│   ├── genetic2.py            # Genetic algorithm agent (9-gene weight vector)
│   ├── genetic_helpers.py     # Board feature extraction (peaks, holes, bumpiness, etc.)
│   ├── run_experiments.py     # Training script for genetic algorithm
│   └── ...
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

4. **Inference**: The trained model evaluates all 40 possible placements for each piece and selects the one with the highest weighted score.

## Setup
1. Clone this repository.
2. Install dependencies:
   ```bash
   cd tetris_a
   pip install -r requirements.txt
   ```

## Usage

**Run the trained genetic algorithm AI:**
```bash
python src/main.py genetic
```

**Train a new model:**
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
- Piece generation is uniform random rather than the standard Tetris "bag" system.
- An initial reinforcement learning approach was abandoned after it stopped improving beyond 30 pieces.
- Only evaluates single-move outcomes with no lookahead for future pieces.

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
