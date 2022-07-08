drop table if exists drop_table;

create table drop_table(
    id integer primary key autoincrement,
    created timestamp not null default current_timestamp,
    path text not null,
    data text not null
);