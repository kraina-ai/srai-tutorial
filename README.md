[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/kraina-ai/srai-tutorial/HEAD)

# SRAI Tutorial

Introduction to Geospatial Machine Learning with SRAI

## Description

This tutorial offers a thorough introduction to the srai library for Geospatial Artificial Intelligence. Participants will learn how to use this library for geospatial tasks like downloading and processing OpenStreetMap data, extracting features from GTFS data, dividing an area into smaller regions, and representing regions in a vector space using various spatial features. Additionally, participants will learn to pre-train embedding models and train predictive models for downstream tasks.

In this tutorial, we intend to provide a comprehensive introduction to the Spatial Representations for Artificial Intelligence (srai) library. Participants will learn how to utilize this library for various geospatial applications, such as downloading and processing OpenStreetMap data, extracting features from GTFS data, splitting a given area into smaller regions, and embedding regions into a vector space based on different spatial features. Moreover, users will learn how to pre-train a model of their choice and build predictive models for use in downstream tasks.

By the end of the tutorial, attendees will be able to:

1. Install and set up the SRAI library.
2. Use SRAI to download and process geospatial data.
3. Apply various regionalization and embedding techniques to geospatial data.
4. Utilize pre-trained embedding models for clustering and similarity search.
5. Build predictive models on top of SRAI embeddings
6. Pre-train available models from scratch.
7. Understand the potential applications and future enhancements of the SRAI library.

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

After that, the notebooks can be run. You can start with the [introductory one](00_hello.ipynb).

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

## Used in

- [EuroSciPy 2023](https://pretalx.com/euroscipy-2023/talk/X8LYJY/) ([Recording](https://www.youtube.com/watch?v=JlyPh_AdQ8E), [Resource Material](https://github.com/kraina-ai/srai-tutorial/tree/EuroSciPy2023))
