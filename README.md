# movie-genres

## Prerequisites
- [Python](https://www.python.org/) (recommended version >= v3.10.2)
- [pipenv](https://pypi.org/project/pipenv/) (`pip install pipenv`)
- Configure Jupyter Notebook environment (recommended: [Visual Studio Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks))

## Usage

1. Clone this repository
2. Enter the virtual environment:
```
pipenv shell
```
4. Install all dependencies via the command line:
```
pipenv install
```
6. Execute blocks of code in your environment

## Notes

- Dataset - [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/)
- Preprocessed dataset - [Preprocessed dataset](https://drive.google.com/file/d/1U-CGGvlc3z3ayk2_qd-uOyUPiNkvsSjj/view?usp=sharing)
- You can skip the part 1 - preprocessing
- Read carefully block 3.1, before executing it
- We built 2 models: one for general genres and one for specific genres
- You can test both models in the part 5 - paste the plot of movie, execute the block and output will be `"General genre, Specific genre"`
- General genres: Animation, Monochrome, Short Film, Documentary, Family, Adventure, Action, Thriller, Drama
- Specific genres: Horror, Musical, Fantasy, War, Biography, Science Fiction, Crime, Romance, Mystery, Comedy
