from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect

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