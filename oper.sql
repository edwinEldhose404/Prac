1.

SELECT SUM(price) FROM products;

2.

SELECT * FROM products WHERE price % 3 = 0;

3. 

SELECT product_name, price, price - (SELECT AVG(price) FROM products) AS price_difference FROM products;

4.

SELECT * FROM products WHERE price >= 50000;

5.

SELECT * FROM customers WHERE age <> 30;

6.

SELECT * FROM orders WHERE order_amt <= 10000;

7.

''' Bitwise & is used to compare the binary equivalent of two characters and return 1 if both 
    are 1
    Eg. 5(101) & 7(111) = 5(101)'''

8.

''' Bitwise | is used to compare the binary equivalent of two characters and returns 1 if either
    bit is 1
    Eg. 5(101) & 7(111) = 5(101)'''

9.

''' Bitwise ^ is used to compare the binary equivalent of two characters and returns 1 if both 
    are different
    Eg. 5(101) & 7(111) = 2(010)'''

10.

SELECT * FROM products WHERE location = 'Mumbai' AND stocklvl > 10;

11.

SELECT * FROM customers WHERE city = 'Mumbai' OR c_id IN (SELECT c_id FROM orders WHERE order_amt > 20000);

12.

SELECT * FROM orders WHERE pmt_mode <> 'upi' AND status = 'completed';






