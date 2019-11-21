from . import api
from flask import request, send_file, abort, jsonify
from ..extensions import argumentBuilder
from sg2im_pytorch.run_model import main


@api.route('/generate', methods=['POST'])
def generate():
    if request.method == 'POST':
        scene_graph = request.json
        args = argumentBuilder()
        args.scene_graphs_json = scene_graph
        model_build = main(args)
        if model_build:
            return send_file(model_build, mimetype='image/gif')
        else:
            abort(404)
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return jsonify(success=True), 201


@api.route('/parser', methods=['POST'])
def get_image():
    print(request.form)
    return 'Hello!'
