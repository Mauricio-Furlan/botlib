import time

import pyautogui

from actions.my_keyboard import key_down, press, release_key
from actions.wait_time import wait_time


class Bot:
    """
    Classe que representa um bot para automação de ações com o PyAutoGUI.

    Methods:
        __call__(*args, **kwargs): Permite a chamada direta da instância da classe.
        search_image(path_img, confidence=0.85, region=None): Procura por uma imagem na tela e armazena suas coordenadas.
        wait_image(path_img, seg=0, confidence=0.85, region=None): Aguarda a aparição de uma imagem na tela.
        moveTo(x=None, y=None, **kargs): Move o cursor do mouse para as coordenadas especificadas.
        click(**kargs): Realiza um clique do mouse.
        sleep(seg): Aguarda um determinado tempo em segundos.
        press_button(key, delay=0.5): Pressiona uma tecla do teclado.
        key_down_button(button): Mantém uma tecla pressionada.
        release_key_button(button): Libera uma tecla pressionada.
        position(log=False): Retorna a posição atual do cursor do mouse ou exibe em tempo real no terminal.

    Attributes:
        box: Armazena o retângulo delimitador da última imagem encontrada.
        x: Coordenada x do centro da última imagem encontrada.
        y: Coordenada y do centro da última imagem encontrada.
        path_img: Caminho da imagem a ser buscada.

    Exemplos:
        >>> bot = Bot().moveTo(500, 500).click(clicks=2)
    """

    def __call__(self, *args, **kwargs):
        return self

    def _search_image(self, path_img, confidence=0.85, region=None):
        """
        Procura por uma imagem na tela e armazena suas coordenadas.

        Args:
            path_img (str): O caminho da imagem a ser procurada.
            confidence (float, optional): O nível de confiança para a busca da imagem. Valor padrão é 0.85.
            region (tuple, optional): Uma tupla que representa a região da tela onde a imagem será procurada.
                                     Valor padrão é None (busca em toda a tela).

        Returns:
            self: A própria instância da classe.

        """
        img = pyautogui.locateOnScreen(
            path_img, confidence=confidence, region=region
        )
        if img != None:
            self.box = img
            self.x, self.y = pyautogui.center(img)
            return self
        return None

    def wait_image(self, path_img, seg=0, confidence=0.85, region=None):
        """
        Aguarda a aparição de uma imagem na tela.

        Args:
            path_img (str): O caminho da imagem a ser procurada.
            seg (int, optional): O tempo máximo, em segundos, a aguardar pela aparição da imagem.
                                Valor padrão é 0 (não aguardar, realiza apenas uma busca).
            confidence (float, optional): O nível de confiança para a busca da imagem. Valor padrão é 0.85.
            region (tuple, optional): Uma tupla que representa a região da tela onde a imagem será procurada.
                                    Valor padrão é None (busca em toda a tela).

        Returns:
            self: A própria instância da classe se a imagem for encontrada.
            None: Caso a imagem não seja encontrada ou o tempo de espera seja atingido.

        """
        self.path_img = path_img
        if seg == 0:
            self._search_image(
                'test_img.PNG', confidence=confidence, region=region
            )
            return self
        if not wait_time(
            seg,
            seg=True,
            exec_fn=lambda: self._search_image(
                'test_img.PNG', confidence=confidence, region=region
            ),
        ):
            return self
        return None

    def moveTo(self, x=None, y=None, **kargs):
        """
        Move o cursor do mouse para as coordenadas especificadas.

        Args:
            x (int, optional): A coordenada x para mover o cursor. Se None, mantém a coordenada atual.
            y (int, optional): A coordenada y para mover o cursor. Se None, mantém a coordenada atual.
            **kargs: Outros argumentos aceitos pelo método `pyautogui.moveTo()`.

        Returns:
            self: A própria instância da classe.

        """
        if x == None and y == None:
            pyautogui.moveTo(self.x, self.y, **kargs)
        pyautogui.moveTo(x, y, **kargs)
        return self

    def click(self, **kargs):
        """
        Realiza um clique do mouse.

        Args:
            **kargs: Outros argumentos aceitos pelo método `pyautogui.click()`.

        Returns:
            self: A própria instância da classe.

        """
        pyautogui.click(**kargs)
        return self

    def sleep(self, seg):
        """
        Aguarda um determinado tempo em segundos.

        Args:
            seg (int): O tempo de espera em segundos.

        Returns:
            self: A própria instância da classe.

        """
        time.sleep(seg)
        return self

    def press_button(self, key, delay=0.5):
        """
        Pressiona uma tecla do teclado.

        Args:
            key (str): A tecla a ser pressionada.
            delay (float, optional): O tempo de atraso após pressionar a tecla. Valor padrão é 0.5.

        Returns:
            self: A própria instância da classe.

        """
        press(key, delay)
        return self

    def key_down_button(self, button):
        """
        Mantém uma tecla pressionada.

        Args:
            button (str): A tecla a ser mantida pressionada.

        Returns:
            self: A própria instância da classe.

        """
        key_down(button)
        return self

    def release_key_button(self, button):
        """
        Libera uma tecla pressionada.

        Args:
            button (str): A tecla a ser liberada.

        Returns:
            self: A própria instância da classe.

        """
        release_key(button)
        return self

    def position(self, log=False):
        """
        Retorna a posição atual do cursor do mouse ou exibe em tempo real no terminal.

        Args:
            log (bool, optional): Define se a posição deve ser exibida em tempo real no terminal.
                                  Valor padrão é False.

        Returns:
            tuple: Uma tupla contendo as coordenadas x e y atuais do cursor do mouse.

        """
        if log:
            print('Press Ctrl-C to quit.')
            try:
                while True:
                    print(pyautogui.position(), end='\r')
            except KeyboardInterrupt:
                print('P')
        else:
            return pyautogui.position()


if __name__ == '__main__':
    print('oi')
    x = pyautogui.locateOnScreen('p')
    if x != None:
        pyautogui.moveTo(x)
    action = Bot().position(log=True)
    print('aa', action)
