"""The package must declare type imap and credential_type imap on import."""

from lynguine.access.io_types import get_io_type


def test_import_registers_imap():
    import lynguine_imap  # noqa: F401

    spec = get_io_type("imap")
    assert spec is not None
    assert spec.name == "imap"
    assert spec.credential_type == "imap"
    assert spec.write is None
    assert spec.read is lynguine_imap.read_imap


def test_read_rejects_missing_credential_value():
    import lynguine_imap

    try:
        lynguine_imap.read_imap({})
    except ValueError as exc:
        assert "credential_value" in str(exc)
    else:
        raise AssertionError("expected ValueError for missing credential_value")
