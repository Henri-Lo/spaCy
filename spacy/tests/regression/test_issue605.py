# coding: utf-8
from __future__ import unicode_literals

from ...attrs import LOWER, ORTH
from ...tokens import Doc
from ...vocab import Vocab
from ...matcher import Matcher


def return_false(doc, ent_id, label, start, end):
    return False


def test_matcher_accept():
    doc = Doc(Vocab(), words=['The', 'golf', 'club', 'is', 'broken'])

    golf_pattern =     [
        { ORTH: "golf"},
        { ORTH: "club"}
    ]
    matcher = Matcher(doc.vocab)

    matcher.add_entity('Sport_Equipment', acceptor=return_false)
    matcher.add_pattern("Sport_Equipment", golf_pattern)
    match = matcher(doc)

    assert match == []
