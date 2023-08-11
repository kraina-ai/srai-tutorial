# SRAI Tutorial

Introduction to Geospatial Machine Learning with SRAI

## Description

This tutorial offers a thorough introduction to the srai library for Geospatial Artificial Intelligence. Participants will learn how to use this library for geospatial tasks like downloading and processing OpenStreetMap data, extracting features from GTFS data, dividing an area into smaller regions, and representing regions in a vector space using various spatial features. Additionally, participants will learn to pre-train and fine-tune models for downstream tasks.

In this tutorial, we intend to provide a comprehensive introduction to the Spatial Representations for Artificial Intelligence (srai) library. Participants will learn how to utilize this library for various geospatial applications, such as downloading and processing OpenStreetMap data, extracting features from GTFS data, splitting a given area into smaller regions, and embedding regions into a vector space based on different spatial features. Moreover, users will learn how to pre-train a model of their choice and fine-tune existing pre-trained models for use in downstream tasks.

By the end of the tutorial, attendees will be able to:

1. Install and set up the SRAI library.
2. Use SRAI to download and process geospatial data.
3. Apply various regionalization and embedding techniques to geospatial data.
4. Utilize pre-trained embedding models for clustering and similarity search.
5. Pre-train available models from scratch.
6. Understand the potential applications and future enhancements of the SRAI library.

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

After that, the notebooks can be run. You can start with the [introductory one](00_primer.ipynb).

## Slideshow

It is possible also to run the jupyter notebooks as a slideshow:

1. `> jupyter notebook`
2. `Edit/Exit RISE Slideshow (or alt+r)` in the opened notebook

## Used in

- https://pretalx.com/euroscipy-2023/talk/X8LYJY/