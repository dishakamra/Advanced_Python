import builtins
from greeter import greet

def test_greet(monkeypatch):
    monkeypatch.setattr(builtins, 'input', lambda _: 'Alice')
    assert greet() == "Hello, Alice!"
