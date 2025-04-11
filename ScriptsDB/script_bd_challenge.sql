DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'estoques') THEN
        CREATE TABLE Estoques (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            status VARCHAR(50) NOT NULL,
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    END IF;
END $$;
-----------------------------------------------------------------------------------------------------------------------
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'localizacoes') THEN
        CREATE TABLE Localizacoes (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            estoque_id INT NOT NULL REFERENCES Estoques(id)
        );
    END IF;
END $$;
-----------------------------------------------------------------------------------------------------------------------
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'tiposequipamento') THEN
        CREATE TABLE TiposEquipamento (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL
        );
    END IF;
END $$;

DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM TiposEquipamento) THEN
        INSERT INTO TiposEquipamento (nome)
        VALUES ('mouse'), 
               ('teclado'),
			   ('headset'),
			   ('notebook');
    END IF;
END$$;


-----------------------------------------------------------------------------------------------------------------------
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'categorias') THEN
        CREATE TABLE Categorias (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL
        );
    END IF;
END $$;

DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Categorias) THEN
        INSERT INTO Categorias (nome)
        VALUES ('periferico'), 
               ('IOT'),
			   ('dispositivo de rede'),
			   ('computador pessoal');
    END IF;
END$$;

-----------------------------------------------------------------------------------------------------------------------
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'equipamentos') THEN
        CREATE TABLE Equipamentos (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            status VARCHAR(50) NOT NULL,
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            estoque_id INT NOT NULL REFERENCES Estoques(id),
            tipo_id INT NOT NULL REFERENCES TiposEquipamento(id),
            categoria_id INT NOT NULL REFERENCES Categorias(id)
        );
    END IF;
END $$;

-----------------------------------------------------------------------------------------------------------------------
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'tiposusuario') THEN
        CREATE TABLE tiposusuario (
            id SERIAL PRIMARY KEY,
            descricao VARCHAR(100) NOT NULL
        );
    END IF;
END $$;

DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM tiposusuario) THEN
        INSERT INTO tiposusuario (id, descricao)
        VALUES (1, 'ADMIN'), 
               (2, 'OPERADOR');
    END IF;
END$$;

-----------------------------------------------------------------------------------------------------------------------
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'usuarios') THEN
        CREATE TABLE usuarios (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            senha_hash VARCHAR(255) NOT NULL,
            tipo_usuario INT NOT NULL REFERENCES tiposusuario(id)
        );
    END IF;
END $$;

-----------------------------------------------------------------------------------------------------------------------
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'historicomovimentacao') THEN
        CREATE TABLE HistoricoMovimentacao (
            id SERIAL PRIMARY KEY,
            equipamento_id INT NOT NULL REFERENCES Equipamentos(id),
            usuario_id INT NOT NULL REFERENCES Usuarios(id),
            tipo_movimentacao VARCHAR(50) NOT NULL,
            data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            localizacao_id INT NOT NULL REFERENCES Localizacoes(id)
        );
    END IF;
END $$;