# Use an official Python runtime as a parent image
FROM continuumio/miniconda3:latest

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN conda update -n base -c defaults conda
RUN conda install -c conda-forge --file cf_requirements.txt
RUN conda install -c anaconda --file an_requirements.txt
RUN pip install --trusted-host pypi.python.org -r pip_requirements.txt

RUN rm cf_requirements.txt an_requirements.txt pip_requirements.txt