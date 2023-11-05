from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel


class Atributos(BaseModel):
    rotulo: str
    chave: str
    tipo: str
    mascara: str

class Filtros(BaseModel):
    url: str
    instrucao: str
    atributos: List[Atributos]
    
class Consultas(BaseModel):
    nome: str
    url: str
    descricao: str
    filtros: List[Filtros]

class Contrato(BaseModel):
    versao_protocolo: int
    nome: str
    referencia: str
    tipo: int
    logo: str
    descricao: str
    consultas: List[Consultas]