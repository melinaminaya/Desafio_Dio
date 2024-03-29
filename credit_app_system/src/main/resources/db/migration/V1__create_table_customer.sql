CREATE TABLE cliente (
  id BIGINT GENERATED BY DEFAULT AS IDENTITY NOT NULL,
   first_name VARCHAR(255) NOT NULL,
   last_name VARCHAR(255) NOT NULL,
   cpf VARCHAR(255) NOT NULL,
   email VARCHAR(255) NOT NULL,
   password VARCHAR(255) NOT NULL,
   zip_code VARCHAR(255),
   rua VARCHAR(255),
   CONSTRAINT pk_cliente PRIMARY KEY (id)
);

ALTER TABLE cliente ADD CONSTRAINT uc_cliente_cpf UNIQUE (cpf);

ALTER TABLE cliente ADD CONSTRAINT uc_cliente_email UNIQUE (email);