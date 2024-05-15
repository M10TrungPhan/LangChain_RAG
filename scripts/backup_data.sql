CREATE SCHEMA IF NOT EXISTS "256_20_chunk_bartpho_word";

create table "256_20_chunk_bartpho_word".document (like public.document including all);
insert into "256_20_chunk_bartpho_word".document  select * from public.document as p WHERE NOT EXISTS (SELECT 1 FROM "256_20_chunk_bartpho_word".document  WHERE id=p.id);

create table "256_20_chunk_bartpho_word".chat_session (like public.chat_session including all);
insert into "256_20_chunk_bartpho_word".chat_session  select * from public.chat_session  as p WHERE NOT EXISTS (SELECT id FROM "256_20_chunk_bartpho_word".chat_session  WHERE id=p.id);

create table "256_20_chunk_bartpho_word".node(like public.node including all);
insert into "256_20_chunk_bartpho_word".node  select * from public.node  as p WHERE NOT EXISTS (SELECT id FROM "256_20_chunk_bartpho_word".node  WHERE id=p.id);

create table "256_20_chunk_bartpho_word".organization (like public.organization including all);
insert into "256_20_chunk_bartpho_word".organization  select * from public.organization  as p WHERE NOT EXISTS (SELECT id FROM "256_20_chunk_bartpho_word".organization  WHERE id=p.id);;

create table "256_20_chunk_bartpho_word".project (like public.project including all);
insert into "256_20_chunk_bartpho_word".project  select * from public.project  as p WHERE NOT EXISTS (SELECT id FROM "256_20_chunk_bartpho_word".project  WHERE id=p.id);;

create table "256_20_chunk_bartpho_word".user (like public.user including all);
insert into "256_20_chunk_bartpho_word".user  select * from public.user as p WHERE NOT EXISTS (SELECT id FROM "256_20_chunk_bartpho_word".user  WHERE id=p.id); ;

