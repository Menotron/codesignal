CREATE PROCEDURE pastEvents()
SELECT name, event_date from Events where DATEDIFF((SELECT max(event_date) m from events),event_date)^7 < 7 order by 2 desc;
