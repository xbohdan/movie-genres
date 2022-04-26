# movie-genres

## Prerequisites
- [Python](https://www.python.org/) (recommended version >= v3.10.2)
- [pipenv](https://pypi.org/project/pipenv/) (`pip install pipenv`)

## Usage

1. Clone this repository
2. Install all dependencies via the command line:
> pipenv install
3. Enter the virtual environment:
> pipenv shell
4. To execute `data_preprocessing.py` script, you need to download the dataset [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/), then unpack `movie.metadata.tsv` and `plot_summaries.txt` files to the root folder of this project. Then, run the script via the command line:
> python data_preprocessing.py
  
5. To execute `feature_extraction.py` script, you need to perform the step 3, or download the [preprocessed dataset](https://drive.google.com/drive/folders/12H30LY4YFlnDAL3fwjG4nYeNCAmWNeZR?usp=sharing). Put the `preprocessed_dataset.csv` into the root folder. Then, run the script via the command line:
> python feature_extraction.py
