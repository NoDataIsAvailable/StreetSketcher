# City-Wireframe-Generator
This tool is used to create a Road only top down view of a city

## Installation

### Windows

```
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
```


### Linux

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```


## How to use it


> You can also use --help to get more info



### Basic
```
python cli.py -n TheNameOfYourCity
```

#### Example
```
python cli.py -n Wuppertal
```

### Advanced
```
python cli.py -n TheNameOfYourCity -o Outputfilename.Format -r Resolution 
```

#### Postalcodes
```
python cli.py -p YourPostalCode -o Outputfilename.Format -r Resolution 
```

#### Example
```
python cli.py -p 10 -o Berlin.png -r 4000
```


