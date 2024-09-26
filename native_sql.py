


create_tables = """
    create table if not exists Countries (
    country_id serial primary key,
    country_name varchar(100) unique not null
);

create table if not exists Cities (
    city_id serial primary key,
    city_name varchar(100) unique not null,
    country_id int not null,
    latitude decimal,
    longitude decimal,
    foreign key (country_id) references Countries(country_id)
);

create table if not exists TargetTypes (
    target_type_id serial primary key,
    target_type_name varchar(255) unique not null
);


create table if not exists Targets (
    target_id serial primary key,
    target_industry varchar(255) not null,
    city_id int not null,
    target_type_id int,
	target_priority int,
    foreign key (city_id) references Cities(city_id),
    foreign key (target_type_id) references TargetTypes (target_type_id)
);
"""