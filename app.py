from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect

from modules.field.use_cases import (
    list_fields_by_user,
    create_field,
)

from modules.shared.errors.error_schema import ErrorSchema
from modules.field.schemas import (
    ListFieldsByUserQuerySchema,
    ListFieldsByUserResponseSchema,
    FieldResponseSchema,
    CreateFieldSchema
)

from modules.shared.config.db_sqlite import *
from flask_cors import CORS

info = Info(title="AgriPrecisison - Serviço de Colheita API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# ----------------------------- Home Route -----------------------------
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

# ----------------------------- Fields Routes -----------------------------
field_tag = Tag(name="Talhão", description="Adição, visualização, edição e deleção de talhões na base de dados.")

@app.get('/fields', tags=[field_tag], responses={'200': ListFieldsByUserResponseSchema, '404': ErrorSchema})
def list_study_trails_by_user_route(query: ListFieldsByUserQuerySchema):
    """
        Lista talhões de um usuário
    """
    return list_fields_by_user(query)

@app.post('/fields/create', tags=[field_tag], responses={'200': FieldResponseSchema, '409': ErrorSchema, '400': ErrorSchema})
def create_user_route(form: CreateFieldSchema):
    """
        Cria novo talhão
    """
    return create_field(form)