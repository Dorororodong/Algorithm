'''
# [Oracle]
# Select CART_ID
# From CART_PRODUCTS
# Where NAME = 'Milk'
# INTERSECT
# Select CART_ID
# From CART_PRODUCTS
# Where NAME = 'Yogurt';

# [Self Join]
# SELECT A.CART_ID
# FROM CART_PRODUCTS as A
# JOIN CART_PRODUCTS as B
# ON A.CART_ID = B.CART_ID
# WHERE A.NAME = "Milk" AND B.NAME = "Yogurt"
# ORDER BY CART_ID;

Select Distinct C.CART_ID
From CART_PRODUCTS as C, CART_PRODUCTS as T
Where C.CART_ID = T.CART_ID And (C.NAME = 'Milk' And T.NAME = 'Yogurt');
'''