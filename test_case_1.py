import requests
import configparser


config = configparser.ConfigParser()
with open('config_file.ini') as fh:
    config.read_file(fh)


def test_case1():
    path1 = config.get('url_data', 'base_url')
    resp = requests.get(f"{path1}api/users?page=2")
    assert "200" in str(resp.status_code)


def test_case2():
    path1 = config.get('url_data', 'base_url')
    resp = requests.post(f"{path1}api/users")
    print(resp.text)
    assert "201" in str(resp.status_code)


def test_case3():
    print("tester")