"""Módulo de triagem e priorização de chamados para Service Desk."""

ORDEM_PRIORIDADE: dict[str, int] = {
    "Alta": 1,
    "Média": 2,
    "Baixa": 3,
}


class ValidadorChamado:
    """Validador responsável pela integridade e conformidade dos dados de um chamado."""

    @staticmethod
    def validar(chamado: dict[str, object]) -> None:
        """Valida a presença de campos obrigatórios e a consistência dos dados do chamado.

        Args:
            chamado (dict): Dicionário contendo os dados do chamado.

        Raises:
            ValueError: Se faltarem campos obrigatórios, se houver campos com valores
                nulos ou se a prioridade informada for desconhecida.
        """
        if not isinstance(chamado, dict) or "id" not in chamado or "prio" not in chamado:
            raise ValueError("Campos faltando na Priorização")

        if chamado["id"] is None:
            raise ValueError("Identificador nulo")

        prioridade = chamado["prio"]
        if prioridade is None:
            raise ValueError("Prioridade nula")

        if not isinstance(prioridade, str) or prioridade not in ORDEM_PRIORIDADE:
            raise ValueError(f"Prioridade desconhecida: {prioridade}")


def priorizar_chamados(chamados: list[dict]) -> list[dict]:
    """Organiza uma lista de chamados por prioridade preservando a ordem de chegada.

    A priorização segue a hierarquia: Alta > Média > Baixa.
    A estabilidade da ordem original de chegada é rigorosamente mantida para chamados
    que possuam a mesma prioridade.

    Args:
        chamados (list[dict]): Lista de dicionários representando os chamados.

    Returns:
        list[dict]: Nova lista contendo os chamados ordenados por prioridade.

    Raises:
        ValueError: Caso a entrada seja inválida ou algum chamado contenha dados inconsistentes.
    """
    if not isinstance(chamados, list):
        raise ValueError("A entrada deve ser uma lista de chamados")

    for chamado in chamados:
        ValidadorChamado.validar(chamado)

    return sorted(
        chamados,
        key=lambda item: ORDEM_PRIORIDADE[item["prio"]],
    )
