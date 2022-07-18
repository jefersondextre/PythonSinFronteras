create database prueba;
use prueba;

-- drop database prueba
-- Crear una tabla
create table Usuario(
	id int,
    email varchar(255),
    username varchar(50)    
    );
-- Alterar agregando una tabla Usuario
alter table Usuario add edad int;

-- Eliminar una columna de la tabla Usuario
alter table Usuario drop column edad;
-- Modificando el tipo de dato de una columna
alter table Usuario modify column email varchar(50);

-- Insertar Registros
insert into Usuario(email, username) values('jeferson@gmail.com','jadex');
insert into Usuario(email, username) values('antonio dextre@yahoo.com','antonio');
insert into Usuario(email, username) values('Rotomartillo_electric@gmail.com','Rotomartillo');
insert into Usuario(email,username)values('jadex@yahoo.es','asdfasd#414');
insert into Usuario(email,username) values('admin','pohoit54#');

-- Eliminando el primer registro insertado
delete from Usuario where email='jeferson@gmail.com' limit 1;
delete from Usuario where email='antonio dextre@yahoo.com' limit 1;


-- estableciendo pk la columna id y añadiendole como autoincremental
alter table Usuario add primary key (id);
alter table Usuario modify column id  int Auto_increment;

select * from Usuario;

select * from Usuario where email = 'jeferson@gmail.com';

select * from Usuario where email='Rotomartillo_electric@gmail.com';
select * from Usuario where edad >=25;

update Usuario set edad = '55' where id=8;

# Eliminar Registros
delete from Usuario where id=7;