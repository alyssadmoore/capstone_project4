drop table if exists locations;
create table locations (
  id integer primary key autoincrement,
  street text not null,
  city text not null,
  state text not null,
  zipcode text not null
);
