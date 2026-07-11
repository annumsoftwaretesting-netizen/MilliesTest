# MilliesTest

Selenium + pytest UI test suite for milliescookies.com, using the
page-object pattern.

## Structure

- `pages/` – page objects (one class per page, inherit `BasePage`)
- `components/` – shared page components (e.g. cookie banner)
- `locators/` – element locators, one module per page
- `tests/smoke/` – smoke tests
- `utilities/` – driver factory, config reader, logger
- `testdata/` – non-secret test configuration

## Setup

```bash
pip install -r requirements.txt
```

## Credentials

Secrets are read from environment variables and must NOT be committed:

```bash
export UAT_USERNAME=...        # UAT basic-auth username
export UAT_PASSWORD=...        # UAT basic-auth password
export TEST_USER_EMAIL=...     # site account email (optional)
export TEST_USER_PASSWORD=...  # site account password (optional)
```

The UAT host itself lives in `testdata/config.json` (`uat_url`).

## Running tests

```bash
pytest                          # chrome, headed
pytest --browser edge           # edge
pytest --browser firefox        # firefox
pytest --headless               # headless mode (CI)
```

Screenshots of failing tests are written to `screenshots/` (git-ignored).
