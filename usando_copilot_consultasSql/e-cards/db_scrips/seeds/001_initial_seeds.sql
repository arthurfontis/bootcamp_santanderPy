INSERT INTO tbl_collections (collectionSetName, releaseDate, totalCardsInCollection)
VALUES
('Base Set', '1999-01-09', 102),
('Jungle', '1999-06-16', 64),
('Fossil', '1999-10-10', 62);

INSERT INTO tbl_types (typeName)
VALUES
('Fire'),
('Water'),
('Electric'),
('Grass'),
('Fighting'),
('Psychic');

INSERT INTO tbl_stages (stageName)
VALUES
('Basic'),
('Stage 1'),
('Stage 2');

INSERT INTO tbl_cards (hp, name, type_id, stage_id, info, attack, damage, weak, resis, retreat, cardNumberInCollection, collection_id)
VALUES
(120, 'Charizard', 1, 3, 'Flame Pokémon. Length: 5''7", Weight: 200 lbs.', 'Fire Spin', 100, 'Water', 'Fighting -30', '★★★', 4, 1),
(100, 'Blastoise', 2, 3, 'Shellfish Pokémon. Length: 5''3", Weight: 189 lbs.', 'Hydro Pump', 40, 'Electric', NULL, '★★★', 2, 1),
(40, 'Pikachu', 3, 1, 'Mouse Pokémon. Length: 1''0", Weight: 13 lbs.', 'Thunder Jolt', 30, 'Fighting', NULL, '★', 60, 2),
(70, 'Scyther', 4, 1, 'Mantis Pokémon. Length: 4''11", Weight: 123 lbs.', 'Slash', 30, 'Fire', NULL, '★★', 10, 2),
(70, 'Hitmonchan', 5, 1, 'Punching Pokémon. Length: 4''7", Weight: 111 lbs.', 'Special Punch', 40, 'Psychic', NULL, '★★', 7, 1);
