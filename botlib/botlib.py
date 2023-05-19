import pyautogui


def move_and_click(x, y, duration=0.0, clicks=1, button='left'):
    """
    Move o mouse até a posição desejada na tela e realiza um ou mais cliques.
    Parameters:
        x (int, obrigatório): a posição horizontal (coordenada x) na tela para mover o cursor do mouse.
        y (int, obrigatório): a posição vertical (coordenada y) na tela para mover o cursor do mouse.
        duration (float, opcional): o tempo em segundos que levará o cursor do mouse para chegar à posição desejada. Valor padrão é 0.0
        clicks (int, opcional): o número de cliques a serem realizados. Valor padrão é 1.
        button (str, opcional): o botão do mouse a ser pressionado. Os valores possíveis são:
          'left' para o botão esquerdo, 'right' para o botão direito e 'middle' para o botão central do mouse. Valor padrão é 'left'.

    >>> move_and_click(300, 300)
    """
    pyautogui.moveTo(x, y, duration)
    pyautogui.click(x=None, y=None, clicks=clicks, button=button)
    return
