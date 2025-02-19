from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect

from modules.field.use_cases import (
    list_fields_by_user,
    create_field,
    get_field,
    edit_field,
    delete_field,
)

from modules.harvest_history.use_cases import (
    list_harvest_history_by_user_and_field,
    create_harvest,
    delete_harvest,
    map_productivity_fields
)

from modules.shared.errors.error_schema import ErrorSchema
from modules.field.schemas import (
    ListFieldsByUserQuerySchema,
    ListFieldsByUserResponseSchema,
    FieldResponseSchema,
    CreateFieldSchema,
    FieldByIdQuerySchema,
    EditFieldSchema,
)
from modules.harvest_history.schemas import (
    ListHarvestHistoryByUserAndFieldResponseSchema,
    ListHarvestHistoryByUserAndFieldQuerySchema,
    HarvestResponseSchema,
    CreateHarvestSchema,
    HarvestByIdAndFieldSchemaQuerySchema,
    ProductivityMapResponseSchema,
    ProductivityMapQuerySchema,
)
from modules.shared.schemas import (
    DeleteResponseSchema,
)

from modules.shared.config.db_sqlite import *
from flask_cors import CORS

info = Info(title="AgriPrecision - Serviço de Colheita API", version="1.0.0")
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
def list_fields_by_user_route(query: ListFieldsByUserQuerySchema):
    """
        Lista talhões de um usuário
    """
    return list_fields_by_user(query)

@app.post('/fields/create', tags=[field_tag], responses={'200': FieldResponseSchema, '400': ErrorSchema})
def create_field_route(form: CreateFieldSchema):
    """
        Cria novo talhão
    """
    return create_field(form)

@app.get('/fields/one', tags=[field_tag], responses={'200': FieldResponseSchema, '404': ErrorSchema})
def get_field_route(query: FieldByIdQuerySchema):
    """
        Busca um talhão através de seu identificador e usuário
    """
    return get_field(query)

@app.put('/fields/edit', tags=[field_tag], responses={'200': FieldResponseSchema, '404': ErrorSchema})
def edit_field_route(form: EditFieldSchema):
    """
        Edita um talhão através de seu identificador e usuário
    """
    return edit_field(form)

@app.delete('/fields/delete', tags=[field_tag], responses={'200': DeleteResponseSchema, '404': ErrorSchema})
def delete_field_route(query: FieldByIdQuerySchema):
    """
        Remove um talhão através de seu identificador e usuário
    """
    return delete_field(query)

# ----------------------------- Harvest History Routes -----------------------------
harvest_history_tag = Tag(name="Histórico de Colheitas", description="Adição, visualização e deleção do histórico de colheitas na base de dados.")

@app.get('/harvest-history', tags=[harvest_history_tag], responses={'200': ListHarvestHistoryByUserAndFieldResponseSchema, '404': ErrorSchema})
def list_harvest_history_by_user_and_field_route(query: ListHarvestHistoryByUserAndFieldQuerySchema):
    """
        Lista histórico de colheitas de um usuário em um talhão
    """
    return list_harvest_history_by_user_and_field(query)

@app.post('/harvest-history/create', tags=[harvest_history_tag], responses={'200': HarvestResponseSchema, '400': ErrorSchema})
def create_harvest_history_route(form: CreateHarvestSchema):
    """
        Registra nova colheita em um talhão de um usuário
    """
    return create_harvest(form)

@app.delete('/harvest-history/delete', tags=[harvest_history_tag], responses={'200': DeleteResponseSchema, '404': ErrorSchema})
def delete_harvest_history_route(query: HarvestByIdAndFieldSchemaQuerySchema):
    """
        Remove um registro de colheita através de seu identificador, talhão e usuário
    """
    return delete_harvest(query)

@app.get('/harvest-history/map-productivity', tags=[harvest_history_tag], responses={'200': ProductivityMapResponseSchema, '404': ErrorSchema})
def map_productivity_fields_route(query: ProductivityMapQuerySchema):
    """
        Retorna mapa de produtividade dos talhões
    """
    return map_productivity_fields(query)