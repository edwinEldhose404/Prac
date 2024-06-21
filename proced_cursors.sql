
1.
DELIMITER //

CREATE FUNCTION calculate_t_rev()
RETURNS DECIMAL(10,2)
BEGIN
    DECLARE t_rev DECIMAL(10,2);

    SELECT SUM(o.amount)
    INTO t_rev
    FROM orders o
    JOIN payment p ON o.o_id = p.o_id
    WHERE o.status = 'completed';

    RETURN t_rev;
END//

SELECT calculate_t_rev() AS t_rev;

//

DELIMITER ;
2.
  DELIMITER //

CREATE FUNCTION calculate_t_rev()
RETURNS DECIMAL(10,2)
BEGIN
    DECLARE t_rev DECIMAL(10,2);

    SELECT SUM(o.amount)
    INTO t_rev
    FROM orders o
    JOIN payment p ON o.o_id = p.o_id
    WHERE o.status = 'completed';

    RETURN t_rev;
END//

SELECT calculate_t_rev() AS t_rev;

//

DELIMITER ;

3.
DELIMITER //

CREATE PROCEDURE get_product_details(IN product_id INT)
BEGIN
    SELECT * FROM products WHERE product_id = product_id;
END//

CALL get_product_details(5);

//

DELIMITER ;

4.
DELIMITER //

CREATE PROCEDURE get_product_count(OUT p_count INT)
BEGIN
    SELECT COUNT(*) INTO p_count FROM products;
END//

CALL get_product_count(@product_count);
SELECT @p_count AS product_count;

//

DELIMITER ;

5.

SET @t_price = 0;

DECLARE done INT DEFAULT FALSE;
DECLARE p_price DECIMAL(10,2);

DECLARE cur CURSOR FOR
    SELECT price FROM products WHERE category = 'Electronics';

DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

OPEN cur;

read_loop: LOOP
    FETCH cur INTO p_price;
    IF done THEN
        LEAVE read_loop;
    END IF;
    SET @t_price = @t_price + p_price;
END LOOP;

CLOSE cur;

SELECT @t_price AS t_price;

6.

SET @p_name = '';

DECLARE done INT DEFAULT FALSE;
DECLARE p_name VARCHAR(255);

DECLARE cur CURSOR FOR
    SELECT name FROM products;

DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

OPEN cur;

read_loop: LOOP
    FETCH cur INTO p_name;
    IF done THEN
        LEAVE read_loop;
    END IF;
    SELECT p_name;
END LOOP;

CLOSE cur;

