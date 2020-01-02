import get_farmlands
from rtree import index


def get_nearest_point(latitude, longitude):
    data = get_farmlands.get_data(latitude, longitude)

    idx = index.Index()
    for d in data:
        idx.insert(d['id'], d['center'])

    id_new = list(idx.nearest([52.20472, 0.14056], 1))

    return [i['center'] for i in data if i['id'] in id_new][0]


print(get_nearest_point(52.20472, 0.14056))
