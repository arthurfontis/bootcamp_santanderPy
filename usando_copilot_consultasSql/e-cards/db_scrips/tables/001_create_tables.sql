CREATE TABLE tbl_collections (
    id INT AUTO_INCREMENT PRIMARY KEY,
    collectionSetName VARCHAR(100) NOT NULL,
    releaseDate DATE NOT NULL,
    totalCardsInCollection INT NOT NULL
);

CREATE TABLE tbl_types (
    id INT AUTO_INCREMENT PRIMARY KEY,
    typeName VARCHAR(50) NOT NULL
);


CREATE TABLE tbl_stages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    stageName VARCHAR(50) NOT NULL
);

CREATE TABLE tbl_cards (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hp INT,
    name VARCHAR(100) NOT NULL,
    type_id INT,
    stage_id INT,
    info TEXT,
    attack VARCHAR(100),
    damage INT,
    weak VARCHAR(50),
    resis VARCHAR(50),
    retreat VARCHAR(50),
    cardNumberInCollection INT,
    collection_id INT,
    FOREIGN KEY (type_id) REFERENCES tbl_types(id),
    FOREIGN KEY (stage_id) REFERENCES tbl_stages(id),
    FOREIGN KEY (collection_id) REFERENCES tbl_collections(id)
);
