# lynguine-imap

IMAP mailbox *subjects* as a lynguine tabular source (`type: imap`).

This is inbound access. It is not referia's outbound `type: email` drafts.

Point at the plugin form in lynguine:

https://github.com/lawrennd/lynguine/blob/main/docs/getting_started/io_plugins.rst

## Authorisation

This package **declares** `credential_type="imap"`. lynguine fetches the CIP-0005
secret named by `credential:` and passes it as `credential_value` (host, user,
password).

```yaml
input:
  type: imap
  folder: INBOX
  credential: my_mail
plugins:
  - lynguine_imap
```

## Status

Registration and the credential contract are in place. The IMAP fetch is not
implemented yet (`read_imap` raises `NotImplementedError` once credentials are
bound).
