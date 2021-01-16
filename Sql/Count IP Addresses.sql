SELECT id,((CAST (split_part(last, '.', 1)AS BIGINT)-CAST (split_part(first, '.', 1)AS BIGINT))*256*256*256)+
((CAST (split_part(last, '.', 2)AS BIGINT)-CAST (split_part(first, '.', 2)AS BIGINT))*256*256)+
((CAST (split_part(last, '.', 3)AS BIGINT)-CAST (split_part(first, '.', 3)AS BIGINT))*256)+
(CAST (split_part(last, '.', 4)AS BIGINT)-CAST (split_part(first, '.', 4)AS BIGINT)) as ips_between
FROM ip_addresses;