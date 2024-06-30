import dash_tabulator

data = [{'name': 'Затраты на ГСМ', 'children': [{'name': 'Оплата прочих коммерческих затрат', 'children': ""},
                                                {'name': 'Оплата прочих коммерческих затрат', 'children': ""}]},
        {"name": "Затраты на КЦ", "children": [{'name': 'Оплата прочих коммерческих затрат', 'children': ""},
                                               {'name': 'Оплата прочих коммерческих затрат', 'children': ""}]},
        {"name": "Коммерческие расходы", "children": [{'name': 'Оплата прочих коммерческих затрат', 'children': ""},
                                                      {'name': 'Оплата прочих коммерческих затрат', 'children': ""}]},
        {"name": "Управленческие расходы", "children": [{'name': 'Затраты на маркетинговые материалы', 'children': ""},
                                                        {'name': 'Затраты на маркетинговые материалы', 'children': ""}]}]


def tabulator():
    return dash_tabulator.DashTabulator(
        theme="tabulator_midnight",
        id='table',
        columns=[
            {'title': 'Наименование', 'field': 'name'},
        ],
        data=data,
        options={
            "dataTree": True,
            "dataTreeChildField": "children"
        }
    )
