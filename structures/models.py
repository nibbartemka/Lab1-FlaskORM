from typing import TypeAlias, Any, List, Tuple
from sqlalchemy import func, and_

from config import db
from models import Country, City, Building, TypeBuilding


QueryKeys: TypeAlias = List[str]
QueryRecords: TypeAlias = List[Any]


def get_all_buildings() -> Tuple[QueryKeys, QueryRecords]:
    query = (
        db.session.query(
            Building.title.label("Здание"),
            TypeBuilding.name.label("Тип"),
            Country.name.label("Страна"),
            City.name.label("Город"),
            Building.year.label("Год"),
            Building.height.label("Высота")
        )
        .select_from(Building)
        .join(TypeBuilding)
        .join(City)
        .join(Country)
    )

    return query.statement.columns.keys(), query.all()


def get_stats_by_type_building() -> Tuple[QueryKeys, QueryRecords]:
    query = (
        db.session.query(
            TypeBuilding.name.label("Тип"),
            func.max(Building.height).label("Максимальная высота"),
            func.min(Building.height).label("Минимальная высота"),
            func.round(func.avg(Building.height), 1).label("Средняя высота"),
        )
        .join(Building)
        .group_by(TypeBuilding.name)
    )

    return query.statement.columns.keys(), query.all()


def get_stats_by_country() -> Tuple[QueryKeys, QueryRecords]:
    query = (
        db.session.query(
            Country.name.label("Страна"),
            func.max(Building.height).label("Максимальная высота"),
            func.min(Building.height).label("Минимальная высота"),
            func.round(func.avg(Building.height), 1).label("Средняя высота"),
        )
        .select_from(Building)
        .join(City)
        .join(Country)
        .group_by(Country.name)
    )

    return query.statement.columns.keys(), query.all()


def get_stats_by_year() -> Tuple[QueryKeys, QueryRecords]:
    query = (
        db.session.query(
            Building.year.label("Год"),
            func.max(Building.height).label("Максимальная высота"),
            func.min(Building.height).label("Минимальная высота"),
            func.round(func.avg(Building.height), 1).label("Средняя высота"),
        )
        .group_by(Building.year)
    )

    return query.statement.columns.keys(), query.all()


def get_buildings_by_period(year_begin: int,
                            year_end: int) -> Tuple[QueryKeys, QueryRecords]:
    query = (
        db.session.query(
            Building.title.label("Здание"),
            Building.year.label("Год"),
            Building.height.label("Высота")
        )
        .filter(
            and_(
                Building.year >= year_begin,
                Building.year <= year_end,
            )
        )
    )

    return query.statement.columns.keys(), query.all()
