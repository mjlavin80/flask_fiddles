CREATE TABLE IF NOT EXISTS metadata (doc_id INTEGER PRIMARY KEY AUTO_INCREMENT, title VARCHAR(32), authorship VARCHAR(32), role VARCHAR(32)) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS tokens (token_id INTEGER PRIMARY KEY AUTO_INCREMENT, doc_id INTEGER,
	term_id INTEGER, token VARCHAR(32), pos VARCHAR(32), FOREIGN KEY(doc_id) REFERENCES metadata(doc_id) ON DELETE CASCADE) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS counts (type_id INTEGER PRIMARY KEY AUTO_INCREMENT, doc_id INTEGER,
	term_id INTEGER, type VARCHAR(32), type_count INTEGER, FOREIGN KEY(doc_id) REFERENCES metadata(doc_id) ON DELETE CASCADE) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS tfidf (doc_id INTEGER, tf DOUBLE, tf_idf DOUBLE, FOREIGN KEY(doc_id) REFERENCES metadata(doc_id) ON DELETE CASCADE) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS corpus (corpus_id INTEGER PRIMARY KEY AUTO_INCREMENT, corpus_title VARCHAR(32)) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS corpus_doc (corpus_id INTEGER, doc_id INTEGER, FOREIGN KEY(doc_id)
	REFERENCES metadata(doc_id), FOREIGN KEY(corpus_id) REFERENCES corpus(corpus_id) ON DELETE CASCADE) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS library_dict (term_id INTEGER PRIMARY KEY AUTO_INCREMENT, _term VARCHAR(32) UNIQUE,
	library_count INTEGER, library_tf DOUBLE, idf DOUBLE) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS cosine (cos_id INTEGER PRIMARY KEY AUTO_INCREMENT, source INTEGER, target INTEGER, cos_sim DOUBLE) ENGINE=INNODB;


CREATE INDEX lib_terms ON library_dict (term_id, _term, library_count, library_tf, idf);
CREATE INDEX cos on cosine(cos_id, source, target, cos_sim);
CREATE INDEX countz ON counts (doc_id, type_id, type, type_count, tf, tf_idf);
CREATE INDEX meta ON metadata (doc_id,title, authorship);
CREATE INDEX toke ON tokens (doc_id, token_id, token, pos);
CREATE INDEX corp ON corpus (corpus_id, corpus_title);
CREATE INDEX corp_doc ON corpus_doc (doc_id, corpus_id);

ALTER TABLE token ADD CONSTRAINT a FOREIGN KEY(term_id) REFERENCES library_dict(term_id);

ALTER TABLE counts ADD CONSTRAINT b FOREIGN KEY(term_id) REFERENCES library_dict(term_id);