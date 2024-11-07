import json
import unittest as ut
from unittest.mock import Mock
from unittest.mock import MagicMock

from SeminarioC214.src.main.buscaHorario import buscaHorario
from SeminarioC214.src.test import HorariosJson


class testHorarioDeAtendimento(ut.TestCase):

    def testHorarioServiceMock(self):
        mockHorarioService = Mock()
        mockHorarioService.Procura.return_value = HorariosJson.HorariosJsons.PaiDoConrado

        mocked = buscaHorario(mockHorarioService)

        result = mocked.buscaHorario(2)

        self.assertEqual(result["nomeDoProfessor"], json.loads(HorariosJson.HorariosJsons.PaiDoConrado)["nomeDoProfessor"])

        mockHorarioService.Procura.assert_called_once()

    def testHorarioServiceMagicMock(self):
        mockHorarioService = MagicMock()
        mockBuscaHorario = buscaHorario(mockHorarioService)
        mockBuscaHorario.buscaHorario = MagicMock(return_value=HorariosJson.HorariosJsons.arr)
        result = mockBuscaHorario.buscaHorario(2)

        iterado = mockBuscaHorario.buscaHorario(2).__iter__()
        print(iterado.__next__())
        iterado.__next__()
        print(iterado.__next__())

        self.assertEqual(result, HorariosJson.HorariosJsons.arr)
