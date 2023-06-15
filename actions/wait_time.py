import datetime
import threading
import time

import keyboard


def check_time(time_init):
    now = datetime.datetime.now()
    past_time = now > time_init
    if past_time:
        return True
    else:
        return False


def wait_time(value, seg=None, exec_fn=None):
    now = datetime.datetime.now()
    if seg != None:
        time_init = now + datetime.timedelta(seconds=value)
    else:
        time_init = now + datetime.timedelta(minutes=value)
    esc_pressed = False
    timeout_reached = False

    def check_esc():
        nonlocal esc_pressed
        while not timeout_reached:
            time.sleep(0.1)
            if keyboard.is_pressed('esc'):
                esc_pressed = True
                break
            if exec_fn != None:
                result = exec_fn()
                print(result)
                if result != None:
                    esc_pressed = True
                    break

    # Inicia uma thread para verificar a tecla "Esc"
    esc_thread = threading.Thread(target=check_esc)
    esc_thread.start()

    # Espera até que o tempo limite seja atingido ou a tecla "Esc" seja pressionada
    while not esc_pressed:
        time_reached = check_time(time_init)
        if time_reached:
            timeout_reached = True
            break
        time.sleep(0.1)

    # Espera a thread da tecla "Esc" terminar
    esc_thread.join()

    # Retorna True se o timeout foi alcançado ou False se a tecla "Esc" foi pressionada
    if timeout_reached:
        return True
    else:
        return False
