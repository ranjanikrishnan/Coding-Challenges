SELECT C.NAME AS CUSTOMERS FROM CUSTOMERS C
LEFT JOIN ORDERS O ON C.ID = O.ID  
WHERE C.ID NOT IN (SELECT ORDERS.CustomerId FROM ORDERS)