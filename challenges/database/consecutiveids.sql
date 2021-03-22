CREATE PROCEDURE consecutiveIds()
SELECT id oldid, @a:=@a+1 newid FROM itemIds,(SELECT @a:=0)t
