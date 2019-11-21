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
    # Initiate a relationship dict to store the posted data.
    relationship_count = len(request.form) // 3
    relationship = dict()
    # Initiate a payload dict to post data to `generate` function.
    payload = dict()
    payload['relationships'] = list()
    payload['objects'] = list()
    # Initiate a objects set to store all the objects.
    objects = set()

    for i in range(relationship_count):
        relationship[i + 1] = (
            request.form.get('obj1-' + str(i + 1)),
            request.form.get('rel-' + str(i + 1)),
            request.form.get('obj2-' + str(i + 1)),
        )
        objects.add(request.form.get('obj1-' + str(i + 1)))
        objects.add(request.form.get('obj2-' + str(i + 1)))

    objects = list(objects)
    payload['objects'] = objects

    for value in relationship.values():
        temp = list()
        temp.append(objects.index(value[0]))
        temp.append(value[1])
        temp.append(objects.index(value[2]))
        payload['relationships'].append(temp)

    return generate(scene_graph=payload)
