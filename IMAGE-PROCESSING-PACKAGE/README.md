# image_processing
Description. The package image_processing is used to:
    Processing:
    - Histogram matching
    - Structural similarity
    - Resize image
    Utils:
    - Read image
    - Save image
    - Plot image
    - Plot result
    - Plot histogram

## Installation
Use the package manager pip to install image_processing

``` pip install image_processing```

## Usage

``` from image_processing.processing import combination.py```

## Comandos de instalação antes de instalar o package
 ```bash 
 python -m pip install --upgrade pip 
 python -m pip install --user twine 
 python -m pip install --user setuptools 

 ```
 Inside the folder image_processing:
 ```bash 
 python3 setup.py sdist bdist_wheel
 ```
 To revert use:
 ```bash 
 rm -rf dist build *.egg-info
```