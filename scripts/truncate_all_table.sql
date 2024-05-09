truncate  table  public.document cascade;
truncate  table  public.node cascade;
truncate  table  public.organization cascade;
truncate  table  public.project cascade;
truncate  table  public.user cascade;
truncate  table  public.chat_session cascade;

drop  table  public.document cascade;
drop  table  public.node cascade;
drop  table  public.organization cascade;
drop  table  public.project cascade;
drop  table  public.user cascade;
drop  table  public.chat_session cascade;


-- delete  from public.document where id not in (select distinct(document_id) from node);