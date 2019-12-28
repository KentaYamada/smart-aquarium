create table aquarium_water_quarities (
    id integer primary key autoincrement,
    measured_at text not null,
    ph real not null,
    temperature real not null,
    unique(measured_at)
);

create table notifications (
    id integer primary key autoincrement,
    created_at text not null,
    message text not null
);

create table configurations (
    id integer primary key,
    ph_lower_limit real not null,
    ph_upper_limit real not null,
    temperature_lower_limit real not null,
    temperature_upper_limit real not null,
    measurement_trials integer not null
);
