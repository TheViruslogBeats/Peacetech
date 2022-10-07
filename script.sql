create table employee
    (
        login varchar,
        password varchar,
        name varchar,
        surname varchar,
        lastname varchar,
        department varchar,
        role varchar,
        wallet varchar,
        primary key (login)
    );

create table garden
    (
        garden_id serial,
        employee_login varchar,
        primary key (garden_id),
        foreign key (employee_login) references employee

    );

create table plant
    (
        id serial,
        garden_id int,
        type varchar,
        color varchar,
        progress float,
        primary key (id),
        foreign key (garden_id) references garden

    );

create table task
    (
        id serial,
        description varchar,
        employee_login varchar,
        award float,
        administrator_login varchar,
        status varchar,
        primary key (id),
        foreign key (employee_login) references employee
    );

create table all_achievements
    (
        id serial,
        description varchar,
        achieve_points float,
        primary key (id)
    );

create table employee_achievements
    (
        id serial,
        employee_login varchar,
        achieve_id int,
        primary key (id),
        foreign key (employee_login) references employee,
        foreign key (achieve_id) references all_achievements
    );

create table shop
    (
        goods_id serial,
        description varchar,
        price float,
        primary key (goods_id)
    );

create table greenhouse
    (
        task_id serial,
        description varchar,
        price float,
        award float,
        authors_login varchar,
        primary key (task_id),
        foreign key (authors_login) references employee
    );