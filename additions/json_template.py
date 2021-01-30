"""
    Сам шаблон формирования json
"""

template = {
    'data': [
        {   # Информация, врямя запуска,
            # можно добавить для видимости прогресса название ОС через os.name или же os.uname
            'info':
                [
                    {}
                ]
        },
        {   # Входные параметры, все, что вводится юзером, находится тут
            'entered_params':
                [
                    {}
                ]
        },
        {
            # Результат работы, пока что тут только время работы, остальное на твое усмотрение
            'result':
                [
                    {}
                ]
        }
    ]
}


# Функция заполнения шаблона, чтобы не хранить там лишнюю инфу
def fill_template(now, leap_time):
    template['data'][0]['info'][0]['start_time'] = now[1:]
    template['data'][2]['result'][0]['lead_time'] = f'{round(leap_time, 4)}s'
    return template