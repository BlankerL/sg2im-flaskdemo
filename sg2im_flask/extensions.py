from flask_cors import CORS
import os

cors = CORS()


class argumentBuilder:
    checkpoint = os.path.join(
        os.path.split(os.path.realpath(__file__))[0], os.path.pardir,
        'sg2im_pytorch', 'sg2im-models', 'vg128.pt'
    )
    id = ''
    scene_graphs_json = ''
    output_dir = os.path.join(
        os.path.split(os.path.realpath(__file__))[0], os.path.pardir,
        'outputs'
    )
    draw_scene_graphs = 0
    device = 'cpu'
