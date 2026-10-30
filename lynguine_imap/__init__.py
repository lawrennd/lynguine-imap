"""IMAP subjects as a lynguine IO type.

This is inbound mail for *access*, not referia's outbound ``type: email``
drafts. Importing this module registers ``type: imap`` and the ``imap``
credential validator. lynguine fetches the secret; this package reads
``credential_value``.
"""

from __future__ import annotations

import pandas as pd

from lynguine.access.io import register_io_type
from lynguine.security.credentials import get_credential_manager


def validate_imap(credential) -> bool:
    """Accept a host/user/password mapping stored as the CIP-0005 value."""
    value = credential.get("value", credential) if isinstance(credential, dict) else credential
    if not isinstance(value, dict):
        return False
    return all(
        isinstance(value.get(k), str) and value[k].strip()
        for k in ("host", "user", "password")
    )


get_credential_manager().register_validator("imap", validate_imap)


def read_imap(details: dict) -> pd.DataFrame:
    """Read mailbox subjects.

    Required YAML:

    * ``credential:`` — CIP-0005 key (lynguine binds ``credential_value``)
    * ``folder:`` — mailbox folder, default ``INBOX``

    The IMAP fetch is not implemented yet; the registration form is.
    """
    cred = details.get("credential_value")
    if not isinstance(cred, dict):
        raise ValueError("IMAP read expected credential_value mapping from lynguine")
    folder = details.get("folder", "INBOX")
    if not isinstance(folder, str) or not folder.strip():
        raise ValueError('Type "imap" requires folder: <mailbox name>')
    raise NotImplementedError(
        "lynguine-imap registers type: imap; the IMAP subject reader is next"
    )


register_io_type(
    "imap",
    read=read_imap,
    credential_type="imap",
)
