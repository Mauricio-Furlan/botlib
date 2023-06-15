from unittest import mock

import pytest

from actions.bot import Bot
from actions.my_keyboard import key_down, press, release_key


@pytest.fixture
def bot():
    return Bot()


def test_search_image(bot):
    # Mocking pyautogui.locateOnScreen
    with mock.patch('pyautogui.locateOnScreen') as mock_locate:
        mock_locate.return_value = (100, 100, 50, 50)  # Mock image coordinates

        # Perform the search
        bot._search_image('test_img.PNG')

        # Check if the attributes are set correctly
        assert bot.box == (100, 100, 50, 50)
        assert bot.x == 125
        assert bot.y == 125


def test_search_image_not_found(bot):
    # Mocking pyautogui.locateOnScreen to return None (image not found)
    with mock.patch('pyautogui.locateOnScreen') as mock_locate:
        mock_locate.return_value = None

        # Perform the search
        bot._search_image('test_img.PNG')

        # Check if the attributes are not set
        assert not hasattr(bot, 'box')
        assert not hasattr(bot, 'x')
        assert not hasattr(bot, 'y')


def test_wait_image_found(bot):
    # Mocking the _search_image method to return self
    with mock.patch.object(
        bot, '_search_image', return_value=bot
    ) as mock_search:
        # Perform the wait
        result = bot.wait_image('test_img.PNG', seg=5)

        # Check if _search_image was called
        mock_search.assert_called_once_with(
            'test_img.PNG', confidence=0.85, region=None
        )

        # Check if the result is the same instance of bot
        assert result is bot


# def test_moveTo_with_coordinates(bot):
#     # Mocking pyautogui.moveTo
#     with mock.patch('pyautogui.moveTo') as mock_moveTo:
#         # Perform the move
#         bot.moveTo(300, 300)

#         # Check if pyautogui.moveTo was called with the correct arguments
#         mock_moveTo.assert_called_once_with(300, 300)


# def test_moveTo_without_coordinates(bot):
#     # Set the coordinates in the bot instance
#     bot.x = 100
#     bot.y = 200

#     # Mocking pyautogui.moveTo
#     with mock.patch('pyautogui.moveTo') as mock_moveTo:
#         # Perform the move
#         bot.moveTo()

#         # Check if pyautogui.moveTo was called with the correct arguments
#         mock_moveTo.assert_called_once_with(100, 200)


# Similarly, you can write tests for the other methods in the Bot class.


# Run the tests
pytest.main()


# @mark.parametrize(
#     'size, expected',
#     [((1920, 1080), (960, 540)), ((1600, 900), (800, 450))],
# )
# def test_return_center_of_screen_position(size, expected):
#     with patch('pyautogui.size', return_value=size):
#         with patch('pyautogui.moveTo') as mock_moveTo, patch(
#             'pyautogui.click'
#         ) as mock_click:
#             result = move_to_center_on_screen()
#             mock_moveTo.assert_called_once_with(*expected, 0.0)
#             mock_click.assert_called_once_with(clicks=0, button='left')
#             assert result == expected
