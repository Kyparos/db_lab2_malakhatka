create table athletes
(
    ath_id        serial
        constraint athletes_pk
            primary key,
    ath_name      char(50),
    noc_id        int,
    discipline_id int
);

create unique index athletes_ath_id_uindex
    on athletes (ath_id);

create table disipline
(
    dist_id   serial
        constraint disipline_pk
            primary key,
    dist_name char(50)
);
create table noc
(
    noc_id   serial
        constraint noc_pk
            primary key,
    noc_name char(50),
    g_medal  int,
    s_medal  int,
    b_medal  int
);

create unique index noc_noc_id_uindex
    on noc (noc_id);

alter table athletes
    add constraint noc_id
        foreign key (noc_id) references noc
            on update cascade on delete set null;

alter table athletes
    add constraint discipline_id
        foreign key (discipline_id) references disipline
            on update cascade on delete set null;