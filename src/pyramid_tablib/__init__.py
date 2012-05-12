from pyramid_tablib.renderer import (
        XLSXRendererFactory,
        XLSRendererFactory,
        CSVRendererFactory,
        )


def includeme(config):
    config.add_renderer('xlsx', XLSXRendererFactory)
    config.add_renderer('xls', XLSRendererFactory)
    config.add_renderer('csv', CSVRendererFactory)
