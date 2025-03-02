from flask import render_template

from .models import (get_all_buildings,
                     get_stats_by_type_building,
                     get_stats_by_year,
                     get_stats_by_country,
                     get_buildings_by_period)
from app import app


@app.route('/')
def index():
    buildings_head, buildings_body = get_all_buildings()
    type_buildings_head, type_buildings_body = get_stats_by_type_building()
    countries_head, countries_body = get_stats_by_country()
    years_head, years_body = get_stats_by_year()
    buildings_by_period_head, buildings_by_period_body = get_buildings_by_period(2000, 2018)

    html = render_template(
        'index.html',
        buildings_head=buildings_head,
        buildings_body=buildings_body,
        type_buildings_head=type_buildings_head,
        type_buildings_body=type_buildings_body,
        countries_head=countries_head,
        countries_body=countries_body,
        years_head=years_head,
        years_body=years_body,
        buildings_by_period_head=buildings_by_period_head,
        buildings_by_period_body=buildings_by_period_body,
    )

    return html
