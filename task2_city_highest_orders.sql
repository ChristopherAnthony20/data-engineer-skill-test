
-- dalam hal jumlah uang yang didapat
SELECT a.city, sum(b.amount) Amount_by_city FROM USERs a
LEFT JOIN orders b
ON a.user_id = b.user_id
GROUP BY  a.city
ORDER BY sum(b.amount) DESC

-- dalam hal jumlah frekuensi
SELECT a.city, count(1) Amount_by_city FROM USERs a
LEFT JOIN orders b
ON a.user_id = b.user_id
GROUP BY  a.city
ORDER BY count(1) desc