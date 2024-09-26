from config.base import engine, session_factory
from config.base import Base
from sqlalchemy import text



def create_tables():
    create_table_countries()
    create_table_cities()
    create_table_target_types()
    create_table_targets()



def insert_into_all_tables():
    insert_table_countries()
    insert_table_cities()
    insert_table_targets_type()
    insert_table_targets()



def create_table_countries():
    with session_factory() as session:
        session.execute(text("""
create table if not exists Countries (
    country_id serial primary key,
    country_name varchar(100) unique not null
);
        """))

def create_table_cities():
    with session_factory() as session:
        session.execute(text("""
create table if not exists Cities (
    city_id serial primary key,
    city_name varchar(100) unique not null,
    country_id int not null,
    latitude decimal,
    longitude decimal,
    foreign key (country_id) references Countries(country_id)
);
        """))


def create_table_target_types():
    with session_factory() as session:
        session.execute(text("""
create table if not exists TargetTypes (
    target_type_id serial primary key,
    target_type_name varchar(255) unique not null
);
        """))

def create_table_targets():
    with session_factory() as session:
        session.execute(text("""
create table if not exists Targets (
    target_id serial primary key,
    target_industry varchar(255) not null,
    city_id int not null,
    target_type_id int,
    target_priority int,
    foreign key (city_id) references Cities(city_id),
    foreign key (target_type_id) references TargetTypes (target_type_id)
);
        """))

def insert_table_targets():
    with session_factory() as session:
        session.execute(text("""
insert into Targets (target_industry, target_priority, city_id, target_type_id)
select distinct
    m.target_industry,
    m.target_priority::integer,
    ci.city_id,
    tt.target_type_id
from mission m
inner join Cities ci on m.target_city = ci.city_name
inner join TargetTypes tt on m.target_type = tt.target_type_name
where m.target_id is not NULL and m.target_industry is not null
on conflict (target_id) do nothing;
        """))

def insert_table_targets_type():
    with session_factory() as session:
        session.execute(text("""
insert into TargetTypes (target_type_name)
select distinct target_type
from mission
where target_type is not null
on conflict (target_type_name) do nothing;
        """))

def insert_table_cities():
    with session_factory() as session:
        session.execute(text("""
insert into Cities (city_name, country_id, latitude, longitude)
select distinct
    m.target_city,
    c.country_id,
    m.target_latitude::decimal,
    m.target_longitude::decimal
from mission m
join Countries c on m.country = c.country_name
where m.target_city is not null
on conflict (city_name) do nothing;
        """))

def insert_table_countries():
    with session_factory() as session:
        session.execute(text("""
insert into Countries (country_name)
select distinct target_country
FROM mission
where target_country is not NULL
on conflict (country_name) do nothing;
        """))

insert_into_all_tables()