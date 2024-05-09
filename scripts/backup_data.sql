CREATE SCHEMA IF NOT EXISTS "1024_100_chunk_gpt";

create table "1024_100_chunk_gpt".document (like public.document including all);
insert into "1024_100_chunk_gpt".document  select * from public.document as p WHERE NOT EXISTS (SELECT 1 FROM "1024_100_chunk_gpt".document  WHERE id=p.id);

create table "1024_100_chunk_gpt".chat_session (like public.chat_session including all);
insert into "1024_100_chunk_gpt".chat_session  select * from public.chat_session  as p WHERE NOT EXISTS (SELECT id FROM "1024_100_chunk_gpt".chat_session  WHERE id=p.id);

create table "1024_100_chunk_gpt".node(like public.node including all);
insert into "1024_100_chunk_gpt".node  select * from public.node  as p WHERE NOT EXISTS (SELECT id FROM "1024_100_chunk_gpt".node  WHERE id=p.id);

create table "1024_100_chunk_gpt".organization (like public.organization including all);
insert into "1024_100_chunk_gpt".organization  select * from public.organization  as p WHERE NOT EXISTS (SELECT id FROM "1024_100_chunk_gpt".organization  WHERE id=p.id);;

create table "1024_100_chunk_gpt".project (like public.project including all);
insert into "1024_100_chunk_gpt".project  select * from public.project  as p WHERE NOT EXISTS (SELECT id FROM "1024_100_chunk_gpt".project  WHERE id=p.id);;

create table "1024_100_chunk_gpt".user (like public.user including all);
insert into "1024_100_chunk_gpt".user  select * from public.user as p WHERE NOT EXISTS (SELECT id FROM "1024_100_chunk_gpt".user  WHERE id=p.id); ;

