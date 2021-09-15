#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2021
# Leandro Toledo de Souza <devs@python-telegram-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
import pytest

from telegram import PassportElementErrorTranslationFiles, PassportElementErrorSelfie


@pytest.fixture(scope="class")
def passport_element_error_translation_files():
    return PassportElementErrorTranslationFiles(
        TestPassportElementErrorTranslationFiles.type_,
        TestPassportElementErrorTranslationFiles.file_hashes,
        TestPassportElementErrorTranslationFiles.message,
    )


class TestPassportElementErrorTranslationFiles:
    source = "translation_files"
    type_ = "test_type"
    file_hashes = ["hash1", "hash2"]
    message = "Error message"

    def test_slot_behaviour(self, passport_element_error_translation_files, mro_slots, recwarn):
        inst = passport_element_error_translation_files
        for attr in inst.__slots__:
            assert getattr(inst, attr, "err") != "err", f"got extra slot '{attr}'"
        assert not inst.__dict__, f"got missing slot(s): {inst.__dict__}"
        assert len(mro_slots(inst)) == len(set(mro_slots(inst))), "duplicate slot"
        inst.custom, inst.type = "should give warning", self.type_
        assert len(recwarn) == 1 and "custom" in str(recwarn[0].message), recwarn.list

    def test_expected_values(self, passport_element_error_translation_files):
        assert passport_element_error_translation_files.source == self.source
        assert passport_element_error_translation_files.type == self.type_
        assert isinstance(passport_element_error_translation_files.file_hashes, list)
        assert passport_element_error_translation_files.file_hashes == self.file_hashes
        assert passport_element_error_translation_files.message == self.message

    def test_to_dict(self, passport_element_error_translation_files):
        passport_element_error_translation_files_dict = (
            passport_element_error_translation_files.to_dict()
        )

        assert isinstance(passport_element_error_translation_files_dict, dict)
        assert (
            passport_element_error_translation_files_dict["source"]
            == passport_element_error_translation_files.source
        )
        assert (
            passport_element_error_translation_files_dict["type"]
            == passport_element_error_translation_files.type
        )
        assert (
            passport_element_error_translation_files_dict["file_hashes"]
            == passport_element_error_translation_files.file_hashes
        )
        assert (
            passport_element_error_translation_files_dict["message"]
            == passport_element_error_translation_files.message
        )

    def test_equality(self):
        a = PassportElementErrorTranslationFiles(self.type_, self.file_hashes, self.message)
        b = PassportElementErrorTranslationFiles(self.type_, self.file_hashes, self.message)
        c = PassportElementErrorTranslationFiles(self.type_, "", "")
        d = PassportElementErrorTranslationFiles("", self.file_hashes, "")
        e = PassportElementErrorTranslationFiles("", "", self.message)
        f = PassportElementErrorSelfie(self.type_, "", self.message)

        assert a == b
        assert hash(a) == hash(b)
        assert a is not b

        assert a != c
        assert hash(a) != hash(c)

        assert a != d
        assert hash(a) != hash(d)

        assert a != e
        assert hash(a) != hash(e)

        assert a != f
        assert hash(a) != hash(f)
