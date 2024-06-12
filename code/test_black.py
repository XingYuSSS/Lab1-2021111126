import pytest
import graph

g = graph.WordGraph("""To explore strange new worlds,
To seek out new life and new civilizations
To find out""")

def test_case1():
    output = g.generateNewText('to strange worlds life new')
    assert output == 'to explore strange new worlds life and new'

def test_case2():
    output = g.generateNewText('to bad life')
    assert output == 'to bad life'

def test_case3():
    output = g.generateNewText(None)
    assert output == 'No input text!'

def test_case4():
    output = g.generateNewText('to out')
    assert output in ['to find out', 'to seek out']
