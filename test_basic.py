import pytest
from unittest.mock import patch, MagicMock
from autokolcsonzo.main import AppHandler, Valasztas, main


@pytest.fixture
def app():
    return AppHandler()


@patch('builtins.input', side_effect=['ABC-123', '2023', '12', '24'])
@patch('main.adat_betoltes', return_value=MagicMock())
def test_berles(mock_adat_betoltes, mock_input, app):
    kolcsonzo_mock = mock_adat_betoltes.return_value
    kolcsonzo_mock.auto_berles.return_value = 15000

    with patch('builtins.print') as mock_print:
        app.berles(kolcsonzo_mock)
        mock_print.assert_any_call("Bérlés sikeres! Ár: 15000 Ft")


@patch('builtins.input', side_effect=['ABC-123', '2023', '12', '24'])
@patch('main.adat_betoltes', return_value=MagicMock())
def test_lemondas(mock_adat_betoltes, mock_input, app):
    kolcsonzo_mock = mock_adat_betoltes.return_value
    kolcsonzo_mock.berles_leomondasa.return_value = True

    with patch('builtins.print') as mock_print:
        app.lemondas(kolcsonzo_mock)
        mock_print.assert_any_call("Bérlés lemondása sikeres!")


@patch('builtins.input', side_effect=['0'])
@patch('sys.exit')
def test_kilepes(mock_sys_exit, mock_input, app):
    with patch('builtins.print') as mock_print:
        app.kilepes()
        mock_print.assert_any_call("Kilépés a programból.")
        mock_sys_exit.assert_called_once()


def test_print_menu(app):
    with patch('builtins.print') as mock_print:
        app.print_menu()
        mock_print.assert_any_call("\n--- Autókölcsönző Rendszer ---")
        for valasztas in Valasztas:
            mock_print.assert_any_call(valasztas.value)


@patch('builtins.input', side_effect=['3'])
@patch('main.adat_betoltes', return_value=MagicMock())
def test_listazas_berles(mock_adat_betoltes, mock_input, app):
    kolcsonzo_mock = mock_adat_betoltes.return_value
    kolcsonzo_mock.berlesek_listazasa.return_value = ["Bérlés 1", "Bérlés 2"]

    with patch('builtins.print') as mock_print:
        app.listazas(kolcsonzo_mock)
        mock_print.assert_any_call("Bérlés 1")
        mock_print.assert_any_call("Bérlés 2")


@patch('builtins.input', side_effect=['4'])
@patch('main.adat_betoltes', return_value=MagicMock())
def test_listazas_auto(mock_adat_betoltes, mock_input, app):
    kolcsonzo_mock = mock_adat_betoltes.return_value
    kolcsonzo_mock.autok_listazasa.return_value = ["Autó 1", "Autó 2"]

    with patch('builtins.print') as mock_print:
        app.listazas(kolcsonzo_mock, True)
        mock_print.assert_any_call("Autó 1")
        mock_print.assert_any_call("Autó 2")


@patch('builtins.input', side_effect=['0'])
@patch('builtins.print')
@patch('sys.exit', side_effect=SystemExit)
def test_main(mock_exit, mock_print, mock_input):
    with pytest.raises(SystemExit):
        main()

    mock_print.assert_any_call("Kilépés a programból.")