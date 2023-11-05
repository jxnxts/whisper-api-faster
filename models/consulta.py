from typing import List, Optional
from pydantic import BaseModel

class Campo(BaseModel):
    rotulo: Optional[str] = None
    chave: Optional[str] = None
    valor: Optional[str] = None
    largura: Optional[int] = None
    tipo: Optional[int] = None

class Url(BaseModel):
    url: Optional[str] = None
class Base64(BaseModel):
    base64: Optional[str] = None


class Resultado(BaseModel):
    documento: Optional[str] = None
    referencia: Optional[str] = None
    imagens: Optional[List[Url]] = None
    campos: Optional[List[Campo]] = None
    botoes: Optional[List[str]] = None

class Consulta(BaseModel):
    versao_protocolo: int = 1
    resultado: Optional[List[Resultado]] = None