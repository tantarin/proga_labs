PARAMS = {
        'precision': None,
        'output_type': None,
        'possible_types': None,
        'dest': None
}


def load_params(path="lab_5/params.ini"):
    config = configparser.ConfigParser()
    config.read(path)
    global PARAMS
    PARAMS['precision'] = config.get("Settings", "precision")
    PARAMS['output_type'] = config.get("Settings", "output_type")
    PARAMS['possible_types'] = config.get("Settings", "possible_types")
    PARAMS['dest'] = config.get("Settings", "dest")
    print(PARAMS)
