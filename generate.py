import urllib.parse
import requests
import plotly.graph_objs as go
import urllib







def generate_img(name, postal_code, path, resolution):
    query = None
    if postal_code:
       query = create_query(postal_code, postal_code = True)
    else:
       query = create_query(name, postal_code = False)

    if not query:
        raise ValueError("Query is None pls check your input")

    street_data = get_data(query)
    
    if not street_data:
        raise ValueError("Could not get any data from api")
    
    positions, edges = convert_data(street_data)
    
    if not positions or not edges:
        raise ValueError("Could not generate any edges or positions")
    
    fig = generate_figure(positions=positions,edges=edges)
    
    if not fig:
        raise ValueError("fig is none pls check the code")
    
    fig.write_image(path,width=resolution,height=resolution,validate=False)
    
    
def create_query(location, postal_code = False):
    if not location:
        raise ValueError("Location can not be None")
    
    # construct area query
    area = None
    
    if postal_code:
        area = f'area[postal_code="{location}"]'
    else:
        area = f'area[name="{location}"]'

    if not area:
        raise ValueError("No area specified")
    

    # create final query    
    query =f"""[out:json][timeout:25];
        {area}->.searchArea;
        (
        way["highway"="primary"](area.searchArea);
        way["highway"="secondary"](area.searchArea);
        way["highway"="residential"](area.searchArea);
        way["highway"="tertiary"](area.searchArea);
        way["highway"="pedestrian"](area.searchArea);
        way["highway"="path"](area.searchArea);
        );
        out geom;"""
        
    return query

def get_data(query):
    
    headers = {
    'Cache-Control': 'no-cache',
    }
    
    response = requests.post('https://overpass-api.de/api/interpreter', headers=headers, data=f'data={urllib.parse.quote(query)}')

    street_data = response.json()
    return street_data


def convert_data(street_data):
    
    positions = {}
    edges = []
    
    for street in street_data['elements']:
        last_node = None
        for geometry in street['geometry']:
            print (geometry)
            x = int(geometry['lon']  * 100000)
            y = int(geometry['lat']  * 100000)
            node_name = f"{x}-{y}"
            positions[node_name] = {'x':x,'y':y}
            if last_node:
                edges.append([last_node, node_name])
            last_node = node_name
            
    return positions, edges


def generate_figure(positions, edges):
    edge_x = []
    edge_y = []
    for edge in edges:
        x0 = positions[edge[0]]['x']
        y0 = positions[edge[0]]['y']
        x1 = positions[edge[1]]['x']
        y1 = positions[edge[1]]['y']
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=2, color='#888'),
        hoverinfo='none',
        mode='lines')
    
    layout = go.Layout( plot_bgcolor='rgba(0,0,0,0)',
                       paper_bgcolor='rgba(0,0,0,0)',
                       height=8000,
                       width=8000,
                       showlegend=False,
                       xaxis=dict(showgrid=False,visible=False)
                       ,yaxis=dict(showgrid=False,visible=False,))
    
    fig = go.Figure(data=[edge_trace], layout=layout)
    return fig

