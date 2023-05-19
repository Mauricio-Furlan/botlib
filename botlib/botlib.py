import pyautogui


def move_and_click(x, y, duration=0.0, clicks=1, button='left', *args):
    """
    Move o mouse até a posição desejada na tela e realiza um ou mais cliques.
    Parameters:
        x (int): a posição horizontal (coordenada x) na tela para mover o cursor do mouse.
        y (int): a posição vertical (coordenada y) na tela para mover o cursor do mouse.
        duration (float): o tempo em segundos que levará o cursor do mouse para chegar à posição desejada.
        clicks (int): o número de cliques a serem realizados.
        button (str): o botão do mouse a ser pressionado. Os valores possíveis são:
          'left' para o botão esquerdo, 'right' para o botão direito e 'middle' para o botão central do mouse.

    >>> move_and_click(x=350, y=300, duration=0)
    """
    pyautogui.moveTo(x, y, duration, *args)
    pyautogui.click(x=None, y=None, clicks=clicks, button=button)
    return
