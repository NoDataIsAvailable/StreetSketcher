# StreetSketcher

This is a simple tool to create a Road only top down view of a city.
It uses OpenStreetMap Data to generate these Images



### Disclaimer

This is a very basic and slow prototype. Don't expect too much.


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
python cli.py -p 50667 -o Collogne.png -r 4000
```




![Collogne](Collogne.png "Title")