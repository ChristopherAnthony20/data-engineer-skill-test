SELECT a.user_id, a.name,a.age, a.city, sum(b.amount) spending_total FROM USERs a
LEFT JOIN orders b
ON a.user_id = b.user_id
GROUP BY a.user_id, a.name,a.age, a.city