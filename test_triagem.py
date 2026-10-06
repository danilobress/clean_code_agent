"""Suíte de testes para o módulo de triagem e priorização de chamados."""

# pyrefly: ignore [missing-import]
import pytest
from triagem import priorizar_chamados


def test_dado_chamados_com_prioridades_diferentes_quando_priorizar_entao_ordena_por_prioridade() -> None:
    """Valida que chamados de prioridade Alta precedem os de prioridade Baixa."""
    # Arrange
    lista_chamados = [
        {"id": 1, "prio": "Baixa"},
        {"id": 2, "prio": "Alta"},
        {"id": 3, "prio": "Alta"},
    ]

    # Act
    resultado = priorizar_chamados(lista_chamados)

    # Assert
    esperado = [
        {"id": 2, "prio": "Alta"},
        {"id": 3, "prio": "Alta"},
        {"id": 1, "prio": "Baixa"},
    ]
    assert resultado == esperado


def test_dado_chamados_com_mesma_prioridade_quando_priorizar_entao_preserva_ordem_de_chegada() -> None:
    """Valida a estabilidade da ordenação mantendo a ordem original para prioridades iguais."""
    # Arrange
    lista_chamados = [
        {"id": 1, "prio": "Média"},
        {"id": 2, "prio": "Média"},
    ]

    # Act
    resultado = priorizar_chamados(lista_chamados)

    # Assert
    esperado = [
        {"id": 1, "prio": "Média"},
        {"id": 2, "prio": "Média"},
    ]
    assert resultado == esperado


def test_dado_prioridades_intercaladas_quando_priorizar_entao_ordena_alta_media_baixa_preservando_ordem_de_chegada() -> None:
    """Valida a hierarquia Alta > Média > Baixa e a estabilidade com prioridades intercaladas."""
    # Arrange
    lista_chamados = [
        {"id": 1, "prio": "Baixa"},
        {"id": 2, "prio": "Média"},
        {"id": 3, "prio": "Alta"},
        {"id": 4, "prio": "Baixa"},
        {"id": 5, "prio": "Média"},
        {"id": 6, "prio": "Alta"},
    ]

    # Act
    resultado = priorizar_chamados(lista_chamados)

    # Assert
    esperado = [
        {"id": 3, "prio": "Alta"},
        {"id": 6, "prio": "Alta"},
        {"id": 2, "prio": "Média"},
        {"id": 5, "prio": "Média"},
        {"id": 1, "prio": "Baixa"},
        {"id": 4, "prio": "Baixa"},
    ]
    assert resultado == esperado


def test_dado_prioridade_desconhecida_quando_priorizar_entao_lanca_value_error() -> None:
    """Valida o lançamento de ValueError quando uma prioridade não permitida é informada."""
    # Arrange
    lista_chamados = [{"id": 1, "prio": "Urgente"}]

    # Act & Assert
    with pytest.raises(ValueError, match=r"^Prioridade desconhecida: Urgente$"):
        priorizar_chamados(lista_chamados)


def test_dado_prioridade_com_tipo_invalido_quando_priorizar_entao_lanca_value_error() -> None:
    """Valida o lançamento de ValueError quando a prioridade não for do tipo string (ex: lista)."""
    # Arrange
    lista_chamados = [{"id": 1, "prio": ["Alta"]}]

    # Act & Assert
    with pytest.raises(ValueError, match=r"^Prioridade desconhecida: \['Alta'\]$"):
        priorizar_chamados(lista_chamados)


def test_dado_prioridade_nula_quando_priorizar_entao_lanca_value_error() -> None:
    """Valida o lançamento de ValueError quando o campo de prioridade for nulo."""
    # Arrange
    lista_chamados = [{"id": 1, "prio": None}]

    # Act & Assert
    with pytest.raises(ValueError, match=r"^Prioridade nula$"):
        priorizar_chamados(lista_chamados)


def test_dado_chamado_sem_identificador_quando_priorizar_entao_lanca_value_error() -> None:
    """Valida o lançamento de ValueError quando o campo obrigatório 'id' estiver ausente."""
    # Arrange
    lista_chamados = [{"prio": "Baixa"}]

    # Act & Assert
    with pytest.raises(ValueError, match=r"^Campos faltando na Priorização$"):
        priorizar_chamados(lista_chamados)


def test_dado_chamado_sem_prioridade_quando_priorizar_entao_lanca_value_error() -> None:
    """Valida o lançamento de ValueError quando a chave obrigatória 'prio' estiver ausente."""
    # Arrange
    lista_chamados = [{"id": 1}]

    # Act & Assert
    with pytest.raises(ValueError, match=r"^Campos faltando na Priorização$"):
        priorizar_chamados(lista_chamados)


def test_dado_identificador_nulo_quando_priorizar_entao_lanca_value_error() -> None:
    """Valida o lançamento de ValueError quando o campo 'id' for nulo."""
    # Arrange
    lista_chamados = [{"id": None, "prio": "Alta"}]

    # Act & Assert
    with pytest.raises(ValueError, match=r"^Identificador nulo$"):
        priorizar_chamados(lista_chamados)


def test_dado_identificador_e_prioridade_nulos_quando_priorizar_entao_lanca_value_error() -> None:
    """Valida o lançamento de ValueError quando o campo 'id' e 'prio' forem nulos."""
    # Arrange
    lista_chamados = [{"id": None, "prio": None}]

    # Act & Assert
    with pytest.raises(ValueError, match=r"^Identificador nulo$"):
        priorizar_chamados(lista_chamados)


def test_dado_lista_vazia_quando_priorizar_entao_retorna_lista_vazia() -> None:
    """Valida o comportamento da função ao receber uma lista vazia."""
    # Arrange
    lista_chamados: list[dict] = []

    # Act
    resultado = priorizar_chamados(lista_chamados)

    # Assert
    assert resultado == []


def test_dado_entrada_invalida_nao_lista_quando_priorizar_entao_lanca_value_error() -> None:
    """Valida o lançamento de ValueError caso a entrada não seja uma lista."""
    # Arrange
    entrada_invalida = "invalido"

    # Act & Assert
    with pytest.raises(ValueError, match=r"^A entrada deve ser uma lista de chamados$"):
        priorizar_chamados(entrada_invalida)  # type: ignore
