SELECT * FROM match_node_cosine_2(
    '[]'::vector(1024),
    0.2::double precision,
    3);

select
node.uuid,
node.text,
1 - (node.embeddings <=> '[]') as similarity
from node
-- where 1 - (node.embeddings <=> '[]') > 0.5
order by similarity desc
limit 10;

SELECT document_id, text ,  token_count, embeddings <=> '[]'
	AS distance 
	FROM node
	ORDER BY distance asc;



-- create or replace function  {strategy_name} (
--     query_embeddings vector({int(VECTOR_EMBEDDINGS_DIM)}),
--     match_threshold float,
--     match_count int
-- ) returns table (
--     uuid uuid,
--     text varchar,
--     similarity float
-- )
-- language plpgsql
-- as $$
-- begin
--     return query
--     select
--         node.uuid,
--         node.text,
--         1 - (node.embeddings {strategy_distance_str} query_embeddings) as similarity
--     from node
--         where 1 - (node.embeddings {strategy_distance_str} query_embeddings) > match_threshold
--         order by similarity desc
--         limit match_count;
-- end;
-- $$;