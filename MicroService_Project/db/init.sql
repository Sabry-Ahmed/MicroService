create database devopsroles;
use devopsroles;

CREATE TABLE test_table (
  login VARCHAR(20),
  mdp VARCHAR(20)
);

INSERT INTO test_table
  (login, mdp)
VALUES
  ('admin', 'admin'),
  ('user', 'user');
