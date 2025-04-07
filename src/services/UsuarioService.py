from sqlalchemy.exc import SQLAlchemyError
from src.repositories.UsuarioRepository import UsuarioRepository
from src.schemas.UsuarioSchema import UsuarioCreate
from src.models.UsuarioModel import UsuarioModel
from passlib.hash import bcrypt
from src.utils.Auth import create_access_token


class UsuarioService:

    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def get_all_usuarios(self):
        try:
            return self.repository.get_all()
        except SQLAlchemyError as e:
            raise Exception(f"Erro ao buscar usuários: {str(e)}")

    def register_usuario(self, usuario_data: UsuarioCreate):
        try:
            # Verificar se o e-mail já está registrado
            if self.repository.get_by_email(usuario_data.email):
                raise ValueError("E-mail já está em uso")

            # Hash da senha
            hashed_password = bcrypt.hash(usuario_data.senha)

            novo_usuario = UsuarioModel(
                nome=usuario_data.nome,
                email=usuario_data.email,
                senha_hash=hashed_password
            )

            self.repository.create(novo_usuario)
            return {"message": "Usuário registrado com sucesso"}

        except SQLAlchemyError as e:
            raise Exception("Erro ao registrar usuário: " + str(e))

    def login_usuario(self, email: str, senha: str):
        try:
            # Buscar usuário pelo e-mail
            usuario = self.repository.get_by_email(email)
            if not usuario:
                raise ValueError("E-mail ou senha inválidos")

            # Verificar a senha
            if not bcrypt.verify(senha, usuario.senha_hash):
                raise ValueError("E-mail ou senha inválidos")

            # Gerar token JWT
            token = create_access_token({"sub": usuario.email})
            return {"access_token": token, "token_type": "bearer"}

        except SQLAlchemyError as e:
            raise Exception("Erro ao fazer login: " + str(e))
