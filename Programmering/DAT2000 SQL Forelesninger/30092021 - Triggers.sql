-- Trigger to delete the symmeticral friend
-- Whenever someone deletes a friendship, for example friend 1 and friend 4
-- (Which are record ID1 = 1, ID2 = 4)
-- then we can assume friend 4 no longer considers friend 1 a friend.
-- So the trigger deletes the record ID1 = 4/ ID2 = 1

CREATE OR REPLACE TRIGGER FriendshipDrama
AFTER DELETE ON Friend
FOR EACH ROW
WHEN EXISTS (SELECT * FROM Friend
			WHERE ID1 = OLD.ID2 AND ID2 = OLD.ID1)
BEGIN 
	DELETE FROM Friend
	WHERE ID1 = OLD.ID2 AND ID2 = OLD.ID1;
END
	
-- Trigger to add symmeticral friend whenever a friend is added
-- For example if friend 1 is friend with 6 and this is added
-- then this trigger adds friend 6 with friend 1.
-- So if friend ID1 = 1, ID2 = 6 is added this trigger adds
-- the record ID1 = 6, ID2 = 1

CREATE OR REPLACE TRIGGER FriendShipRenewed
AFTER INSERT ON Friend
FOR EACH ROW
WHEN NOT EXISTS (SELECT * FROM Friend
				WHERE ID1 = NEW.ID2 AND ID2 = NEW.ID1)
BEGIN 
	INSERT INTO Friend VALUES (NEW.ID2,NEW.ID1);
END
