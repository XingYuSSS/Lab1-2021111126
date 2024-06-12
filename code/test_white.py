import pytest
import graph

g = graph.WordGraph("""To explore strange new worlds,
To seek out new life and new civilizations
To find out""")

def test_case1():
    output = g.queryBridgeWords('to', 'from')
    assert output == 'No from in the graph!'

def test_case2():
    output = g.queryBridgeWords('to', 'new')
    assert output == 'No bridge words from \"to\" to \"new\"!'

def test_case3():
    output = g.queryBridgeWords('to', 'strange')
    assert output == 'The bridge words from \"to\" to \"strange\" is: explore.'

def test_case4():
    output = g.queryBridgeWords('to', 'out')
    assert output == 'The bridge words from \"to\" to \"out\" are: seek and find.'
