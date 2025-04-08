from sqlalchemy.exc import SQLAlchemyError
from src.repositories.usuarioRepository import UsuarioRepository
from src.schemas.usuarioSchema import UsuarioCreate
from src.models.usuarioModel import UsuarioModel
from src.enums.tipoUsuarioEnum import TipoUsuarioEnum
from passlib.hash import bcrypt
from src.utils.auth import create_access_token


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
            if usuario_data.tipoUsuario not in [tipo.value for tipo in TipoUsuarioEnum]:
                raise ValueError("O tipoUsuarioId fornecido é inválido")

            if self.repository.get_by_email(usuario_data.email):
                raise ValueError("E-mail já está em uso")

            hashed_password = bcrypt.hash(usuario_data.senha)

            novo_usuario = UsuarioModel(
                nome=usuario_data.nome,
                email=usuario_data.email,
                senha_hash=hashed_password,
                tipo_usuario=usuario_data.tipoUsuario
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
            return {"tokenType": "bearer", "accessToken": token}

        except SQLAlchemyError as e:
            raise Exception("Erro ao fazer login: " + str(e))
