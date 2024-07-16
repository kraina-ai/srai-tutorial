
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/kraina-ai/srai-tutorial/HEAD) [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kraina-ai/srai-tutorial/blob/main)

# SRAI Tutorial

Introduction to Geospatial Machine Learning with SRAI

## Description

Tutorial offers a thorough introduction to the geospatial domain with Python libraries. Participants will learn how to use, analyse and visualize open-source geospatial data. Additionally, participants will learn to pre-train embedding models and train predictive models for downstream tasks.

Most of the tutorial will be showing capabilities of the library srai (Spatial Representation for Artificial Intelligence), as well as GeoPandas, Shapely, osmnx and scikit-learn.

Beginner knowledge of Python is expected from the participants. Tutorial materials is provided in the form of Jupyter notebooks.

## Setup

Initialize Python virtual environment (optional but recommended):

```sh
python -m venv venv
source venv/bin/activate
```

And then install the dependencies:

```sh
pip install -r requirements.txt
```

After that, the notebooks can be run. They are available in the [tutorial](tutorial) directory. You can start with the [introductory one](tutorial/MLinPL/00_hello.ipynb).

Solutions to the assignments are available in the [answers](answers) directory

## Slideshow

It is possible also to run the jupyter notebooks as a slideshow:

1. `> jupyter notebook`
2. `Edit/Exit RISE Slideshow (or alt+r)` in the opened notebook

## Export to pdf

Use [decktape](https://rise.readthedocs.io/en/stable/exportpdf.html#using-decktape). An exemplary command:

```sh
./node_modules/.bin/decktape rise -s 1920x1080 http://localhost:8888/notebooks/02_srai.ipynb?token=<copy-token> ./export/02_srai.pdf
```

## Exported Slideshow

Visit [export](./export) folder for the rendered slides.

## Generate tutorial

The following command will generate files in the `tutorial` folder.

```sh
nbgrader generate_assignment MLinPL -f
```

## Used in

- [EuroSciPy 2023](https://pretalx.com/euroscipy-2023/talk/X8LYJY/) ([Recording](https://www.youtube.com/watch?v=JlyPh_AdQ8E), [Resource Material](https://github.com/kraina-ai/srai-tutorial/tree/EuroSciPy2023))
- [MLinPL 2023](https://conference2023.mlinpl.org/program#tutorial-3) ([Resource Material](https://github.com/kraina-ai/srai-tutorial/tree/MLinPL2023-fix-1))
