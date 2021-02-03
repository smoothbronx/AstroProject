template = {'data': {'info': {}, 'result': {}}}


def fill_template(now, leap_time, inputs):
    template['data']['info']['start_time'] = now[1:]
    template['data']['result']['lead_time'] = f'{round(leap_time, 4)}s'
    template['data']['entered_params'] = inputs
    return template
