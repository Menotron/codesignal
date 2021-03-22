CREATE PROCEDURE dancingcompetition()
BEGIN
CREATE OR REPLACE VIEW v(w,x,y,z) AS SELECT * FROM scores;
  SELECT w,x,y,z
  FROM (
      SELECT *, 
      IF(x = i || x = j,1,0) AS p,
      IF(y = k || y = l,1,0) AS q,
      IF(z = m || z = n,1,0) AS r FROM v 
      JOIN (
          SELECT max(x)  AS i,
          min(x) AS j,
          max(y) AS k,
          min(y) AS l,
          max(z) AS m,
          min(z) AS n FROM v)b)a
  WHERE  (p + q + r) < 2;
END
