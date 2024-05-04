import click
from generate import generate_img

@click.command()
@click.option('--name','-n',default=None, help='The name of the City')
@click.option('--postal-code','-p',default=None, help='Postalcode (Note this will overwrite the name argument)')
@click.option('--output-path','-o',default='out.svg', help='Path of the output file')
@click.option('--resolution','-r',default=8000, help='Resolution of the image, this will be the same for height and widht to minize distortion')
def generate(name, postal_code, output_path, resolution):
    if not name and not postal_code:
        raise ValueError("no name or postal-code was given")
    
    generate_img(name,postal_code, output_path ,resolution)
    
    
    
if __name__ == '__main__':
    generate()