import pytest

from string_utils import StringUtils

string_utils = StringUtils()

#Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст (1-5)
@pytest.mark.parametrize("string, result", [("skypro", "Skypro"),("Skypro", "Skypro")])
def test_capitilize_positive(string, result):
    string_utils = StringUtils()
    res = string_utils.capitilize(string)
    assert res == result

@pytest.mark.parametrize("string, result", [("", ""),("   ", "   "),("123abc", "123abc")])
def test_capitilize_negative(string, result):
    string_utils = StringUtils()
    res = string_utils.capitilize(string)
    assert res == result

#Принимает на вход текст и удаляет пробелы в начале, если они есть
@pytest.mark.parametrize("string, result", [(" Skypro", "Skypro"), ("  Skypro", "Skypro"), ("     Skypro", "Skypro"), ("Skypro", "Skypro")])
def test_trim_positive(string, result):
    string_utils = StringUtils()
    res = string_utils.trim(string)
    assert res == result

@pytest.mark.parametrize("string, result", [("", ""), ("  ", ""), ("  123Skypro", "123Skypro")])
def test_trim_negative(string, result):
    string_utils = StringUtils()
    res = string_utils.trim(string)
    assert res == result

#Принимает на вход текст с разделителем и возвращает список строк. \n
@pytest.mark.parametrize("string, delimeter, result", [("a,b,c,d", ",", ["a", "b", "c", "d"]),("1:2:3:4", ":", ["1", "2", "3", "4"]), ("Привет Александр", ",", ["Привет", "Александр"])])
def test_to_list_positive(string, delimeter, result):
   string_utils = StringUtils()
   res = string_utils.to_list(string, delimeter)
   assert res == result

@pytest.mark.parametrize("string, delimeter, result", [("", ",", []),("один, два, три", ":", ["один, два, три"]), ("1,2,3,4,5", ",", ["1,2,3,4,5"])])
def test_to_list_negative(string, delimeter, result):
   string_utils = StringUtils()
   res = string_utils.to_list(string, delimeter)
   assert res == result   

#Возвращает `True`, если строка содержит искомый символ и `False` - если нет \n   
@pytest.mark.parametrize("string, symbol, result",[("Skypro", "S", True), ("Skypro", "P", False)])
def test_contains_positive(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.contains(string, symbol)
    assert res == result

@pytest.mark.xfail(strict=False)
@pytest.mark.parametrize("string, symbol, result",[("Skypro", "y", True), ("Skypro", "S", True)])
def test_contains_negative(string, symbol, result):
    string_utils = StringUtils()
    with pytest.raises(ValueError):
        res = string_utils.contains(string,symbol)

#Удаляет все подстроки из переданной строки \n 
@pytest.mark.parametrize("string, symbol, result",[("SkyPro", "k", "SyPro"),("SkyPro", "Pro", "Sky"),("SkyPro", "Sky", "Pro")])
def test_delete_symbol_positive(string, symbol,result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(string,symbol)
    assert res == result
    
@pytest.mark.parametrize("string, symbol, result",[("SkyPro", "x", "SkyPro")])
def test_delete_symbol_negative(string, symbol,result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(string,symbol)
    assert res == result

#Возвращает `True`, если строка начинается с заданного символа и `False` - если нет \n 
@pytest.mark.parametrize("string, symbol,result", [("SkyPro", "S", True), ("SkyPro", "P", False)])
def test_starts_with_positive(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.starts_with(string, symbol)
    assert res == result

@pytest.mark.parametrize("string, symbol,result", [("SkyPro", "x", False), ("SkyPro", "k", False)])
def test_starts_with_negative(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.starts_with(string, symbol)
    assert res == result

#Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет \n 
@pytest.mark.parametrize("string, symbol, result", [("SkyPro", "o", True), ("Skypro", "y", False)])
def test_end_with_positive(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.end_with(string, symbol)
    assert res == result

@pytest.mark.parametrize("string, symbol, result", [("SkyPro", "y", False), ("Skypro", "j", False)])
def test_end_with_negative(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.end_with(string, symbol)
    assert res == result 

#Возвращает `True`, если строка пустая и `False` - если нет \n 
@pytest.mark.parametrize("string, result", [("", True), ("  ", True), ("Skypro", False)])
def test_is_empty_positive(string,result):
    string_utils = StringUtils()
    res = string_utils.trim(string)
    res = string_utils.is_empty("")
    assert res == result

#Преобразует список элементов в строку с указанным разделителем \n 
@pytest.mark.parametrize("lst, joiner, result", [([1, 2, 3, 4], ", ", "1, 2, 3, 4"),(["Sky", "Pro"], ", ", "Sky, Pro")])
def test_list_to_string_positive(lst, joiner, result):
    string_utils = StringUtils()
    res = string_utils.list_to_string(lst, joiner)
    assert res == result
 
@pytest.mark.parametrize("lst, joiner, result", [([], ", ", ""),([1], ", ", "1"),([1, 2, 3], "- ", "1-2-3"),(["Sky", "Pro"], "?", "Sky?Pro")])
def test_list_to_string_negative(lst, joiner, result):
    string_utils = StringUtils()
    res = string_utils.list_to_string(lst, joiner)
    assert res == result
   