from flask import abort
from ..extensions import argumentBuilder
from sg2im_pytorch.run_model import main
import os
import random


def generate(scene_graph):
    args = argumentBuilder()
    args.scene_graphs_json = scene_graph
    args.id = str(int(random.random() * 1000000))
    model_build = main(args)
    if model_build:
        response = '<img src="' + '/static/outputs/' + os.path.split(model_build)[1] + '" >'
        return response
    else:
        return abort(404)
