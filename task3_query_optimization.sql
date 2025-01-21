--indek
CREATE INDEX idx_users_user_id ON users(user_id);


CREATE INDEX idx_orders_user_id ON orders(user_id);


CREATE INDEX idx_orders_order_date ON orders(order_date);



--partitions
ALTER TABLE orders
   ADD PARTITION BY RANGE (order_date) (
      PARTITION orders_2021 VALUES LESS THAN (TO_DATE('01-JAN-2022', 'DD-MON-YYYY')),
      PARTITION orders_2022 VALUES LESS THAN (TO_DATE('01-JAN-2023', 'DD-MON-YYYY'))
   );