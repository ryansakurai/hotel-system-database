-- role creation
CREATE ROLE administrator SUPERUSER;
CREATE ROLE manager;
CREATE ROLE attendant; 
CREATE ROLE client;
CREATE ROLE "anonymous";

ALTER DATABASE hotel_system OWNER TO administrator;

SET ROLE administrator;

-- grants in "guest"
GRANT SELECT ON guest TO manager;
GRANT SELECT ON guest TO attendant;
GRANT SELECT, INSERT, UPDATE, DELETE ON guest TO client;

-- grants in "hotel"
GRANT SELECT, UPDATE(email, website) ON hotel TO manager;
GRANT SELECT ON hotel TO attendant;
GRANT SELECT ON hotel TO client;
GRANT SELECT ON hotel TO "anonymous";

-- grants in "room"
GRANT SELECT, INSERT, UPDATE(daily_rate, "type"), DELETE ON room TO manager;
GRANT SELECT ON room TO attendant;
GRANT SELECT ON room TO client;
GRANT SELECT ON room TO "anonymous";

-- grants in "reservation"
GRANT SELECT ON reservation TO manager;
GRANT SELECT, INSERT, UPDATE, DELETE ON reservation TO attendant;
GRANT SELECT ON reservation TO client;
